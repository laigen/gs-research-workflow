# -*- coding: UTF-8 -*-
__author__ = "laigen"

"""生成聚源的 ddl entity define 的相关代码
NOTE : 一个 table 对象一个 py file ， 避免会产生一次 import 太多内容时导致的 IDE 速度变慢
"""

import pandas as pd
import os
import logging
import pathlib

logger = logging.getLogger(__name__)


class PyTableCodeGenerator:

    @staticmethod
    def generate_one_table(df: pd.DataFrame):
        import re
        table_py_template = """class {table_name_en}(SQLTableEntity):
    name: str = '{table_name_en}'
    
    chn_name: str = '{table_name_zh}'
    
    business_unique: str = '{business_unique}'
    
    refresh_freq: str = \"\"\"{table_freq}\"\"\"
    
    comment: str = \"\"\"{table_info}\"\"\""""

        column_py_template = """    {col_name}: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='{tbl_name}', column_name='{col_name}', column_type='{col_type}', nullable={nullable}, chn_name='{col_lb}')
    \"\"\"{col_lb}:{col_info}\"\"\""""

        ls_cols_code = []
        ls_set_all_columns_code = []
        i_valid_rows = 0
        table_paras = {}
        for index, row in df.iterrows():
            if pd.isnull(row["列名"]):
                continue
            if pd.isnull(row["类型"]):
                continue
            if pd.isnull(row["table_name_en"]):
                continue
            if row["列名"] == "null":
                continue
            if not re.match("^[0-9]*$", row["序号"]):
                continue

            i_valid_rows += 1
            if i_valid_rows == 1:
                table_paras["table_name_en"] = row["table_name_en"]
                table_paras["table_name_zh"] = '' if pd.isnull(row["table_name_zh"]) else row["table_name_zh"]
                table_paras["business_unique"] = '' if pd.isnull(row["业务唯一性"]) else row["业务唯一性"]
                table_paras["table_freq"] = '' if pd.isnull(row["表数据更新频率"]) else row["表数据更新频率"]
                table_paras["table_info"] = '' if pd.isnull(row["说明解释"]) else row["说明解释"]

            ls_cols_code.append(column_py_template.format(table_name_en=table_paras["table_name_en"],
                                                          tbl_name=table_paras["table_name_en"],
                                                          col_name=row["列名"], col_type=row["类型"],
                                                          nullable=True if row["空否"] == "否" else False, col_lb=row["中文名称"],
                                                          col_info='' if pd.isnull(row["备注"]) else row["备注"]))
        if i_valid_rows == 0:
            return ""

        py_code = table_py_template.format(**table_paras) + os.linesep * 2 + (os.linesep * 2).join(
            ls_cols_code) + os.linesep
        return py_code

    @staticmethod
    def generate_table_object(csv_path):
        """
        从抓取的数据内容中，生成所有的 table object
        :param csv_path:
        :return:
        """
        import fnmatch
        import codecs

        for file in os.listdir(csv_path):
            if fnmatch.fnmatch(file, "*.csv"):
                logger.info(f"start read: {csv_path}{os.path.sep}{file}")
                df = pd.read_csv(csv_path + os.path.sep + file, header=0)
                # 一个 table 对象一个文件
                for tbl_name in df["table_name_en"].unique():
                    if pd.isna(tbl_name):
                        continue
                    table_category = file.replace(".csv", "")
                    "".strip()
                    output_path = os.path.join(os.path.dirname(__file__), "ddl_entities", table_category)
                    pathlib.Path(output_path).mkdir(parents=True,exist_ok=True)
                    output_py_file = os.path.join(output_path, tbl_name.strip() + ".py")
                    logger.info(f"create file {output_py_file}")

                    with codecs.open(output_py_file, "w+", "utf-8") as f:
                        f.write("# -*- coding: utf-8 -*-" + os.linesep)
                        f.write("# Auto Generated Code .  DO NOT EDIT!" + os.linesep * 2)

                        f.write("from gs_research_workflow.time_series.data_vendor.jy.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity" + os.linesep*3)

                        code = PyTableCodeGenerator.generate_one_table(df[df["table_name_en"] == tbl_name].sort_values(by=["序号"], ascending=True))
                        if code != "":
                            f.write(code)
                            f.write(os.linesep)

    @staticmethod
    def generate_all_table_defs():
        PyTableCodeGenerator.generate_table_object(os.path.join(os.path.dirname(__file__), "resource", "ddl"))
