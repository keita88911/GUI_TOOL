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
class ZhiZhiZiLiao():
    @classmethod
    def ZhiZhiZL(self):
        token = weblogin.gettoken.token()
        taskId1 = getsql.sql.GetZhiZhiZiLiaoID()[1]
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        # print(taskId1)
        for i in range(0, len(taskId1)):
            taskId = taskId1[i]
            headers = api.API.SetHeaders()
            payload1 = {
                "data": {
                    "moduleCode": "confirmPaper",
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
            print ("主贷人:" + customer + "  纸质资料领取:" + response.text1["header"]["msg"][0])
            payload2={
	"data": {
		"custName": listdata1[i]['loanerName'],
		"custIdcard": listdata1[i]['loanerCardId'],
		"custMobile": "18583266667",
		"salesmanName": "向进/黄涛",
		"custMarriage": "1",
		"custNation": "汉族",
		"custRegister": "成都",
		"systemType": "1",
		"ccSystemType": "",
		"auditWay": "不知道",
		"financeCost": 111,
		"provinceCode": 110000,
		"areaGroup": "1",
		"carLicenseLocationProvinceCode": 110000,
		"riskAssessment": "1",
		"carModel": "AC Schnitzer/AC Schnitzer X6/2011款 ACS6 35i",
		"loanAmount": 160000,
		"driverLicenseFlag": "",
		"replaceBuyFlag": "",
		"assessorAmount": "18000",
		"loanYear": "1",
		"loanRate": 11,
		"premium": 1111,
		"otherCost": 111111,
		"gpsCost": 1111,
		"gpsQuantity": 11223,
		"payeeName": "111123",
		"payeePhone": "11112233333",
		"payeeBankAmount": "2222222",
		"payeeOpenBank": "111112",
		"insuranceCompany": "1111233",
		"otherContacts": None,
		"carType": "0",
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
		"indoorAuditOpinion": "测试审核备注12312321#!@#@!!@#@!#\nASDASDASD",
		"exAuditOpinion": None,
		"auditOpinion": "请问请问无群二群翁请问请问请问请问123123123123 奥术大师大所阿萨德按时 新增操作从自行车征信",
		"supplementOpinion": "请问请问群无切请问额\n12312321312\n12312321切尔奇翁\n123123213",
		"sendBankRemark": None,
		"handleRemark": "测试备注123213213",
		"taskId": taskId,
		"completed": "true",
		"push": "false",
		"carMeterial": None,
		"paperMeterial": [{
			"code": "LE",
			"name": "主贷人委托查询征信书",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": -1,
			"urlList": None,
			"serialNum": 30,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "LES",
			"name": "配偶委托查询征信书",
			"meterialType": 1,
			"enableFlag": None,
			"remark": None,
			"existFlag": -1,
			"urlList": None,
			"serialNum": 80,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "LEG",
			"name": "担保人委托查询征信书",
			"meterialType": 1,
			"enableFlag": None,
			"remark": None,
			"existFlag": -1,
			"urlList": None,
			"serialNum": 130,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "CCF",
			"name": "信用卡申请表",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CCF956b25520a2c313d09662d0c5e1c4b9f.jpg"],
			"serialNum": 160,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "CCF",
			"name": "信用卡申请表",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": -1,
			"urlList": None,
			"serialNum": 160,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "IDC",
			"name": "身份证复印件",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDF18ca204cbcc227b20d836d55059ab6b8.jpg", "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDBe423f7dfa12298159d05816a34efe81f.jpg"],
			"serialNum": 170,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": ["IDF", "IDB"]
		}, {
			"code": "IDC",
			"name": "身份证复印件",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": -1,
			"urlList": None,
			"serialNum": 170,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "GLC",
			"name": "担保承诺函",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 180,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "BSR",
			"name": "业务调查报告",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/BSRcc36d15b2b759d83701349ef42dd4d4b.jpg"],
			"serialNum": 200,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "BSR",
			"name": "业务调查报告",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 200,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "CCIA",
			"name": "信用卡分期业务申请书",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CCIA7dfbcdf9f285bf0d5e47e8fdf4c84c24.jpg"],
			"serialNum": 210,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "CCIA",
			"name": "信用卡分期业务申请书",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 210,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "SD",
			"name": "单身具结书或结婚证",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 220,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "PLOC",
			"name": "共偿人承诺书(个人)",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 230,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "COI",
			"name": "收入证明或收入申明",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 240,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "CPC",
			"name": "购车合同",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 250,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "CLOC",
			"name": "共偿人承诺书(公司)",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 270,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "BN",
			"name": "业务告知书",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 280,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "CCA",
			"name": "代领卡授权书",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 290,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "MC",
			"name": "抵押合同3份",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 300,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "ALOA",
			"name": "授权委托书",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 330,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "BRB",
			"name": "业务承接单",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3908/BRB9513d4c0d33be63d3273b493a8b24632.jpg"],
			"serialNum": 820,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "BRB",
			"name": "业务承接单",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 820,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}],
		"qualificationMeterial": [{
			"code": "CPCH",
			"name": "商品房购房合同",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCH77e2de124544029a4e34b1bf01d2dc90.jpg", "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCHae71ce8c4f22a0e88463df1224665f4e.jpg", "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCH46538b93aeaf19b78fdc72a1d7ba305c.jpg", "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCHf97121c2a17595e2396426384d71e9d4.jpg", "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCH589790bb7e7ab48b8775e53f68be2261.jpg", "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCHdb1b45dd32a47169e4b57c4c28df94c5.jpg"],
			"serialNum": 410,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "CPCH",
			"name": "商品房购房合同",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 410,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "CPT",
			"name": "商品房产调",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 420,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "SBHC",
			"name": "自建房房屋证明",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 430,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "BF",
			"name": "银行流水",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 440,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "BL",
			"name": "营业执照",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 450,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "SWP",
			"name": "特殊工作工作证",
			"meterialType": 1,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": None,
			"serialNum": 460,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "CHPRC",
			"name": "商品房产权证",
			"meterialType": 1,
			"enableFlag": None,
			"remark": None,
			"existFlag": -1,
			"urlList": None,
			"serialNum": 680,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "RT",
			"name": "还款小票",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/RTf3e87c299ff23fc9f84d5528003290b2.jpg"],
			"serialNum": 920,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "MAC",
			"name": "结婚证",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/MAC192910f2db9a59aaa0fcabfd386641ef.jpg", "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/MAC21ad6330f80f9e5a9bf01296b30f8960.jpg"],
			"serialNum": 930,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "DC",
			"name": "离婚证",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/DC7c127c98a14fdb13dfdabaf596f67387.jpg", "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/DC411fffa0b5eab2419d7043d4e6ae93c0.jpg"],
			"serialNum": 940,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "HB",
			"name": "户口本",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/HB8c2aa2b73f20c4530e60bba0ddf6d7d7.jpg", "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/HB6f793f9ae96614b7047dca6f21e6d828.jpg", "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/HB2b6af99368d89d4abddd5a39445cc139.jpg", "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/HBbc9345e7b2e873f1efd9501907fe1cb0.jpg", "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/HBc6ff32c6ea3501fdac34630c5bac09e8.jpg"],
			"serialNum": 950,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "RHA",
			"name": "安置房协议",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/RHA30d1cffac267fe5f375c71fd76651964.jpg", "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/RHA12885d06bb3b0da492d3a6142c9c1e7a.jpg", "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/RHAdabd490aa72a9fce83129c7fe7d20bbc.jpg", "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/RHA80c9b4f22047f587910e30dcf4f681ea.jpg"],
			"serialNum": 960,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}],
		"cityCode": 110100,
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
            url4 = api.API.SetUrl() + "work/handle/confirmPaper"
            data = json.dumps(payload2)
            response = requests.request("POST", url4, data=data, headers=headers)
            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            print ("主贷人:" + customer + "  纸质资料审核:" + response.text1["header"]["msg"][0])
# a=ZhiZhiZiLiao.ZhiZhiZL()