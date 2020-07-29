# -*- coding: UTF-8 -*-

"""
获取某个可以用于操作 google drive 的 credential 内容
预先准备：
    1) 先在 WSL 中运行 "gs-desktop-env" project 中的 "gs_desktop_envs/google/oauth.py" 文件，将 用于操作数据的账号的 cred 文件保存到 arctic 中备用
        目前使用的操作账号为 laigen.test1@gmail.com
"""
import pickle

from google.oauth2.credentials import Credentials
from gs_framework.gs_resource import set_http_proxy
import os
from google.auth.transport.requests import Request

from gs_framework.utilities import md5_str
from gs_research_workflow.common.arctic_binary import ArcticBinary, GOOG_TOKEN_LIB

_DEFAULT_GOOG_ACCOUNT: str = "" # your google account
"""目前平台使用的账号内容"""

# _SYMBOL_DEFAULT_CREDENTIAL:str = "gs_default_cred"
# """credential 信息存放的位置"""

def get_google_token(acct: str = _DEFAULT_GOOG_ACCOUNT, force_refresh_pkl=False) -> Credentials:
    # NOTE: 这里应该是不需要 credential 的，只需要授权过的 token 即可，所以相关 credential 的代码都暂时先注释掉
    set_http_proxy()
    # cred_file_path = os.path.join("/tmp", "gs_default_google_cred.pkl")
    token_file_path = os.path.join("/tmp", f"gtoken_{md5_str(acct)}.pkl")
    if force_refresh_pkl:
        # if os.path.isfile(cred_file_path):
        #     os.remove(cred_file_path)
        if os.path.isfile(token_file_path):
            os.remove(token_file_path)

    # if not os.path.isfile(cred_file_path):
    #     bin_data = arctic_bin.read_bin_object(_SYMBOL_DEFAULT_CREDENTIAL)
    #     if bin_data is None:
    #         raise RuntimeError("Google credential data is not found in arctic mongo")
    #     with open(cred_file_path, "wb") as f:
    #         f.write(bin_data)
    if not os.path.isfile(token_file_path):
        arctic_bin = ArcticBinary(lib_name=GOOG_TOKEN_LIB, mongo_db="google")
        bin_data = arctic_bin.read_bin_object(acct)
        if bin_data is None:
            raise RuntimeError(f"Google account '{acct}' token data is not found in arctic mongo")
        with open(token_file_path, "wb") as f:
            f.write(bin_data)
    # credential = None
    # with open(cred_file_path, "rb") as f:
    #     credential = bytes_2_object(f.read())
    token = None
    with open(token_file_path, "rb") as f:
        token = pickle.load(f)

    if token and token.expired and token.refresh_token:
        token.refresh(Request())
        # refresh 之后，把 refresh 完成的 token 进行保存
        with open(token_file_path, "wb") as f:
            pickle.dump(token, f)
    return token


if __name__ == "__main__":
    from googleapiclient.discovery import build

    token = get_google_token()
    # 试验的代码
    service = build('drive', 'v3', credentials=token)

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
