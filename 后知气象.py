# -*- coding: UTF-8 -*-
import requests

__author__ = 'zy'
__time__ = '2020/2/17 19:54'

# 导入所需模块
import urllib.error
import urllib.request
import urllib.parse
import re
import rsa
import http.cookiejar  # 从前的cookielib
import base64
import json
import urllib
import binascii
import pymongo,re
import logging
import logging.config
import time
def trans(timeStamp):

    timeStamp = int(timeStamp)
    timeStamp = float(timeStamp / 1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

def get_area(url,areacode):
    mongo_client = pymongo.MongoClient(host='127.0.0.1', port=27017)
    db = mongo_client.paper  # 指定数据库
    connection = db.nweather  # 指定数据集

    response = requests.get(url,allow_redirects=False)
    if response.status_code == 200:
        # try:
            resp = json.loads(response.text)
            day=['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16', 's17', 's18', 's19', 's20', 's21', 's22', 's23', 's24', 's25', 's26', 's27', 's28', 's29', 's30', 's31']
            print(resp)

            for i in day:
                if i in resp['data']:
                    items={}
                    try:
                        items['aqi']=resp['data'][i]['aqi']
                    except:
                        items['aqi'] =''

                    try:
                        items['avgTmp']=resp['data'][i]['avgTmp']
                    except:
                        items['avgTmp'] =''

                    try:
                        items['cloudAmount']=resp['data'][i]['cloudAmount']
                    except:
                        items['cloudAmount'] =''

                    try:
                        items['dataTime']=trans(resp['data'][i]['dataTime'])
                    except:
                        items['dataTime'] =''

                    try:
                        items['humi']=resp['data'][i]['humi']
                    except:
                        items['humi'] =''

                    try:
                        items['level']=resp['data'][i]['level']
                    except:
                        items['level'] =''

                    try:
                        items['mainPol']=resp['data'][i]['mainPol']
                    except:
                        items['mainPol'] =''

                    try:
                        items['rainfall']=resp['data'][i]['rainfall']
                    except:
                        items['rainfall'] =''

                    try:
                        items['vis']=resp['data'][i]['vis']
                    except:
                        items['vis'] =''

                    try:
                        items['windLevel']=resp['data'][i]['windLevel']
                    except:
                        items['windLevel'] =''

                    try:
                        items['windSpeed']=resp['data'][i]['windSpeed']
                    except:
                        items['windSpeed'] =''

                    items['city']=areacode

                    connection.insert_one(dict(items))
        # except:
        #     print('error')
if __name__ == '__main__':
    url = 'http://hz.zc12369.com/api/index/calendar/{date}/{code}'
    #http://hz.zc12369.com/api/index/calendar/2020-01/411100
    keyword_list = ['广州', '深圳',
                    '珠海'
        , '汕头'
        , '佛山'
        , '韶关'
        , '河源'
        , '梅州'
        , '惠州'
        , '汕尾'
        , '东莞'
        , '中山'
        , '江门'
        , '阳江'
        , '湛江'
        , '茂名'
        , '肇庆'
        , '清远'
        , '潮州'
        , '揭阳'
        , '云浮'
    ]

    # ['广州', '411700'],
    # ['深圳', '440300'],
    # ['珠海', '440400'],
    # ['汕头', '440500'],
    # ['佛山', '440600'],
    # ['韶关', '440200'],
    # ['河源', '441600'],
    # ['梅州', '441400'],
    # ['惠州', '441300'],
    # ['汕尾', '441500'],
    # ['东莞', '441900'],
    # ['中山', '442000'],
    # ['江门', '440700'],
    # ['阳江', '441700'],
    # ['湛江', '440800'],
    # ['茂名', '440900'],

    area_list=[
['肇庆','441200'],
['清远','441800'],
['潮州','445100'],
['揭阳','445200'],
['云浮','445300'],
]
    keyword_list = [440100]
    startTime_list = ['2009-01', '2009-02', '2009-03', '2009-04', '2009-05', '2009-06', '2009-07', '2009-08', '2009-09',
                      '2009-10', '2009-11', '2009-12', '2010-01', '2010-02', '2010-03', '2010-04', '2010-05', '2010-06',
                      '2010-07', '2010-08', '2010-09', '2010-10', '2010-11', '2010-12', '2011-01', '2011-02', '2011-03',
                      '2011-04', '2011-05', '2011-06', '2011-07', '2011-08', '2011-09', '2011-10', '2011-11', '2011-12',
                      '2012-01', '2012-02', '2012-03', '2012-04', '2012-05', '2012-06', '2012-07', '2012-08', '2012-09',
                      '2012-10', '2012-11', '2012-12', '2013-01', '2013-02', '2013-03', '2013-04', '2013-05', '2013-06',
                      '2013-07', '2013-08', '2013-09', '2013-10', '2013-11', '2013-12', '2014-01', '2014-02', '2014-03',
                      '2014-04', '2014-05', '2014-06', '2014-07', '2014-08', '2014-09', '2014-10', '2014-11', '2014-12',
                      '2015-01', '2015-02', '2015-03', '2015-04', '2015-05', '2015-06', '2015-07', '2015-08', '2015-09',
                      '2015-10', '2015-11', '2015-12', '2016-01', '2016-02', '2016-03', '2016-04', '2016-05', '2016-06',
                      '2016-07', '2016-08', '2016-09', '2016-10', '2016-11', '2016-12', '2017-01', '2017-02', '2017-03',
                      '2017-04', '2017-05', '2017-06', '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12',
                      '2018-01', '2018-02', '2018-03', '2018-04', '2018-05', '2018-06', '2018-07', '2018-08', '2018-09',
                      '2018-10', '2018-11', '2018-12', '2019-01', '2019-02', '2019-03', '2019-04', '2019-05', '2019-06',
                      '2019-07', '2019-08', '2019-09', '2019-10', '2019-11', '2019-12']

    # get_area('http://hz.zc12369.com/api/index/calendar/2020-01/411100','q')
    for i in area_list:
        time.sleep(1)
        for j in startTime_list:
            time.sleep(0.1)
            trl=url.format(date=str(j),code=str(i[1]))
            print(trl)
            get_area(trl,i[0])
# for i in keyword_list:
#     for j in startTime_list:
#         trl=url.format(date=str(j),code=str(i))
#         print(trl)
#
#         try:
#             cd = CollectData(keyword=i, area=j, startTime=j, interval=interval, fileS=fileS)
#             url = cd.getURL()
#             cd.download(url)
#             logger.info("抓取成功")
#             logger.info(i)
#             logger.info(j)
#         except:
#             logger.info("抓取失败")
#             logger.info(i)
#             logger.info(j)