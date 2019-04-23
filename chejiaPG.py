#!usr/bin/python
# -*- coding: utf-8 -*-
import applogin
import rdexcel
import requests
import json
import applogin
import sys
import getsql
import api
import weblogin

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class CheJiaPingGu():
    @classmethod
    def chejiaPG(self):
        return True
        # a = rdexcel.readexcel()
        # listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        # token = weblogin.gettoken.token()
        # taskId1 = getsql.sql.GetCheJiaPingGuID()[1]
        # for i in range(0, len(listdata1)):
        #     # print("1")
        #     taskId = taskId1[i]
        #     headers = api.API.SetHeaders()
        #     payload1 = {
        #         "data": {
        #             "moduleCode": "evaluateCar",
        #             "taskId": taskId
        #         },
        #         "ext": "string",
        #         "header": {
        #             "app": "string",
        #             "gps": "string",
        #             "os": "string",
        #             "token": token,
        #             "ver": "string"
        #         }
        #     }
        #     url3 = api.API.SetUrl() + "work/receiveTask"
        #     data = json.dumps(payload1)
        #     response = requests.request("POST", url3, data=data, headers=headers)
        #
        #     response.text1 = json.loads(response.text)
        #     customer = getsql.sql.GetName()[i]
        #     # print (taskId)
        #     print ("主贷人:" + customer + "  车价评估领取:" + response.text1["header"]["msg"][0])
        #
        #     url1 = api.API.SetUrl() + "work/handle/evaluateCar"
        #     newcar = int(listdata1[i]['newcar'])
        #
        #     # print(newcar)
        #     # print(type(newcar))
        #     if newcar == 1:
        #         # print("新车")
        #         payload1 = {
        #             "data": {
        #                 "custName": listdata1[i]['loanerName'],
        #                 "custIdcard": listdata1[i]['loanerCardId'],
        #                 "custMobile": "18583266667",
        #                 "salesmanName": "向进/王刚",
        #                 "custMarriage": "",
        #                 "custNation": None,
        #                 "custRegister": None,
        #                 "systemType": "",
        #                 "ccSystemType": "",
        #                 "auditWay": None,
        #                 "financeCost": None,
        #                 "provinceCode": None,
        #                 "areaGroup": "",
        #                 "carLicenseLocationProvinceCode": None,
        #                 "riskAssessment": "",
        #
        #                 "gearBox": "自动",
        #                 "loanAmount": None,
        #                 "driverLicenseFlag": "",
        #                 "replaceBuyFlag": "",
        #                 "assessorAmount": "1999",
        #                 "loanYear": "",
        #                 "loanRate": None,
        #                 "premium": None,
        #                 "otherCost": None,
        #                 "gpsCost": None,
        #                 "gpsQuantity": None,
        #                 "payeeName": None,
        #                 "payeePhone": None,
        #                 "payeeBankAmount": None,
        #                 "payeeOpenBank": None,
        #                 "insuranceCompany": None,
        #                 "otherContacts": None,
        #                 "carType": listdata1[i]['newcar'],
        #                 "carAuto": "1",
        #                 # "autohomeid":"AC0A00HB111",
        #                 "pgPrice": "0",
        #                 "province": "8",
        #                 "b": "大众",
        #                 "buessCheckDate": "2018-08",
        #                 "carAge": "一年以下",
        #                 "carCapacity": "111",
        #                 "carMileage": "222",
        #                 "carColor": "红色",
        #                 "carSkylight": "有天窗",
        #                 "carConfig": "配置1123",
        #                 "carRegisterDate": "2018-05-27",
        #                 "city": "131",
        #                 "d": "2011款 劲取 1.6L 自动实酷版",
        #                 "environment": "国1",
        #                 "carDealer": "21313",
        #                 "carModel": "大众POLO2011款 劲取 1.6L 自动实酷版",
        #                 "regdate": "2018-06",
        #                 "strongRiskDate": "2018-09",
        #                 "vin": "LFMBE20D470105978",
        #                 "yearCheckDate": "2018-07",
        #                 "sgNo": None,
        #                 "reportNo": None,
        #                 "appraisalTime": None,
        #                 "carVin": None,
        #                 "rebate": None,
        #                 "actualPay": None,
        #                 "payerName": None,
        #                 "loanTime": None,
        #                 "address": None,
        #                 "email": None,
        #                 "mortgageArea": None,
        #                 "other": None,
        #                 "handleCardStatus": None,
        #                 "subBankPassTime": None,
        #                 "returnedMoneyDate": None,
        #                 "cardBackTime": None,
        #                 "bankBackTime": None,
        #                 "cardNo": None,
        #                 "transferName": "",
        #                 "hasCarNum": "",
        #                 "m": "POLO",
        #                 "transcribeCarModel": None,
        #                 "exCustName": None,
        #                 "exCustIdcard": None,
        #                 "exCustPhone": None,
        #                 "exRelation": None,
        #                 "loanRemark": None,
        #                 "indoorAuditOpinion": None,
        #                 "exAuditOpinion": None,
        #                 "auditOpinion": None,
        #                 "supplementOpinion": None,
        #                 "sendBankRemark": None,
        #                 "taskId": taskId,
        #                 "completed": "true",
        #                 "push": "false",
        #                 "evaluateCarMaterial": [{
        #                     "code": "RCMVB",
        #                     "name": "机动车登记证书(过户前)",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/RCMVB59ce9ca98d795f7cd8a6383dedde0aad.jpg"],
        #                     "serialNum": 370,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "MVDLB",
        #                     "name": "机动车行驶证(过户前)",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/MVDLBebe298e5889b77edc3e913c9c53ba304.jpg"],
        #                     "serialNum": 390,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "BF",
        #                     "name": "银行流水",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg"],
        #                     "serialNum": 440,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "CFD",
        #                     "name": "车辆正面照",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CFDc7e652ef1ffa4692a8a085a789c4560a.jpg"],
        #                     "serialNum": 470,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "CB",
        #                     "name": "车尾正面",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CBf14cc0a7ca956de9e68b3d77d4e83b51.jpg"],
        #                     "serialNum": 490,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "FSC",
        #                     "name": "车头45度",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/FSC43ce4372703d441c74591b56efc55f63.jpg"],
        #                     "serialNum": 500,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "CR",
        #                     "name": "车顶",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CR9934393f738715ee6585f0c10d246ff4.jpg"],
        #                     "serialNum": 510,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "CFR",
        #                     "name": "车前排",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CFR3f89b8c7e2bf8a51a6a6a7d99b87b749.jpg"],
        #                     "serialNum": 530,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "CBR",
        #                     "name": "车后排",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CBRfcb685b63d92a6d7b4896cb1394a31dc.jpg"],
        #                     "serialNum": 540,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "CN",
        #                     "name": "铭牌",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CN25c4830498bbaa93a5727c4609a72709.jpg"],
        #                     "serialNum": 550,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "ECI",
        #                     "name": "发动机机舱照",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/ECIff4445d1faaa9dc51808f777bbabc79b.jpg"],
        #                     "serialNum": 560,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "OPI",
        #                     "name": "里程表照片",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/OPI84362c9993bfdf505dc35165fd43b5ed.jpg"],
        #                     "serialNum": 610,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "MCI",
        #                     "name": "中控仪表",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/MCI37ed0ab19cca8e6f09184486b2342665.jpg"],
        #                     "serialNum": 760,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "SW",
        #                     "name": "方向盘",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/SWe7e02e2017c6e74d107045fcd0d65206.jpg"],
        #                     "serialNum": 770,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "MSSS",
        #                     "name": "主驾座椅侧面",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/MSSSc7761771b1d8266ae35833ab8b72522a.jpg"],
        #                     "serialNum": 780,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "VSSS",
        #                     "name": "副驾座椅侧面",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/VSSS053614bcaff57a137d1b2365bd28b32b.jpg"],
        #                     "serialNum": 790,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "SP",
        #                     "name": "档杆照片",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/SPafc7d45aad4a7b0248950a6cb526619c.jpg"],
        #                     "serialNum": 800,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "BRB",
        #                     "name": "业务承接单",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3908/BRB9513d4c0d33be63d3273b493a8b24632.jpg"],
        #                     "serialNum": 820,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }],
        #                 "cityCode": None,
        #                 "countryCode": None,
        #                 "carLicenseLocationCityCode": None,
        #                 "carLicenseLocationCountryCode": None
        #             },
        #             "header": {
        #                 "app": " ",
        #                 "gps": " ",
        #                 "os": " ",
        #                 "ver": " ",
        #                 "token": token
        #             }
        #         }
        #     else:
        #         # print("二手车")
        #         payload1 = {
        #             "data": {
        #
        #                 "carModel": "阿尔法罗密欧Gtv-3.0-MT",
        #                 "custName": listdata1[i]['loanerName'],
        #                 "custIdcard": listdata1[i]['loanerCardId'],
        #                 "custMobile": "18583266667",
        #                 "salesmanName": "向进/王刚",
        #                 "custMarriage": "",
        #                 "custNation": None,
        #                 "custRegister": None,
        #                 "systemType": "",
        #                 "ccSystemType": "",
        #                 "auditWay": None,
        #                 "financeCost": None,
        #                 "provinceCode": None,
        #                 "areaGroup": "",
        #                 "carLicenseLocationProvinceCode": None,
        #                 "riskAssessment": "",
        #
        #                 "gearBox": "自动",
        #                 "loanAmount": None,
        #                 "driverLicenseFlag": "",
        #                 "replaceBuyFlag": "",
        #                 "assessorAmount": "1999",
        #                 "loanYear": "",
        #                 "loanRate": None,
        #                 "premium": None,
        #                 "otherCost": None,
        #                 "gpsCost": None,
        #                 "gpsQuantity": None,
        #                 "payeeName": None,
        #                 "payeePhone": None,
        #                 "payeeBankAmount": None,
        #                 "payeeOpenBank": None,
        #                 "insuranceCompany": None,
        #                 "otherContacts": None,
        #                 "carType": listdata1[i]['newcar'],
        #                 "carAuto": "1",
        #                 # "autohomeid": "157907",
        #                 "pgPrice": "0",
        #                 "province": "8",
        #
        #                 "buessCheckDate": "2018-08",
        #                 "carAge": "一年以下",
        #                 "carCapacity": "111",
        #                 "carMileage": "222",
        #                 "carColor": "红色",
        #                 "carSkylight": "有天窗",
        #                 "carConfig": "配置1123",
        #                 "carRegisterDate": "2018-05-27",
        #                 "city": "131",
        #
        #                 "environment": "国1",
        #                 "carDealer": "21313",
        #                 "carModel": "大众POLO2011款 劲取 1.6L 自动实酷版",
        #                 "regdate": "2018-06",
        #                 "strongRiskDate": "2018-09",
        #                 "vin": "LFMBE20D470105978",
        #                 "yearCheckDate": "2018-07",
        #                 "sgNo": None,
        #                 "reportNo": None,
        #                 "appraisalTime": None,
        #                 "carVin": None,
        #                 "rebate": None,
        #                 "actualPay": None,
        #                 "payerName": None,
        #                 "loanTime": None,
        #                 "address": None,
        #                 "email": None,
        #                 "mortgageArea": None,
        #                 "other": None,
        #                 "handleCardStatus": None,
        #                 "subBankPassTime": None,
        #                 "returnedMoneyDate": None,
        #                 "cardBackTime": None,
        #                 "bankBackTime": None,
        #                 "cardNo": None,
        #                 "transferName": "",
        #                 "hasCarNum": "",
        #                 "m": "POLO",
        #                 "transcribeCarModel": None,
        #                 "exCustName": None,
        #                 "exCustIdcard": None,
        #                 "exCustPhone": None,
        #                 "exRelation": None,
        #                 "loanRemark": None,
        #                 "indoorAuditOpinion": None,
        #                 "exAuditOpinion": None,
        #                 "auditOpinion": None,
        #                 "supplementOpinion": None,
        #                 "sendBankRemark": None,
        #                 "taskId": taskId,
        #                 "completed": "true",
        #                 "push": "false",
        #                 "evaluateCarMaterial": [{
        #                     "code": "RCMVB",
        #                     "name": "机动车登记证书(过户前)",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/RCMVB59ce9ca98d795f7cd8a6383dedde0aad.jpg"],
        #                     "serialNum": 370,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "MVDLB",
        #                     "name": "机动车行驶证(过户前)",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/MVDLBebe298e5889b77edc3e913c9c53ba304.jpg"],
        #                     "serialNum": 390,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "BF",
        #                     "name": "银行流水",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg"],
        #                     "serialNum": 440,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "CFD",
        #                     "name": "车辆正面照",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CFDc7e652ef1ffa4692a8a085a789c4560a.jpg"],
        #                     "serialNum": 470,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "CB",
        #                     "name": "车尾正面",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CBf14cc0a7ca956de9e68b3d77d4e83b51.jpg"],
        #                     "serialNum": 490,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "FSC",
        #                     "name": "车头45度",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/FSC43ce4372703d441c74591b56efc55f63.jpg"],
        #                     "serialNum": 500,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "CR",
        #                     "name": "车顶",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CR9934393f738715ee6585f0c10d246ff4.jpg"],
        #                     "serialNum": 510,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "CFR",
        #                     "name": "车前排",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CFR3f89b8c7e2bf8a51a6a6a7d99b87b749.jpg"],
        #                     "serialNum": 530,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "CBR",
        #                     "name": "车后排",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CBRfcb685b63d92a6d7b4896cb1394a31dc.jpg"],
        #                     "serialNum": 540,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "CN",
        #                     "name": "铭牌",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CN25c4830498bbaa93a5727c4609a72709.jpg"],
        #                     "serialNum": 550,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "ECI",
        #                     "name": "发动机机舱照",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/ECIff4445d1faaa9dc51808f777bbabc79b.jpg"],
        #                     "serialNum": 560,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "OPI",
        #                     "name": "里程表照片",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/OPI84362c9993bfdf505dc35165fd43b5ed.jpg"],
        #                     "serialNum": 610,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "MCI",
        #                     "name": "中控仪表",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/MCI37ed0ab19cca8e6f09184486b2342665.jpg"],
        #                     "serialNum": 760,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "SW",
        #                     "name": "方向盘",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/SWe7e02e2017c6e74d107045fcd0d65206.jpg"],
        #                     "serialNum": 770,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "MSSS",
        #                     "name": "主驾座椅侧面",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/MSSSc7761771b1d8266ae35833ab8b72522a.jpg"],
        #                     "serialNum": 780,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "VSSS",
        #                     "name": "副驾座椅侧面",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/VSSS053614bcaff57a137d1b2365bd28b32b.jpg"],
        #                     "serialNum": 790,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "SP",
        #                     "name": "档杆照片",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/SPafc7d45aad4a7b0248950a6cb526619c.jpg"],
        #                     "serialNum": 800,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }, {
        #                     "code": "BRB",
        #                     "name": "业务承接单",
        #                     "meterialType": 2,
        #                     "enableFlag": 0,
        #                     "remark": None,
        #                     "existFlag": 0,
        #                     "urlList": [
        #                         "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3908/BRB9513d4c0d33be63d3273b493a8b24632.jpg"],
        #                     "serialNum": 820,
        #                     "linkType": 1,
        #                     "updateFlag": None,
        #                     "optionalFlag": 0,
        #                     "urlListCode": None
        #                 }],
        #                 "cityCode": None,
        #                 "countryCode": None,
        #                 "carLicenseLocationCityCode": None,
        #                 "carLicenseLocationCountryCode": None
        #             },
        #             "header": {
        #                 "app": " ",
        #                 "gps": " ",
        #                 "os": " ",
        #                 "ver": " ",
        #                 "token": token
        #             }
        #         }
        #
        #     data = json.dumps(payload1)
        #     response1 = requests.request("POST", url=url1, data=data, headers=headers)
        #     # r = requests.post(url,data=payload,headers= headers)
        #     response.text2 = json.loads(response1.text)
        #     customer = getsql.sql.GetName()[i]
        #
        #     print ("主贷人:" + customer + "  车价评估审核:" + response.text2["header"]["msg"][0])
# a=CheJiaPingGu
# a.chejiaPG()
