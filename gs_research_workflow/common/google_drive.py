# -*- coding: UTF-8 -*-

"""
提供 google drive 的一些功能接口封装
    接口文档 see : https://developers.google.com/drive/api/v3/quickstart/python
"""
from typing import NamedTuple, List, Optional, Union

from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload
from gs_framework.gs_resource import set_http_proxy
from googleapiclient.discovery import build
from mimetypes import guess_type


MIME_FOLDER = "application/vnd.google-apps.folder"
MIME_COLAB = "application/vnd.google.colaboratory"
MIME_BINARY = "application/x-binary"


class FolderWithID(NamedTuple):
    name: str
    id: str
    mimeType: str
    createdTime: str
    modifiedTime: str
    parents: List[str]


class GoogleDriveWrapper:
    _RET_GFILE_FIELDS = "id,name,parents,createdTime,modifiedTime,mimeType"
    _LIST_FIELDS = f"files({_RET_GFILE_FIELDS})"

    def __init__(self, token: Credentials):
        set_http_proxy()
        # NOTE : cache_discovery 设为 False 可以避免一些 module 内部因为 cache 引起的 Exception
        service = build('drive', 'v3', credentials=token, cache_discovery=False)
        self._g_files = service.files()
        self._service = service

    def query_folder(self, folder_path: List[str]) -> List[FolderWithID]:
        """按照类似于文件系统的方式，匹配到一个文件路径的数据结构，必须从最根目录开始"""
        ls_rlt = list()
        last_parent_id = None
        for folder_name in folder_path:
            q = f"name = '{folder_name}' and mimeType='{MIME_FOLDER}'"
            if last_parent_id is not None:
                q += f" and '{last_parent_id}' in parents"
            data = self._g_files.list(q=q, fields=GoogleDriveWrapper._LIST_FIELDS).execute()

            assert len(data.get("files", [])) > 0  # 假定入参保证了一定能找到内容
            folder_info = FolderWithID(**data["files"][0])
            ls_rlt.append(folder_info)
            last_parent_id = folder_info.id
        return ls_rlt

    def query_object_by_name(self, name: str, parent_id: str) -> Optional[FolderWithID]:
        """查询某个目录下的 object ， 一般在更新文件之前，先查询一次"""
        q = f"name = '{name}' and '{parent_id}' in parents"
        data = self._g_files.list(q=q, fields=GoogleDriveWrapper._LIST_FIELDS).execute()
        if len(data.get("files", [])) > 0:
            return FolderWithID(**data["files"][0])
        else:
            return None

    def create_or_update_file(self, gdrive_file_name: str, mime_type: str,
                              parent_path_str_or_obj: Union[str, FolderWithID],
                              local_file_path: str = None,
                              get_only: bool = False) -> FolderWithID:
        """
        在某个指定的位置，新建或者更新一个文件的内容，支持创建一个文件或者一个 folder

        see https://developers.google.com/drive/api/v3/manage-uploads
        see https://developers.google.com/drive/api/v3/reference/files

        Parameters
        ----------
        gdrive_file_name : str
            在 google drive 上的文件名或者 folder name

        mime_type : str
            mime 的类型

        parent_path_str_or_obj : str
            父路径，用 "/" 分隔，不需要第一个 和最后一个 "/" ， 为了能够提供和 file system 相一致的数据模型，要求该路径是已经创建过的

        local_file_path : str
            待上传的文件在本地的位置，如果是产生一个 Folder ，则这项内容留空

        Returns
        -------

        """
        parent_folder_id = None
        if isinstance(parent_path_str_or_obj, str):
            if parent_path_str_or_obj.startswith("/"):
                parent_path_str_or_obj = parent_path_str_or_obj[1:]
            parent_folder = self.query_folder(parent_path_str_or_obj.split("/"))
            parent_folder_id = parent_folder[-1].id
        elif isinstance(parent_path_str_or_obj, FolderWithID):
            parent_folder_id = parent_path_str_or_obj.id
        else:
            raise RuntimeError(f"invalid argument parent_path_str_or_obj = {parent_path_str_or_obj}")

        target_file = self.query_object_by_name(gdrive_file_name, parent_folder_id)
        if local_file_path is None:  # 创建或者更新一个folder
            if target_file:  # folder 已经创建过的，不允许再重复创建
                return target_file
            assert not get_only
            assert mime_type == MIME_FOLDER
            body = {
                'name': gdrive_file_name,
                'mimeType': mime_type,
                "parents": [parent_folder_id]
            }
            file = self._g_files.create(body=body, fields=GoogleDriveWrapper._RET_GFILE_FIELDS).execute()
            return FolderWithID(**file)
        else:  # 创建一个文件
            body = {
                'name': gdrive_file_name,
                'mimeType': mime_type,
            }
            media = MediaFileUpload(local_file_path,
                                    mimetype=mime_type,
                                    resumable=True)
            if target_file is None:  # create
                assert not get_only
                body["parents"] = [parent_folder_id]
                # 尝试重新 new 新的 files 对象
                file = self._service.files().create(body=body, media_body=media,
                                                    fields=GoogleDriveWrapper._RET_GFILE_FIELDS).execute()
                # file = self._g_files.create(body=body, media_body=media,
                #                             fields=GoogleDriveWrapper._RET_GFILE_FIELDS).execute()
                return FolderWithID(**file)
            else:  # update
                # 尝试重新 new 新的 files 对象
                file = self._service.files().update(fileId=target_file.id, body=body, media_body=media,
                                                    fields=GoogleDriveWrapper._RET_GFILE_FIELDS).execute()
                # file = self._g_files.update(fileId=target_file.id, body=body, media_body=media,
                #                             fields=GoogleDriveWrapper._RET_GFILE_FIELDS).execute()
                return FolderWithID(**file)

        # body = {
        #     'name': gdrive_file_name,
        #     # 'mimeType': 'application/vnd.google-apps.colab'
        # }
        # file = self._g_files.create(body=body, media_body=media_body,fields="id").execute()
        # return file


if __name__ == "__main__":
    """
{
 "kind": "drive#file",
 "id": "1oN7NASHxjZYgG_ZXsnnjos8JeTGgCq5m",
 "name": "ColabVMRequirements.ipynb",
 "mimeType": "application/vnd.google.colaboratory"
}
    """

    from gs_research_workflow.common.google_oauth import get_google_token
    from gs_research_workflow.auto_ml.notebook.colab_notebook_generator import notebook_by_replace_one_cell

    token = get_google_token()
    gdrive = GoogleDriveWrapper(token)
    # GS / NNI_EXPERIMENTS / HPO
    # file_info = gdrive.create_or_update_file("HPO", MIME_FOLDER,
    #                                          "GS/NNI_EXPERIMENTS")
    _code = """
print("hello world v4!")"""
    file_path = notebook_by_replace_one_cell(cell_idx=4, new_code=_code, new_nb_name="my_first_new_notebook.ipynb")
    file_info = gdrive.create_or_update_file("my_first_new_notebook_v3.ipynb", MIME_COLAB,
                                             "GS/ModelData/InceptionTime/test_folder", file_path)

    print(file_info)
    # gdrive.read_file("1oN7NASHxjZYgG_ZXsnnjos8JeTGgCq5m")
    # file_path = "/tmp/tmpzijxl577.ipynb"
    # gdrive.upload_file(file_path, "tmpzijxl576.ipynb","application/x-ipynb+json")
