# -*- coding: utf-8 -*-

"""
对 Search Keyword 进行管理的页面，大致包括的功能有：
1) 提交一个 google SpreadSheet 的 url ，从里面读取 keyword 的 tag 清单
    格式为 ： 一列为一个 tag 下的 keywords , 列头为 tag

2) 提交一个 google spreadsheet 的 url ， 从里面读取 tag combination

3) 对 mongo 中的 keywords 进行一些简单的汇总查询


TODO : feature -> external env
TODO : keyword 做 rl robot
TODO : artical 突然变多了，把相关的 ts 拿出来显示
TODO : 爬虫可以做 windows app
TODO : instrinsic reward = search result diff from last time
TODO : extrinsic reward = end user consumption (click, vote) of data (chart, news article), etc
"""
