# _*_encoding:utf-8 _*_
# author:fq

import re
import json
from urllib import request
from stockdata.database import sqlite

class Stock:
    """股票类"""
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def __str__(self):
        return "名称：" + self.name +"股票代码：" + self.code


def db_store(mysqlite,info):
    try:
        #stock = Stock(info["name"], info["code"])
        name = info["name"]
        code = info["code"]
        data = info["data"]
        date = ""
        open_value = ""
        close_value = ""
        high_value = ""
        low_value = ""
        change_value = ""
        deal_volume = ""
        deal_value = ""
        amplitude = ""
        exchange = ""
        prev_close = 1.0
        for day_data in data:
            ret = day_data.split(',')
            date = ret[0]
            open_value = ret[1]
            close_value = ret[2]
            high_value = ret[3]
            low_value = ret[4]
            deal_volume = ret[5]
            deal_value = ret[6]
            amplitude = ret[7]
            exchange = ret[8]
            if prev_close:
                change_value = "%1.2f" % (((float(close_value) - prev_close) / prev_close) * 100)
            else:
                change_value = "NAN"
            prev_close = float(close_value)
            sql_str = "INSERT INTO stockdata (name,code,datadate,open_value,close_value,high_value,low_value,change_value,deal_volume,deal_value,amplitude,exchange)\
                VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name,code,date,open_value,close_value,high_value,low_value,change_value,deal_volume,deal_value,amplitude,exchange)
            mysqlite.Execute(sql_str)
    except Exception as e:
        print(str(e))
if __name__ == "__main__":
    p1 = re.compile(r'[(](.*)[)]',re.S)
    response = request.urlopen("http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js?rtntype=5&token=4f1862fc3b5e77c150a2b985b12db0fd&cb=jQuery183036043298931397505_1533125389853&id=0021952&type=k&authorityType=fa&_=1533125420524")
    all_info = response.read().decode("utf-8")
    info = re.findall(p1, all_info)[0]
    info = json.loads(info)
    mysqlite = sqlite("E:\Develop\qz\stockdata\stockdata.sqlite")
    db_store(mysqlite, info)
    mysqlite.Close()


