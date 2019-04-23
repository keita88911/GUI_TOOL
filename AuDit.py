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
import  Dir
from  LoadDetails import LoadDetails
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class ChuShen():

    GetIdTaskID = getsql.sql.auto('初审')
    # print( GetIdTaskID[0][0])
    global DingDanid
    DingDanid = GetIdTaskID[0][0]
    global taskid

    taskid = GetIdTaskID[1][0]

    @classmethod
    def test_chushen_auditMaterial(self):
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        global listdata2
        listdata2 = a.excel_table_byindex("images.xlsx", 0, 0)
        # taskId=taskId1[i]
        # data = listdata1[i]['material']
        # data = json.loads(data)
        data = LoadDetails.test_loaddetails()[0]
        # print(len(data))
        global n
        for n in range(0,len(data)):
        # for n in range(0,1):
        #     n=3

            auditMaterial=LoadDetails.test_loaddetails()[0]
            # print((auditMaterial[n]['name']))
            if not str(auditMaterial[n]['name'])=="身份证复印件":
                auditMaterial[n]['enableFlag'] = "-1"
                auditMaterial[n]['remark'] = "2222"
                auditMaterial[n]['segmentCode']="audit"
                global PaparName
                global PaparCode
                PaparCode=auditMaterial[n]['code']
                PaparName=auditMaterial[n]['name']
                print("打回资料：：：    "+str(auditMaterial[n]['name']))
                para = {
        "data": {
            "ccSystemType": "",
            "otherContacts": None,
            "carAuto": "",
            "carCapacity": None,
            "carMileage": None,
            "carColor": None,
            "carAge": "一年以下",
            "carSkylight": None,
            "carConfig": None,
            "environment": "国1",
            "carDealer": "21313",
            "aaa": [8, 131],
            "vin": "123213123123",
            "regdate": "2018-06",
            "gearBox": "自动",
            "yearCheckDate": "2018-07",
            "buessCheckDate": "2018-08",
            "strongRiskDate": "2018-09",
            "sgNo": None,
            "reportNo": None,
            "appraisalTime": None,
            "carVin": None,
            "evaluationCompany": "东方航空公司",
            "rebate": None,
            "actualPay": None,
            "payerName": None,
            "loanTime": None,
            "actualFinanceCost": None,
            "address": None,
            "email": None,
            "mortgageArea": None,
            "other": None,
            "handleCardStatus": None,
            "subBankPassTime": None,
            "returnedMoneyDate": None,
            "cardBackTime": None,
            "bankBackTime": None,
            "cardNo": None,
            "transferName": "",
            "hasCarNum": "",
            "transcribeCarModel": None,
            "exCustName": None,
            "exCustIdcard": None,
            "exCustPhone": None,
            "exRelation": None,
            "carRegisterDate": "2011-10-31",
            "terminalId": None,
            "loanRemark": None,
            "indoorAuditOpinion": None,
            "exAuditOpinion": None,
            "supplementOpinion": None,
            "sendBankRemark": None,
            "custName": listdata1[0]['loanerName'],
            "custIdcard": listdata1[0]['loanerCardId'],
            "custMobile": "18555555555",
            "salesmanName": "18555555555/test",
            "custMarriage": "",
            "custNation": None,
            "custRegister": None,
            "custRegisterAddress": None,
            "systemType": "",
            "auditWay": None,
            "financeCost": 22,
            "provinceCode": None,
            "areaGroup": "",
            "carLicenseLocationProvinceCode": None,
            "riskAssessment": "",
            "carModel": "大众POLO2011款 劲取 1.6L 自动实酷版",
            "loanAmount": 60000,
            "driverLicenseFlag": "",
            "replaceBuyFlag": "",
            "assessorAmount": 1999,
            "loanYear": "",
            "loanRate": None,
            "premium": None,
            "otherCost": None,
            "gpsCost": None,
            "gpsQuantity": None,
            "payeeName": None,
            "payeePhone": None,
            "payeeBankAmount": None,
            "payeeOpenBank": None,
            "insuranceCompany": None,
            "carType": "1",
            "auditOpinion": None,
            "province": 8,
            "city": 131,
            "toPaymentPool": 0,
            "cback": False,
            "taskId": taskid,
            "completed": False,
            "push": True,
            "auditAdvanceMaterial": [{
                "code": "HVPIA",
                "name": "家访照片(室内)",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 310,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "HVPOA",
                "name": "家访照片(室外)",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 320,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "SV",
                "name": "签单视频",
                "meterialType": 3,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 340,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "QAV",
                "name": "问答视频",
                "meterialType": 3,
                "enableFlag": None,
                "remark": None,
                "existFlag": 0,
                "urlList": [],
                "serialNum": 350,
                "linkType": 1,
                "updateFlag": None,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "HV",
                "name": "家访/工作访视频",
                "meterialType": 3,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 670,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }],
            "auditMaterial": [{
                "code": "IDF",
                "name": "主贷人身份证正面",
                "meterialType": 2,
                "enableFlag": 0,
                "remark": "None",
                "existFlag": 0,
                "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDF18ca204cbcc227b20d836d55059ab6b8.jpg"],
                "serialNum": 10,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "IDB",
                "name": "主贷人身份证反面",
                "meterialType": 2,
                "enableFlag": 0,
                "remark": "None",
                "existFlag": 0,
                "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDBe423f7dfa12298159d05816a34efe81f.jpg"],
                "serialNum": 20,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "LE",
                "name": "主贷人委托查询征信书",
                "meterialType": 2,
                "enableFlag": 0,
                "remark": "None",
                "existFlag": 0,
                "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/LE58583af34c31202acc9bf3a3709bad08.jpg"],
                "serialNum": 30,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "JSZ",
                "name": "驾驶证",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 40,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "AP",
                "name": "主贷人授权书照片",
                "meterialType": 2,
                "enableFlag": 0,
                "remark": "None",
                "existFlag": 0,
                "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/AP5b9708d50f9f8d8b1b2ef0cb82785e20.jpg"],
                "serialNum": 40,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "FDBH",
                "name": "反担保函",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 50,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "IDSF",
                "name": "配偶身份证正面",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 60,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "IDSB",
                "name": "配偶身份证反面",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 70,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "LES",
                "name": "配偶委托查询征信书",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 80,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "APS",
                "name": "配偶授权书照片",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 90,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "IDGF",
                "name": "担保人身份证正面",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 110,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "IDGB",
                "name": "担保人身份证反面",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 120,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "LEG",
                "name": "担保人委托查询征信书",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 130,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "APG",
                "name": "担保人授权书照片",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 140,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "IDC",
                "name": "身份证复印件",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 170,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 0,
                "segmentCode": None
            }, {
                "code": "BSR",
                "name": "业务调查报告",
                "meterialType": 2,
                "enableFlag": 0,
                "remark": None,
                "existFlag": 0,
                "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/BSRd422e94b6a30cc970bda06bcbaffa233.jpg"],
                "serialNum": 200,
                "linkType": 1,
                "updateFlag": None,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "CCIA",
                "name": "信用卡分期业务申请书",
                "meterialType": 2,
                "enableFlag": 0,
                "remark": None,
                "existFlag": 0,
                "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/CCIA2568aedde2d9176f70857becee3f6ee4.jpg"],
                "serialNum": 210,
                "linkType": 1,
                "updateFlag": None,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "RCMVB",
                "name": "机动车登记证书(过户前)",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 370,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "BRB",
                "name": "业务承接单",
                "meterialType": 2,
                "enableFlag": 0,
                "remark": None,
                "existFlag": 0,
                "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/BRBff17a7e9398cf478f35466ac1e916358.jpg"],
                "serialNum": 400,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "BF",
                "name": "银行流水",
                "meterialType": 2,
                "enableFlag": 0,
                "remark": None,
                "existFlag": 0,
                "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/BFf78ad79a1554ddb9e931a708df498064.jpg"],
                "serialNum": 440,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }],
            "auditQualificationMaterial": [{
                "code": "CPCH",
                "name": "商品房购房合同",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 410,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "CPT",
                "name": "商品房产调",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 420,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "SBHC",
                "name": "自建房房屋证明",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 430,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "BL",
                "name": "营业执照",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 450,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "SWP",
                "name": "特殊工作工作证",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 460,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "CHPRC",
                "name": "商品房产权证",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 680,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }],
            "cityCode": None,
            "countryCode": None,
            "carLicenseLocationCityCode": None
        },
        "header": {
            "app": " ",
            "gps": " ",
            "os": " ",
            "ver": " ",
            "token": "13505b26-7d6e-4667-9e3a-b2bea06a5c7d"
        }
    }
                para['data']['auditMaterial'] = auditMaterial
                # print("原始token：：：："+para['header']['token'])
                token = weblogin.gettoken.token()
                para['header']['token']=token

        # print(data['data']['auditMaterial'][n]['enableFlag'])
        #     print("现在token：：：："+para['header']['token'])





                data=json.dumps(para)

                headers = api.API.SetHeaders()
                url4 = api.API.SetUrl()+"work/handle/audit"
                # tttt1 = json.dumps(para, encoding='UTF-8', ensure_ascii=False)
                # print(tttt1)
                response = requests.request("POST", url4, data=data, headers=headers)
                response.text1 = json.loads(response.text)
                # print(response.text)

                if response.text1['header']['msg'][0]=="操作成功":
                    print("第" + str(n + 1) + "次初审驳回成功")
                else:
                    print("第" + str(n + 1) + "次初审驳回不成功！！！")
                # print(response.text1['header']['msg'][0])
                ChuShen.adjustList()
                ChuShen.queryProblemMater()
                ChuShen.adjustMater()



    @classmethod
    def test_chushen_auditQualificationMaterial(self):
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        global listdata2
        listdata2 = a.excel_table_byindex("images.xlsx", 0, 0)
        # taskId=taskId1[i]
        # data = listdata1[i]['material']
        # data = json.loads(data)
        data = LoadDetails.test_loaddetails()[1]
        # print(len(data))
        global n
        for n in range(0,len(data)):
        # for n in range(0,1):
        #     n=3

            auditQualificationMaterial=LoadDetails.test_loaddetails()[1]
            # print((auditMaterial[n]['name']))
            if not str(auditQualificationMaterial[n]['name'])=="身份证复印件":
                auditQualificationMaterial[n]['enableFlag'] = "-1"
                auditQualificationMaterial[n]['remark'] = "2222"
                auditQualificationMaterial[n]['segmentCode'] = "audit"
                global PaparName
                global PaparCode
                PaparCode=auditQualificationMaterial[n]['code']
                PaparName=auditQualificationMaterial[n]['name']
                print("打回资料：：：    "+str(auditQualificationMaterial[n]['name']))
                para = {
        "data": {
            "ccSystemType": "",
            "otherContacts": None,
            "carAuto": "",
            "carCapacity": None,
            "carMileage": None,
            "carColor": None,
            "carAge": "一年以下",
            "carSkylight": None,
            "carConfig": None,
            "environment": "国1",
            "carDealer": "21313",
            "aaa": [8, 131],
            "vin": "123213123123",
            "regdate": "2018-06",
            "gearBox": "自动",
            "yearCheckDate": "2018-07",
            "buessCheckDate": "2018-08",
            "strongRiskDate": "2018-09",
            "sgNo": None,
            "reportNo": None,
            "appraisalTime": None,
            "carVin": None,
            "evaluationCompany": "东方航空公司",
            "rebate": None,
            "actualPay": None,
            "payerName": None,
            "loanTime": None,
            "actualFinanceCost": None,
            "address": None,
            "email": None,
            "mortgageArea": None,
            "other": None,
            "handleCardStatus": None,
            "subBankPassTime": None,
            "returnedMoneyDate": None,
            "cardBackTime": None,
            "bankBackTime": None,
            "cardNo": None,
            "transferName": "",
            "hasCarNum": "",
            "transcribeCarModel": None,
            "exCustName": None,
            "exCustIdcard": None,
            "exCustPhone": None,
            "exRelation": None,
            "carRegisterDate": "2011-10-31",
            "terminalId": None,
            "loanRemark": None,
            "indoorAuditOpinion": None,
            "exAuditOpinion": None,
            "supplementOpinion": None,
            "sendBankRemark": None,
            "custName": listdata1[0]['loanerName'],
            "custIdcard": listdata1[0]['loanerCardId'],
            "custMobile": "18555555555",
            "salesmanName": "18555555555/test",
            "custMarriage": "",
            "custNation": None,
            "custRegister": None,
            "custRegisterAddress": None,
            "systemType": "",
            "auditWay": None,
            "financeCost": 22,
            "provinceCode": None,
            "areaGroup": "",
            "carLicenseLocationProvinceCode": None,
            "riskAssessment": "",
            "carModel": "大众POLO2011款 劲取 1.6L 自动实酷版",
            "loanAmount": 60000,
            "driverLicenseFlag": "",
            "replaceBuyFlag": "",
            "assessorAmount": 1999,
            "loanYear": "",
            "loanRate": None,
            "premium": None,
            "otherCost": None,
            "gpsCost": None,
            "gpsQuantity": None,
            "payeeName": None,
            "payeePhone": None,
            "payeeBankAmount": None,
            "payeeOpenBank": None,
            "insuranceCompany": None,
            "carType": "1",
            "auditOpinion": None,
            "province": 8,
            "city": 131,
            "toPaymentPool": 0,
            "cback": False,
            "taskId": taskid,
            "completed": False,
            "push": True,
            "auditAdvanceMaterial": [{
                "code": "HVPIA",
                "name": "家访照片(室内)",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 310,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "HVPOA",
                "name": "家访照片(室外)",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 320,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "SV",
                "name": "签单视频",
                "meterialType": 3,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 340,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "QAV",
                "name": "问答视频",
                "meterialType": 3,
                "enableFlag": None,
                "remark": None,
                "existFlag": 0,
                "urlList": [],
                "serialNum": 350,
                "linkType": 1,
                "updateFlag": None,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "HV",
                "name": "家访/工作访视频",
                "meterialType": 3,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 670,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }],
            "auditMaterial": [{
                "code": "IDF",
                "name": "主贷人身份证正面",
                "meterialType": 2,
                "enableFlag": 0,
                "remark": "None",
                "existFlag": 0,
                "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDF18ca204cbcc227b20d836d55059ab6b8.jpg"],
                "serialNum": 10,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "IDB",
                "name": "主贷人身份证反面",
                "meterialType": 2,
                "enableFlag": 0,
                "remark": "None",
                "existFlag": 0,
                "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDBe423f7dfa12298159d05816a34efe81f.jpg"],
                "serialNum": 20,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "LE",
                "name": "主贷人委托查询征信书",
                "meterialType": 2,
                "enableFlag": 0,
                "remark": "None",
                "existFlag": 0,
                "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/LE58583af34c31202acc9bf3a3709bad08.jpg"],
                "serialNum": 30,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "JSZ",
                "name": "驾驶证",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 40,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "AP",
                "name": "主贷人授权书照片",
                "meterialType": 2,
                "enableFlag": 0,
                "remark": "None",
                "existFlag": 0,
                "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/AP5b9708d50f9f8d8b1b2ef0cb82785e20.jpg"],
                "serialNum": 40,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "FDBH",
                "name": "反担保函",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 50,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "IDSF",
                "name": "配偶身份证正面",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 60,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "IDSB",
                "name": "配偶身份证反面",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 70,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "LES",
                "name": "配偶委托查询征信书",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 80,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "APS",
                "name": "配偶授权书照片",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 90,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "IDGF",
                "name": "担保人身份证正面",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 110,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "IDGB",
                "name": "担保人身份证反面",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 120,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "LEG",
                "name": "担保人委托查询征信书",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 130,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "APG",
                "name": "担保人授权书照片",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 140,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "IDC",
                "name": "身份证复印件",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 170,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 0,
                "segmentCode": None
            }, {
                "code": "BSR",
                "name": "业务调查报告",
                "meterialType": 2,
                "enableFlag": 0,
                "remark": None,
                "existFlag": 0,
                "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/BSRd422e94b6a30cc970bda06bcbaffa233.jpg"],
                "serialNum": 200,
                "linkType": 1,
                "updateFlag": None,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "CCIA",
                "name": "信用卡分期业务申请书",
                "meterialType": 2,
                "enableFlag": 0,
                "remark": None,
                "existFlag": 0,
                "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/CCIA2568aedde2d9176f70857becee3f6ee4.jpg"],
                "serialNum": 210,
                "linkType": 1,
                "updateFlag": None,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "RCMVB",
                "name": "机动车登记证书(过户前)",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 370,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "BRB",
                "name": "业务承接单",
                "meterialType": 2,
                "enableFlag": 0,
                "remark": None,
                "existFlag": 0,
                "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/BRBff17a7e9398cf478f35466ac1e916358.jpg"],
                "serialNum": 400,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "BF",
                "name": "银行流水",
                "meterialType": 2,
                "enableFlag": 0,
                "remark": None,
                "existFlag": 0,
                "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/BFf78ad79a1554ddb9e931a708df498064.jpg"],
                "serialNum": 440,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 0,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }],
            "auditQualificationMaterial": [{
                "code": "CPCH",
                "name": "商品房购房合同",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 410,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "CPT",
                "name": "商品房产调",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 420,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "SBHC",
                "name": "自建房房屋证明",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 430,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "BL",
                "name": "营业执照",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 450,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "SWP",
                "name": "特殊工作工作证",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 460,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }, {
                "code": "CHPRC",
                "name": "商品房产权证",
                "meterialType": 2,
                "enableFlag": None,
                "remark": None,
                "existFlag": -1,
                "urlList": None,
                "serialNum": 680,
                "linkType": 1,
                "updateFlag": 0,
                "optionalFlag": 1,
                "urlListCode": None,
                "canPass": 1,
                "canReject": 1,
                "segmentCode": None
            }],
            "cityCode": None,
            "countryCode": None,
            "carLicenseLocationCityCode": None
        },
        "header": {
            "app": " ",
            "gps": " ",
            "os": " ",
            "ver": " ",
            "token": "13505b26-7d6e-4667-9e3a-b2bea06a5c7d"
        }
    }
                para['data']['auditQualificationMaterial'] = auditQualificationMaterial
                # print("原始token：：：："+para['header']['token'])
                token = weblogin.gettoken.token()
                para['header']['token']=token

        # print(data['data']['auditMaterial'][n]['enableFlag'])
        #     print("现在token：：：："+para['header']['token'])





                data=json.dumps(para)

                headers = api.API.SetHeaders()
                url4 = api.API.SetUrl()+"work/handle/audit"
                # tttt1 = json.dumps(para, encoding='UTF-8', ensure_ascii=False)
                # print(tttt1)
                response = requests.request("POST", url4, data=data, headers=headers)
                response.text1 = json.loads(response.text)
                # print(response.text)

                if response.text1['header']['msg'][0]=="操作成功":
                    print("第" + str(n + 1) + "次初审驳回成功")
                else:
                    print("第" + str(n + 1) + "次初审驳回不成功！！！")
                # print(response.text1['header']['msg'][0])
                ChuShen.adjustList()
                ChuShen.queryProblemMater()
                ChuShen.adjustMater()



    @classmethod
    def adjustList(self):
        # ======================================APP驳回待办验证
        global APPtoken
        global headers4
        APPtoken = applogin.gettoken.token()
        headers4 = api.API.SetHeaders()

        for pagenum in range(0,20):
            url4 = api.API.SetUrl()+"v1/app/material/adjustList"
            # print(APPtoken)
            # print(pagenum)
            data4={
                    "pageNum": pagenum,
                    "phone": "18555555555",
                    "token": APPtoken,
                    "os": "android",
                    "pageSize": 80
                }
            data4 = json.dumps(data4)

            response = requests.request("POST", url4, data=data4, headers=headers4)
            response.text1= json.loads(response.text)
            # print(headers4)
            # print(data4)
            # print(url4)
            # print("adjustList::::"+response.text)
            # print(response.text1['data']['list'][0]['lId'])

            # print(DingDanid)
            for listI in range(0,len(response.text1['data']['list'])):
                if    response.text1['data']['list'][listI]['lId']==DingDanid:

                    print("第"+str(n+1)+"次提交APP-被驳回页面存在该订单")
                    break
            break
        else:
            print("第" + str(n + 1) + "次提交APP-被驳回页面不存在该订单！！！！")


        # ====================================APP待办页面显示【被驳回】按钮








    @classmethod
    def queryProblemMater(self):
        # ====================================APP待办页面显示【被驳回】资料
        APPtoken = applogin.gettoken.token()
        headers4 = api.API.SetHeaders()
        url5 = api.API.SetUrl() + "/v1/app/material/queryProblemMater"
        # print(APPtoken)
        data5 ={
                "phone": "18555555555",
                "reqId": DingDanid,
                "token": APPtoken,
                "os": "android"
                }
        data5 = json.dumps(data5)


        response2 = requests.request("POST", url5, data=data5, headers=headers4)
        response2.text2 = json.loads(response2.text)

        # print(PaparId)
        #
        # print(response2.text)
        # print(type(PaparCode.encode('gbk')))
        # print(type(response.text2['data'][0]['code'].encode('gbk')))
        # print(PaparCode.encode('gbk'))
        # print(PaparCode+"=="+response2.text2['data'][0]['code'])
        if str(response2.text2['data'][0]['code'] )== str(PaparCode):
            print("第" + str(n + 1) + "次   "+PaparName+"   提交APP-被驳回页面存在该资料")
        else:
            print("第" + str(n + 1) + "次   "+PaparName+"   提交，APP-被驳回页面不存在该资料！！！！！！！！！！！")
        # print(response2.text)
        PaparId=response2.text2['data'][0]['id']
        PaparisImg=response2.text2['data'][0]['isImg']
        PaparisIsMust = response2.text2['data'][0]['isMust']
        PaparisIsPaper = response2.text2['data'][0]['isPaper']
        PaparisIsVideo = response2.text2['data'][0]['isVideo']

        return PaparId,PaparisImg,PaparisIsMust,PaparisIsPaper,PaparisIsVideo

                # =======================================================================APP重新上传
    @classmethod
    def adjustMater(self):
        some=ChuShen.queryProblemMater()
        id=some[0]
        isImg=some[1]
        isMust=some[2]
        isPaper=some[3]
        isVideo=some[4]
        APPtoken = applogin.gettoken.token()
        headers4 = api.API.SetHeaders()
        url6 = api.API.SetUrl() + "/v1/app/material/adjustMater"
        # print(PaparCode)
        data6 = {
                        "phone": "18555555555",
                        "reqId": DingDanid,
                        "adjustList": [{
                            "code": PaparCode,
                            "have": 1,
                            "id": id,           #   照片ID
                            "isImg": isImg,
                            "isMust": isMust,
                            "isPaper": isPaper,
                            "isVideo": isVideo,
                            "path": listdata2[n]['URL-auditMaterial'],
                            "reqId": DingDanid
                        }],
                        "token": APPtoken,
                        "os": "android"
                    }
        data6 = json.dumps(data6)

        response = requests.request("POST", url6, data=data6, headers=headers4)
        response.text3 = json.loads(response.text)
        # print(response.text)
            #
            # print()
            # print(type(PaparCode.encode('gbk')))
            # print(type(response.text2['data'][0]['code'].encode('gbk')))
            # print(PaparCode.encode('gbk'))

        if  response.text3['msg'] =="操作成功":
            print("第" + str(n + 1) + "次   " + PaparName + "   提交APP-被驳回上传成功")
        else:
            print("第" + str(n + 1) + "次   " + PaparName +"   提交，APP-被驳回上传不成功！！！")






a = ChuShen.test_chushen_auditQualificationMaterial()
b = ChuShen.test_chushen_auditMaterial()

