# -*- coding: UTF-8 -*-


# NOTE : 先定义一个 dummy 的 entity 基类，以后再调整成其他位置的 entity 对象


class Entity:
    ...


class TableColumnDeclarationEntity(Entity):
    """Table Column 的定义声明信息"""
    def __init__(self, tbl_name: str, column_name: str, column_type: str, nullable: bool, chn_name: str):
        self.tbl_name: str = tbl_name
        """表名"""

        self.name: str = column_name
        """取csv文件中列'列名'"""

        self.column_type: str = column_type
        """取'类型'"""

        self.nullable: bool = nullable
        """取 '空否' """

        self.chn_name: str = chn_name
        """取 '中文名称'"""


class SQLTableEntity(Entity):
    name: str = ""
    """取 'table_name_en' """

    chn_name: str = ""
    """取 'table_name_zh'"""

    business_unique: str = ""
    """取 ‘业务唯一性’"""

    refresh_freq: str = ""
    """取 '表数据更新频率'"""

    comment: str = ""
    """ 取 '说明解释' """

    def __init__(self):
        super().__init__()

    @classmethod
    def table_name(cls) -> str:
        return cls.name
