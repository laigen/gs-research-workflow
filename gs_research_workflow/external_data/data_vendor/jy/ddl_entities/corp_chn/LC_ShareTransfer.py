# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_ShareTransfer(SQLTableEntity):
    name: str = 'LC_ShareTransfer'
    
    chn_name: str = '股东股权变动'
    
    business_unique: str = '无'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.收录公司股东股权转让、二级市场买卖、股权拍卖、大宗交易、股东重组等引起股东股权变动方面的明细资料，并包含与股权分置改革相关的股东增持、减持等信息。
2.数据范围：1996-01-26至今
3.信息来源：上交所和深交所大宗交易公开信息、临时公告等。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    TransfererName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='TransfererName', column_type='varchar(100)', nullable=False, chn_name='股权出让方名称')
    """股权出让方名称:"""

    TansfererEcoNature: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='TansfererEcoNature', column_type='int', nullable=False, chn_name='股权出让方经济性质')
    """股权出让方经济性质:"""

    TranShareType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='TranShareType', column_type='int', nullable=False, chn_name='出让股权性质')
    """出让股权性质:出让股权性质(TranShareType)与(CT_SystemConst)表中的DM字段关联，令LB = 1040，得到出让股权性质的具体描述：1-国家股，2-国有法人股，3-外资法人股，4-其他法人股，5-流通A股，6-B股，7-H股，8-转配股，9-专项资产管理计划转让，10-资产支持证券转让，11-中小企业私募债转让，12-中国存托凭证。"""

    SumBeforeTran: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='SumBeforeTran', column_type='decimal(16,0)', nullable=False, chn_name='出让前持股数量(股)')
    """出让前持股数量(股):"""

    PCTBeforeTran: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='PCTBeforeTran', column_type='decimal(19,8)', nullable=False, chn_name='出让前持股比例')
    """出让前持股比例:"""

    SNBeforeTran: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='SNBeforeTran', column_type='smallint', nullable=False, chn_name='出让前股东序号')
    """出让前股东序号:"""

    SumAfterTran: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='SumAfterTran', column_type='decimal(16,0)', nullable=False, chn_name='出让后持股数量(股)')
    """出让后持股数量(股):"""

    ResSumAfterTran: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='ResSumAfterTran', column_type='decimal(16,0)', nullable=False, chn_name='其中:出让后有限售股数(股)')
    """其中:出让后有限售股数(股):"""

    NonResSumAfterTran: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='NonResSumAfterTran', column_type='decimal(16,0)', nullable=False, chn_name='其中:出让后无限售股数(股)')
    """其中:出让后无限售股数(股):"""

    PCTAfterTran: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='PCTAfterTran', column_type='decimal(19,8)', nullable=False, chn_name='出让后持股比例')
    """出让后持股比例:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='InnerCode', column_type='int', nullable=False, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。"""

    SNAfterTran: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='SNAfterTran', column_type='smallint', nullable=False, chn_name='出让后股东序号')
    """出让后股东序号:"""

    ReceiverName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='ReceiverName', column_type='varchar(100)', nullable=False, chn_name='股权受让方名称')
    """股权受让方名称:"""

    ReceiverEcoNature: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='ReceiverEcoNature', column_type='int', nullable=False, chn_name='股权受让方经济性质')
    """股权受让方经济性质:"""

    SumAfterRece: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='SumAfterRece', column_type='decimal(16,0)', nullable=False, chn_name='受让后持股数量(股)')
    """受让后持股数量(股):"""

    ResSumAfterRece: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='ResSumAfterRece', column_type='decimal(16,0)', nullable=False, chn_name='其中:受让后有限售股数(股)')
    """其中:受让后有限售股数(股):"""

    NonResSumAfterRece: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='NonResSumAfterRece', column_type='decimal(16,0)', nullable=False, chn_name='其中:受让后无限售股数(股)')
    """其中:受让后无限售股数(股):"""

    PCTAfterRece: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='PCTAfterRece', column_type='decimal(19,8)', nullable=False, chn_name='受让后持股比例')
    """受让后持股比例:"""

    SNAfterRece: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='SNAfterRece', column_type='smallint', nullable=False, chn_name='受让后股东序号')
    """受让后股东序号:"""

    TranMode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='TranMode', column_type='int', nullable=False, chn_name='股权转让方式')
    """股权转让方式:股权转让方式(TranMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1202，得到股权转让方式的具体描述：1-协议转让，2-协议划转，3-股权拍卖，4-以资抵债，5-二级市场买卖，6-股东重组，7-股东更名，8-大宗交易，9-要约收购，10-以股抵债，11-大宗交易(席位)，12-大宗交易(获流通权股份)，13-ETF换购，14..."""

    InvolvedSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='InvolvedSum', column_type='decimal(16,0)', nullable=False, chn_name='涉及股数(股)')
    """涉及股数(股):"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    PCTOfTansferer: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='PCTOfTansferer', column_type='decimal(19,8)', nullable=False, chn_name='占出让方原持股数比例')
    """占出让方原持股数比例:"""

    PCTOfTotalShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='PCTOfTotalShares', column_type='decimal(19,8)', nullable=False, chn_name='占总股本比例')
    """占总股本比例:"""

    DealPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='DealPrice', column_type='decimal(19,4)', nullable=False, chn_name='交易价格(元/股)')
    """交易价格(元/股):"""

    DealTurnover: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='DealTurnover', column_type='decimal(19,4)', nullable=False, chn_name='交易金额(元)')
    """交易金额(元):"""

    ValidCondition: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='ValidCondition', column_type='varchar(100)', nullable=False, chn_name='生效条件')
    """生效条件:"""

    TranStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='TranStatement', column_type='text', nullable=False, chn_name='事项描述与进展说明')
    """事项描述与进展说明:"""

    IfSuspended: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='IfSuspended', column_type='int', nullable=False, chn_name='是否终止实施')
    """是否终止实施:是否终止实施（IfSuspended），该字段固定以下常量：1-是；0-否"""

    SuspendedPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='SuspendedPublDate', column_type='datetime', nullable=False, chn_name='终止实施公告日期')
    """终止实施公告日期:"""

    IfSPBlockTradeCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='IfSPBlockTradeCode', column_type='int', nullable=False, chn_name='是否专场大宗交易代码')
    """是否专场大宗交易代码:是否专场大宗交易（IfSPBLockTradeCode），该字段固定以下常量：1-是；0-否"""

    IfSPBlockTrade: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='IfSPBlockTrade', column_type='varchar(10)', nullable=False, chn_name='是否专场大宗交易')
    """是否专场大宗交易:"""

    InitialInfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='InitialInfoPublDate', column_type='datetime', nullable=False, chn_name='首次信息发布日期')
    """首次信息发布日期:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='InfoPublDate', column_type='datetime', nullable=True, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    ContractSignDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='ContractSignDate', column_type='datetime', nullable=False, chn_name='股权转让协议签署日')
    """股权转让协议签署日:"""

    ApprovedDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='ApprovedDate', column_type='datetime', nullable=False, chn_name='转让批准日期')
    """转让批准日期:"""

    TranDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareTransfer', column_name='TranDate', column_type='datetime', nullable=False, chn_name='股权正式变动日期/过户日期')
    """股权正式变动日期/过户日期:"""

