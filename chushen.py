# -*- coding: UTF-8 -*-
import rdexcel
import requests
import json
import weblogin
import MySQLdb
import getsql
import api
import sys
import Province

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class ChuShen():

    @classmethod
    def chushen(self):
        token = weblogin.gettoken.token()
        taskId1 = getsql.sql.ChuShenID()[1]
        id1 = getsql.sql.ChuShenID()[0]
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        # print(taskId1)

        for i in range(0, len(taskId1)):
            taskId = taskId1[i]
            id=id1[i]
            headers = api.API.SetHeaders()
            payload1 = {
                "data": {
                    "moduleCode": "audit",
                    "taskId": taskId
                },
                "ext": "string",
                "header": {
                    "app": "string",
                    "gps": "string",
                    "os": "string",
                    "token": token,
                    "ver": "string"
                }
            }
            url3 = api.API.SetUrl() + "work/receiveTask"
            data = json.dumps(payload1)
            response = requests.request("POST", url3, data=data, headers=headers)
            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            print ("主贷人:" + customer + "  初审领取:" + response.text1["header"]["msg"][0])

            payload3 = {
                "data": {
                    "type": "2",
                    "cardNo": "230500197807017375",
                    "name": "王大",
                    "phone": "18588888888",
                    "relation": "0",
                    "memo": "123",
                    "customerIdcard": listdata1[i]['loanerCardId'],
                    "reqId": id
                },
                "header": {
                    "app": " ",
                    "gps": " ",
                    "os": " ",
                    "ver": " ",
                    "token": token
                }
            }
            url5 = api.API.SetUrl() + "contact/add"
            # print(url5)
            # print(id)
            # print(payload3)
            data2 = json.dumps(payload3)
            response = requests.request("POST", url5, data=data2, headers=headers)
            # print(response.text)
            payload2 = {
                "data": {
                    "lowLoan":"0",
                    "isSeparate": "1",
                    "firstPayment": 95200,
                    "custName": listdata1[i]['loanerName'],
                    "custIdcard": listdata1[i]['loanerCardId'],
                    "custMobile": listdata1[i]['mobile'],
                    "salesmanName": "向进/黄涛",
                    "custCompany": "成都工作单位",
                    "custMarriage": "1",
                    "custNation": "汉族",
                    "custCompany": "测试公司",
                    "custRegister": "成都",
                    "carAge": "一年以下",
                    "systemType": "1",
                    "ccSystemType": "",
                    "auditWay": "电审",
                    "financeCost": "111",
                    "provinceCode": 510000,
                    "areaGroup": "1",
                    "carLicenseLocationProvinceCode": 110000,
                    "riskAssessment": "1",
                    # "autohomeid":"LSVD000B111",
                    "carModel": "AC Schnitzer/AC Schnitzer X6/2011款 ACS6 35i",
                    "loanAmount": listdata1[i]['loanAmount'],

                    "replaceBuyFlag": "",
                    "assessorAmount": 1999,
                    "loanYear": "3",
                    "loanRate": "27",
                    "driverLicenseFlag": "1",
                    "premium": "1111",
                    "otherCost": "111111",
                    "gpsCost": "1111",
                    "gpsQuantity": "11223",
                    "payeeName": "重庆市野峰汽车销售有限公司",
                    "payeePhone": "18583287565",
                    "regdate": "2018-06",
                    "payeeBankAmount": "2222222",
                    "payeeOpenBank": "111112",
                    "insuranceCompany": "1111233",
                    "otherContacts": None,
                    "carType": listdata1[i]['newcar'],
                    "carAuto": "",
                    "carCapacity": None,
                    "carMileage": None,
                    "carColor": None,
                    "carSkylight": None,
                    "carConfig": None,
                    "carRegisterDate": None,
                    "sgNo": None,
                    "reportNo": None,
                    "appraisalTime": None,
                    "carVin": None,
                    "rebate": None,
                    "actualPay": None,
                    "payerName": None,
                    "loanTime": None,
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
                    "loanRemark": None,
                    "indoorAuditOpinion": None,
                    "exAuditOpinion": None,
                    "auditOpinion": "请问请问无群二群翁请问请问请问请问123123123123 奥术大师大所阿萨德按时 新增操作从自行车征信 ",
                    "supplementOpinion": None,
                    "sendBankRemark": None,
                    "taskId": taskId,
                    "completed": "true",
                    "push": "false",
                    "auditAdvanceMaterial": [{
                        "code": "HVPIA",
                        "name": "家访照片(室内)",
                        "meterialType": 2,
                        "enableFlag": 0,
                        "remark": None,
                        "existFlag": 0,
                        "urlList": [
                            "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/HVPIA48d8731769e8c2548a0390435ac32ed7.jpg",
                            "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/HVPIAd5a53a595c6c4c623b83a7aac4e985fe.jpg"
                        ],
                        "serialNum": 310,
                        "linkType": 1,
                        "updateFlag": None,
                        "optionalFlag": 0,
                        "urlListCode": None
                    },
                        {
                            "code": "HVPOA",
                            "name": "家访照片(室外)",
                            "meterialType": 2,
                            "enableFlag": 0,
                            "remark": None,
                            "existFlag": 0,
                            "urlList": [
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/HVPOA83e8b927b5397966982e7227c3b1346a.jpg",
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/HVPOAa24c0305bef9e2a2a52f2f9ecb0e3a8b.jpg"
                            ],
                            "serialNum": 320,
                            "linkType": 1,
                            "updateFlag": None,
                            "optionalFlag": 0,
                            "urlListCode": None
                        },
                        {
                            "code": "ALOA",
                            "name": "授权委托书",
                            "meterialType": 2,
                            "enableFlag": 0,
                            "remark": None,
                            "existFlag": 0,
                            "urlList": [
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/ALOA830fdb11303f89d125b1c2d6b0d01a88.jpg"
                            ],
                            "serialNum": 330,
                            "linkType": 1,
                            "updateFlag": None,
                            "optionalFlag": 0,
                            "urlListCode": None
                        },
                        {
                            "code": "SV",
                            "name": "签单视频",
                            "meterialType": 3,
                            "enableFlag": 0,
                            "remark": None,
                            "existFlag": 0,
                            "urlList": None,
                            "serialNum": 340,
                            "linkType": 1,
                            "updateFlag": None,
                            "optionalFlag": 0,
                            "urlListCode": None
                        },
                        {
                            "code": "PPA",
                            "name": "保单照片",
                            "meterialType": 2,
                            "enableFlag": None,
                            "remark": None,
                            "existFlag": -1,
                            "urlList": None,
                            "serialNum": 360,
                            "linkType": 1,
                            "updateFlag": 0,
                            "optionalFlag": 0,
                            "urlListCode": None
                        },
                        {
                            "code": "HV",
                            "name": "家访视频",
                            "meterialType": 3,
                            "enableFlag": 0,
                            "remark": None,
                            "existFlag": 0,
                            "urlList": None,
                            "serialNum": 670,
                            "linkType": 1,
                            "updateFlag": None,
                            "optionalFlag": 0,
                            "urlListCode": None
                        }
                    ],
                    "auditMaterial": [{
                        "code": "IDF",
                        "name": "主贷人身份证正面",
                        "meterialType": 2,
                        "enableFlag": 0,
                        "remark": "None",
                        "existFlag": 0,
                        "urlList": [
                            "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDF18ca204cbcc227b20d836d55059ab6b8.jpg"
                        ],
                        "serialNum": 10,
                        "linkType": 1,
                        "updateFlag": 0,
                        "optionalFlag": 0,
                        "urlListCode": None
                    },
                        {
                            "code": "IDB",
                            "name": "主贷人身份证反面",
                            "meterialType": 2,
                            "enableFlag": 0,
                            "remark": "None",
                            "existFlag": 0,
                            "urlList": [
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDBe423f7dfa12298159d05816a34efe81f.jpg"
                            ],
                            "serialNum": 20,
                            "linkType": 1,
                            "updateFlag": 0,
                            "optionalFlag": 0,
                            "urlListCode": None
                        },
                        {
                            "code": "CCF",
                            "name": "信用卡申请表",
                            "meterialType": 2,
                            "enableFlag": 0,
                            "remark": None,
                            "existFlag": 0,
                            "urlList": [
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CCF956b25520a2c313d09662d0c5e1c4b9f.jpg"
                            ],
                            "serialNum": 160,
                            "linkType": 1,
                            "updateFlag": None,
                            "optionalFlag": 0,
                            "urlListCode": None
                        },
                        {
                            "code": "IDC",
                            "name": "身份证复印件",
                            "meterialType": 2,
                            "enableFlag": 0,
                            "remark": None,
                            "existFlag": 0,
                            "urlList": [
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDF18ca204cbcc227b20d836d55059ab6b8.jpg",
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDBe423f7dfa12298159d05816a34efe81f.jpg"
                            ],
                            "serialNum": 170,
                            "linkType": 1,
                            "updateFlag": 0,
                            "optionalFlag": 0,
                            "urlListCode": [
                                "IDF",
                                "IDB"
                            ]
                        },
                        {
                            "code": "BSR",
                            "name": "业务调查报告",
                            "meterialType": 2,
                            "enableFlag": 0,
                            "remark": None,
                            "existFlag": 0,
                            "urlList": [
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/BSRcc36d15b2b759d83701349ef42dd4d4b.jpg"
                            ],
                            "serialNum": 200,
                            "linkType": 1,
                            "updateFlag": None,
                            "optionalFlag": 0,
                            "urlListCode": None
                        },
                        {
                            "code": "CCIA",
                            "name": "信用卡分期业务申请书",
                            "meterialType": 2,
                            "enableFlag": 0,
                            "remark": None,
                            "existFlag": 0,
                            "urlList": [
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CCIA7dfbcdf9f285bf0d5e47e8fdf4c84c24.jpg"
                            ],
                            "serialNum": 210,
                            "linkType": 1,
                            "updateFlag": None,
                            "optionalFlag": 0,
                            "urlListCode": None
                        },
                        {
                            "code": "BF",
                            "name": "银行流水",
                            "meterialType": 2,
                            "enableFlag": 0,
                            "remark": None,
                            "existFlag": 0,
                            "urlList": [
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg",
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3250/BFa03a7f979dc4077750d38e6e3d969c1f.jpg"
                            ],
                            "serialNum": 440,
                            "linkType": 1,
                            "updateFlag": None,
                            "optionalFlag": 0,
                            "urlListCode": None
                        },
                        {
                            "code": "BRB",
                            "name": "业务承接单",
                            "meterialType": 2,
                            "enableFlag": 0,
                            "remark": None,
                            "existFlag": 0,
                            "urlList": [
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3908/BRB9513d4c0d33be63d3273b493a8b24632.jpg"
                            ],
                            "serialNum": 820,
                            "linkType": 1,
                            "updateFlag": None,
                            "optionalFlag": 0,
                            "urlListCode": None
                        }
                    ],
                    "auditQualificationMaterial": [{
                        "code": "CPCH",
                        "name": "商品房购房合同",
                        "meterialType": 2,
                        "enableFlag": 0,
                        "remark": None,
                        "existFlag": 0,
                        "urlList": [
                            "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCH77e2de124544029a4e34b1bf01d2dc90.jpg",
                            "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCHae71ce8c4f22a0e88463df1224665f4e.jpg",
                            "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCH46538b93aeaf19b78fdc72a1d7ba305c.jpg",
                            "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCHf97121c2a17595e2396426384d71e9d4.jpg",
                            "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCH589790bb7e7ab48b8775e53f68be2261.jpg",
                            "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCHdb1b45dd32a47169e4b57c4c28df94c5.jpg"
                        ],
                        "serialNum": 410,
                        "linkType": 1,
                        "updateFlag": None,
                        "optionalFlag": 0,
                        "urlListCode": None
                    },
                        {
                            "code": "CPT",
                            "name": "商品房产调",
                            "meterialType": 2,
                            "enableFlag": 0,
                            "remark": None,
                            "existFlag": 0,
                            "urlList": [
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPT50db4532964d3127ff0ee9735c11fc25.jpg"
                            ],
                            "serialNum": 420,
                            "linkType": 1,
                            "updateFlag": None,
                            "optionalFlag": 0,
                            "urlListCode": None
                        },
                        {
                            "code": "SBHC",
                            "name": "自建房房屋证明",
                            "meterialType": 2,
                            "enableFlag": 0,
                            "remark": None,
                            "existFlag": 0,
                            "urlList": [
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/SBHC6acfb05511ab15b8cdd92c36096e4a40.jpg"
                            ],
                            "serialNum": 430,
                            "linkType": 1,
                            "updateFlag": None,
                            "optionalFlag": 0,
                            "urlListCode": None
                        },
                        {
                            "code": "BL",
                            "name": "营业执照",
                            "meterialType": 2,
                            "enableFlag": 0,
                            "remark": None,
                            "existFlag": 0,
                            "urlList": [
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/BL5f50091676026963e1ae6f28bd5a45ec.jpg"
                            ],
                            "serialNum": 450,
                            "linkType": 1,
                            "updateFlag": None,
                            "optionalFlag": 0,
                            "urlListCode": None
                        },
                        {
                            "code": "SWP",
                            "name": "特殊工作工作证",
                            "meterialType": 2,
                            "enableFlag": 0,
                            "remark": None,
                            "existFlag": 0,
                            "urlList": [
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/SWP5069539f0c71c1266c7f71f465412b40.jpg"
                            ],
                            "serialNum": 460,
                            "linkType": 1,
                            "updateFlag": None,
                            "optionalFlag": 0,
                            "urlListCode": None
                        },
                        {
                            "code": "CHPRC",
                            "name": "商品房产权证",
                            "meterialType": 2,
                            "enableFlag": 0,
                            "remark": None,
                            "existFlag": 0,
                            "urlList": [
                                "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CHPRC163d311e1cc161dae1405c08b3fea0aa.jpg"
                            ],
                            "serialNum": 680,
                            "linkType": 1,
                            "updateFlag": None,
                            "optionalFlag": 0,
                            "urlListCode": None
                        }
                    ],
                    "cityCode": 510100,
                    "countryCode": 110101,
                    "carLicenseLocationCityCode": 110100,
                    "carLicenseLocationCountryCode": 110101
                },
                "header": {
                    "app": " ",
                    "gps": " ",
                    "os": " ",
                    "ver": " ",
                    "token": token
                }
            }
            url4 = api.API.SetUrl() + "work/handle/audit"
            aa=str(payload2).encode('raw_unicode_escape')
            data = json.dumps(payload2)
            # print(str(data).replace('u\'', '\'').decode('unicode_escape'))
            response = requests.request("POST", url4, data=data, headers=headers)
            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            print ("主贷人:" + customer + "  初审审核:" + response.text1["header"]["msg"][0])
            if getsql.sql.Province():
                print (u"省区经理即将审核")
            else:
                print (u"此业务员所在地区不存在省区经理，即将跳过此节点")

# a=ChuShen.chushen()
