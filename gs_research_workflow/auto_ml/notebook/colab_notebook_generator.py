# -*- coding: utf-8 -*-

"""
生成 trail 的 .ipynb 文件
"""
import logging
import os
import nbformat
import tempfile

logger = logging.getLogger(__name__)


def notebook_by_replace_one_cell(template_file_name: str = 'colab_template',
                                 cell_idx: int = 0, new_code: str = "",
                                 new_nb_name: str = None) -> str:
    """
    通过替换template一个cell 的方式，生成新的 notebook 文件

    Parameters
    ----------
    template_file_name
            template  的文件名

    cell_idx
            替换的 cell 索引

    new_code
            新的代码
            
    new_nb_name
            新 notebook name ， None 表示不修改

    Returns
    -------
        output_file_path

    """
    template_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), f"{template_file_name}.ipynb")
    # logger.info(f"read notebook file {template_file}")

    with open(template_file, "rt", encoding='utf-8') as f:
        nb_nodes = nbformat.read(f, nbformat.NO_CONVERT)
    assert nb_nodes.cells[cell_idx].cell_type == "code"
    nb_nodes.cells[cell_idx].source = new_code
    if new_nb_name:
        nb_nodes.metadata.colab.name = new_nb_name

    with tempfile.NamedTemporaryFile("wt", suffix=".ipynb", delete=False, encoding="utf-8-sig") as nf:
        nbformat.write(nb_nodes, nf)
        output_file_path = nf.name
    return output_file_path


if __name__ == "__main__":
    # abc

    _code = """
print("hello world!")
"""
    file_path = notebook_by_replace_one_cell(cell_idx=4, new_code=_code, new_nb_name="my_first_new_notebook.ipynb")
    print(file_path)
