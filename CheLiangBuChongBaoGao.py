# -*- coding: UTF-8 -*-
import rdexcel
import requests
import json
import weblogin
import  MySQLdb
import getsql
import api
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
class CheLiangBuChong():
    @classmethod
    def CheLiangBuChong(self):
        token = weblogin.gettoken.token()
        taskId1 = getsql.sql.auto('车辆评估报告补充资料')[1]
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        # print(taskId1)
        Getnewcar=0
        for i in range(0,len(listdata1)):
            n = -1
            if int(listdata1[i]['newcar']) == 0:
                n=n+1
                taskId = taskId1[n]
                headers = api.API.SetHeaders()

                payload2={
    "data": {
        "custName": listdata1[i]['loanerName'],
        "custIdcard": listdata1[i]['loanerCardId'],
        "custMobile": "18555555555",
        "salesmanName": "向进/xiaojiang",
        "custMarriage": "1",
        "custNation": "汉族",
        "custRegister": "成都",
        "custRegisterAddress": None,
        "systemType": "1",
        "ccSystemType": "",
        "auditWay": "电审",
        "financeCost": 111,
        "provinceCode": 110000,
        "areaGroup": "",
        "carLicenseLocationProvinceCode": 110000,
        "riskAssessment": "1",
        "carModel": "AC Schnitzer/AC Schnitzer X6/2011款 ACS6 35i",
        "loanAmount": 160000,
        "driverLicenseFlag": "",
        "replaceBuyFlag": "",
        "assessorAmount": 18000,
        "loanYear": "3",
        "loanRate": 11,
        "premium": 1111,
        "otherCost": 111111,
        "gpsCost": 1111,
        "gpsQuantity": 11223,
        "payeeName": "测试收款人",
        "payeePhone": "11112233333",
        "payeeBankAmount": "6225881287543051",
        "payeeOpenBank": "测试开户行",
        "insuranceCompany": "1111233",
        "otherContacts": None,
        "carType": "0",
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
        "price": 0,
        "gearBox": "自动",
        "yearCheckDate": "2018-07",
        "buessCheckDate": "2018-08",
        "strongRiskDate": "2018-09",
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
        "autohomeid": None,
        "carRegisterDate": "2011-10-31",
        "terminalId": None,
        "loanRemark": None,
        "indoorAuditOpinion": "测试审核备注12312321#!@#@!!@#@!#\nASDASDASD",
        "exAuditOpinion": None,
        "auditOpinion": "请问请问无群二群翁请问请问请问请问123123123123 奥术大师大所阿萨德按时 新增操作从自行车征信",
        "supplementOpinion": "请问请问群无切请问额\n12312321312\n12312321切尔奇翁\n123123213",
        "sendBankRemark": None,
        "sgNo": "1111",
        "reportNo": "1111",
        "appraisalTime": "2018-06-03",
        "carVin": "123213123123",
        "evaluationCompany": "东方航空公司",
        "province": 8,
        "city": 131,
        "toPaymentPool": 0,
        "materFull": 1,
        "cback": True,
        "taskId": taskId,
        "completed": True,
        "push": False,
        "type": "fillAssessReport",
        "paperMeterial": None,
        "qualificationMeterial": None,
        "assessmentReportPaperMeterial": [{
            "code": "TPWPS",
            "name": "第三方网站截图",
            "meterialType": 1,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": None,
            "serialNum": 810,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 0,
            "urlListCode": None,
            "elec": False,
            "exist": True
        }],
        "assessmentReportCarRelImgMeterial": [{
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
            "elec": True,
            "exist": False
        }, {
            "code": "RCMVA",
            "name": "机动车登记证书(过户后)",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/12847/RCMVAb22ca574f26ef08e6f0c329192e9553f.jpg"],
            "serialNum": 380,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 0,
            "urlListCode": None,
            "elec": True,
            "exist": True
        }, {
            "code": "MVDLB",
            "name": "机动车行驶证(过户前)",
            "meterialType": 2,
            "enableFlag": None,
            "remark": None,
            "existFlag": -1,
            "urlList": None,
            "serialNum": 390,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 1,
            "urlListCode": None,
            "elec": True,
            "exist": False
        }, {
            "code": "MVDLA",
            "name": "机动车行驶证(过户后)",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/12847/MVDLA3874c84bd0f0c43755c33ec908325002.jpg"],
            "serialNum": 400,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 0,
            "urlListCode": None,
            "elec": True,
            "exist": True
        }, {
            "code": "LPPA",
            "name": "车牌号照片(过户后)",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/12847/LPPAc46a385868f2350d9b85b90ff95a0655.jpg"],
            "serialNum": 401,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 0,
            "urlListCode": None,
            "elec": True,
            "exist": True
        }, {
            "code": "LPPB",
            "name": "车牌号照片(过户前)",
            "meterialType": 2,
            "enableFlag": None,
            "remark": None,
            "existFlag": -1,
            "urlList": None,
            "serialNum": 402,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 1,
            "urlListCode": None,
            "elec": True,
            "exist": False
        }, {
            "code": "CFD",
            "name": "车辆正面照",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/CFD36d3538a2b9091b9b2193dba51ff70af.jpg"],
            "serialNum": 470,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 0,
            "urlListCode": None,
            "elec": True,
            "exist": True
        }, {
            "code": "COS",
            "name": "车辆斜侧面照",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/COS86cacb5e62a8142659ed5eca03fde4a0.jpg"],
            "serialNum": 480,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 0,
            "urlListCode": None,
            "elec": True,
            "exist": True
        }, {
            "code": "CB",
            "name": "车尾正面",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/CB4f5d5da1887c19ad6d7fdd4da42de890.jpg"],
            "serialNum": 490,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 0,
            "urlListCode": None,
            "elec": True,
            "exist": True
        }, {
            "code": "PMC",
            "name": "人车合影",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/PMCd6c0ba52533a23f2d39db9c272057620.jpg"],
            "serialNum": 590,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 0,
            "urlListCode": None,
            "elec": True,
            "exist": True
        }, {
            "code": "ICFAC",
            "name": "身份证与车架号合影",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/12847/ICFAC1d36b19b3681ea0a25bbbf46521b766d.jpg"],
            "serialNum": 600,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 0,
            "urlListCode": None,
            "elec": True,
            "exist": True
        }, {
            "code": "ICFACC",
            "name": "身份证与出厂牌合影",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/12847/ICFACCbbe17cc7a41c5f8e0d9bdb8403acb499.jpg"],
            "serialNum": 601,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 0,
            "urlListCode": None,
            "elec": True,
            "exist": True
        }, {
            "code": "OPI",
            "name": "里程表照片",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/OPI99b1f63f1af17af3fcf939093967fa8b.jpg"],
            "serialNum": 610,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 0,
            "urlListCode": None,
            "elec": True,
            "exist": True
        }],
        "cityCode": 110100,
        "countryCode": 110101,
        "carLicenseLocationCityCode": 110100
    },
    "header": {
        "app": " ",
        "gps": " ",
        "os": " ",
        "ver": " ",
        "token": token
    }
}
                url4 = api.API.SetUrl() + "work/handle/fillReport"
                data = json.dumps(payload2)
                response = requests.request("POST", url4, data=data, headers=headers)
                response.text1 = json.loads(response.text)
                customer = getsql.sql.GetName()[i]
                # print(response.text)
                print ("主贷人:" + customer + "  车辆评估补充资料:" + response.text1["header"]["msg"][0])
                Getnewcar = Getnewcar + 1



# a=CheLiangPingGuBaoGao.CheLiangPingGuBG()