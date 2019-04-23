# -*- coding: UTF-8 -*-
import rdexcel
import requests
import json
import weblogin
import MySQLdb
import getsql
import api
import sys
import applogin
import unittest
import Dir


default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class LoadDetails():

    @classmethod
    def test_loaddetails(self, datail=None):
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        taskId1 = getsql.sql.auto('初审')[1]
        taskid=taskId1[0]
        # print(taskid)
        token = weblogin.gettoken.token()
        data = {
            "data": {
                "moduleCode": "audit",
                "taskId": taskid,
            },
            "header": {
                "app": " ",
                "gps": " ",
                "os": " ",
                "ver": " ",
                "token": token
            }
        }

        data = json.dumps(data)
        # print(data)
        # print(type(data))
        headers = api.API.SetHeaders()
        url4 = api.API.SetUrl() + "work/queryLoadDetails"
        response = requests.request("POST", url4, data=data, headers=headers)
        response.text1 = json.loads(response.text)
        # print(response.text)
        auditMaterial = response.text1['data']['auditMaterial']
        # """""""""
        #  *初审-审核资料
        # """""""""
        auditQualificationMaterial=response.text1['data']['auditQualificationMaterial']
        # """""""""
        # *初审-资质资料
        # """""""""

        auditAdvanceMaterial=response.text1['data']['auditAdvanceMaterial']

        # detail = response.headers
        # print(auditMaterial)
        # print(auditQualificationMaterial)
        # print(type(response.text))
        # print(response.text)
        # print(type(json.dumps(t['data']['auditMaterial'][1]['name'])))
        # print len(t)
        # print(t['data']['auditMaterial'][0]['enableFlag'])
        return auditMaterial,auditQualificationMaterial,auditAdvanceMaterial


# a = LoadDetails.test_loaddetails()
