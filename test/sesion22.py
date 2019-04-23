#!usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import sesion
import sys


default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
s=sesion.test.ZhuHangSStoken()
def cre():
    headers = {'Content-Type': "application/json", }  # 读取接口相关信息
    url =  "http://ivt4.hschefu.com:9199/v1/app/business/create"
    payload = {
        # "autohomeid": "LSVD000B111",
        "carModel": "奔驰/102",
        "coupleFlag": "0",
        "guarantorFlag": "0",
        "loanAmountType": "1",
        "custIncome": 6000,
        "autochthon": 1,
        "loanChannel": 1,
        "loanerCardId":"331021197011164002",
        # "loanerCardPath1": "erp/510104198806031672/IDF18ca204cbcc227b20d836d55059ab6b8.jpg",
        "loanerCardPath1": "erp/510104198806031672/IDF8b0b03d09752570ff081ef83e4b77b74.jpg",
        "loanerCardPath2": "erp/510104198806031672/IDB0e6d054322edebfe284a83557bb3f9ff.jpg",
        "loanerCreditPath": "erp/510104198806031672/LE08b40c32383f94cf3de8d1ddec5da2c7.jpg ",
        "loanerName": "测试",
        "loanerPhone": "18585874587",
        "loanerSignPath": "erp/510104198806031672/AP3bafec670d5497b6a3dcda539f9abafe.jpg",
        "os": "android",
        "phone": "18583287560",
        "newcar": "0",
        "token": ""}
    para1 = json.dumps(payload)
    r = s.post(url, data=para1, headers=headers)
    print(r.text)
a=cre()