# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_LeaderStockAlter(SQLTableEntity):
    name: str = 'LC_LeaderStockAlter'
    
    chn_name: str = '公司领导人持股变动'
    
    business_unique: str = 'InnerCode,AlternationDate,SerialNum,StockHolder'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """收录深沪交易所披露的上市公司领导人及其亲属买卖所在公司股份的情况。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    ConnectionDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='ConnectionDesc', column_type='varchar(50)', nullable=False, chn_name='与领导人关系描述')
    """与领导人关系描述:"""

    Connection: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='Connection', column_type='int', nullable=False, chn_name='与领导人关系')
    """与领导人关系:与领导人关系(Connection)与(CT_SystemConst)表中的DM字段关联，令LB = 1499，得到与领导人关系的具体描述：1-本人，2-父母，3-配偶，4-子女，5-兄弟姐妹，6-受控法人，9-其他，11-上市公司股东的关联人，12-上市公司的关联人。"""

    HoldSumBeforAlter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='HoldSumBeforAlter', column_type='decimal(19,2)', nullable=False, chn_name='变动前持股数(股)')
    """变动前持股数(股):"""

    StockSumChanging: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='StockSumChanging', column_type='decimal(19,2)', nullable=False, chn_name='变动股数(股)')
    """变动股数(股):"""

    AvgPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='AvgPrice', column_type='decimal(19,4)', nullable=False, chn_name='变动均价(元/股)')
    """变动均价(元/股):"""

    ChangeProportion: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='ChangeProportion', column_type='decimal(19,8)', nullable=False, chn_name='变动比例(%)')
    """变动比例(%):"""

    HoldSumAfterAlter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='HoldSumAfterAlter', column_type='decimal(19,2)', nullable=False, chn_name='变动后持股数(股)')
    """变动后持股数(股):"""

    AlternationReasonDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='AlternationReasonDesc', column_type='varchar(100)', nullable=False, chn_name='变动原因描述')
    """变动原因描述:"""

    AlternationReason: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='AlternationReason', column_type='int', nullable=False, chn_name='变动原因')
    """变动原因:变动原因(AlternationReason)与(CT_SystemConst)表中的DM字段关联，令LB = 1500，得到变动原因的具体描述：11-竞价交易，12-二级市场买卖，21-分红送转，22-老股东配售，23-大宗交易，31-股权激励，32-股改对价，41-新股申购，42-增发配股，99-其他。"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='CompanyCode', column_type='int', nullable=False, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    AlternationDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='AlternationDate', column_type='datetime', nullable=False, chn_name='变动日期')
    """变动日期:"""

    ReportDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='ReportDate', column_type='datetime', nullable=False, chn_name='填报日期')
    """填报日期:"""

    SerialNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='SerialNum', column_type='int', nullable=False, chn_name='序号')
    """序号:"""

    LeaderName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='LeaderName', column_type='varchar(50)', nullable=False, chn_name='领导人姓名')
    """领导人姓名:"""

    PositionDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='PositionDesc', column_type='varchar(100)', nullable=False, chn_name='职务描述')
    """职务描述:"""

    StockHolder: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_LeaderStockAlter', column_name='StockHolder', column_type='varchar(50)', nullable=False, chn_name='股份变动人姓名')
    """股份变动人姓名:"""

