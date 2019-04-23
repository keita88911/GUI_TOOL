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
class AddCaiWu():
    @classmethod
    def AddCaiWu(self):
        token = weblogin.gettoken.token()
        taskId1 = getsql.sql.AddCaiWu()[1]
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        # print(taskId1)
        for i in range(0, len(taskId1)):
            taskId = taskId1[i]
            headers = api.API.SetHeaders()
            # payload1 = {
            #     "data": {
            #         "moduleCode": "transcribeOrder",
            #         "taskId": taskId
            #     },
            #     "ext": "string",
            #     "header": {
            #         "app": "string",
            #         "gps": "string",
            #         "os": "string",
            #         "token": token,
            #         "ver": "string"
            #     }
            # }
            # url3 = api.API.SetUrl() + "work/receiveTask"
            # data = json.dumps(payload1)
            # response = requests.request("POST", url3, data=data, headers=headers)
            # response.text1 = json.loads(response.text)
            # customer = getsql.sql.GetName()[i]
            # print ("主贷人:" + customer + "  抄单领取:" + response.text1["header"]["msg"][0])

            payload2={
	"data": {
		"materFull": 0,


		"custName": listdata1[i]['loanerName'],
		"custIdcard":  listdata1[i]['loanerCardId'],
		"custMobile": "18583266667",
		"salesmanName": "向进/高家源",
		"custMarriage": "1",
		"custNation": "汉族",
		"custRegister": "成都",
		"custRegisterAddress": None,
		"systemType": "1",
		"ccSystemType": "",
		"auditWay": "不知道",
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
		"payeePhone": None,
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
		"sgNo": None,
		"reportNo": None,
		"appraisalTime": None,
		"carVin": None,
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
		"payeeName": "四川惠商信息科技有限公司",
		"payeeBankAmount": "6225881287543051",
		"payeeOpenBank": "测试开户行",
		"province": 8,
		"city": 131,
		"taskId": taskId,
		"completed": "true",
		"push": "false",
		"addFinancialAdvanceMaterial": [{
			"code": "HVPIA",
			"name": "家访照片(室内)",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": "",
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/HVPIA48d8731769e8c2548a0390435ac32ed7.jpg",
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/HVPIAd5a53a595c6c4c623b83a7aac4e985fe.jpg"],
			"serialNum": 310,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "HVPOA",
			"name": "家访照片(室外)",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": "",
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/HVPOA83e8b927b5397966982e7227c3b1346a.jpg",
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/HVPOAa24c0305bef9e2a2a52f2f9ecb0e3a8b.jpg"],
			"serialNum": 320,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "SV",
			"name": "签单视频",
			"meterialType": 3,
			"enableFlag": 0,
			"remark": "",
			"existFlag": 0,
			"urlList": None,
			"serialNum": 340,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "QAV",
			"name": "问答视频",
			"meterialType": 3,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": [],
			"serialNum": 350,
			"linkType": 1,
			"updateFlag": None,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "PPA",
			"name": "保单照片",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": "",
			"existFlag": 0,
			"urlList": [],
			"serialNum": 360,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "HV",
			"name": "家访视频",
			"meterialType": 3,
			"enableFlag": 0,
			"remark": "",
			"existFlag": 0,
			"urlList": None,
			"serialNum": 670,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}],
		"addFinancialAptitudesMaterial": [{
			"code": "CPCH",
			"name": "商品房购房合同",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": "",
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCH77e2de124544029a4e34b1bf01d2dc90.jpg",
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCHae71ce8c4f22a0e88463df1224665f4e.jpg",
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCH46538b93aeaf19b78fdc72a1d7ba305c.jpg",
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCHf97121c2a17595e2396426384d71e9d4.jpg",
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCH589790bb7e7ab48b8775e53f68be2261.jpg",
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPCHdb1b45dd32a47169e4b57c4c28df94c5.jpg"],
			"serialNum": 410,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "CPT",
			"name": "商品房产调",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": "",
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CPT50db4532964d3127ff0ee9735c11fc25.jpg"],
			"serialNum": 420,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "SBHC",
			"name": "自建房房屋证明",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": "",
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/SBHC6acfb05511ab15b8cdd92c36096e4a40.jpg"],
			"serialNum": 430,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "BL",
			"name": "营业执照",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": "",
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/BL5f50091676026963e1ae6f28bd5a45ec.jpg"],
			"serialNum": 450,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "SWP",
			"name": "特殊工作工作证",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": "",
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/SWP5069539f0c71c1266c7f71f465412b40.jpg"],
			"serialNum": 460,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "CHPRC",
			"name": "商品房产权证",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": "",
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3934/CHPRC163d311e1cc161dae1405c08b3fea0aa.jpg"],
			"serialNum": 680,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}],
		"addFinancialAuditMaterial": [{
			"code": "IDF",
			"name": "主贷人身份证正面",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": "None",
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDF18ca204cbcc227b20d836d55059ab6b8.jpg"],
			"serialNum": 10,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "IDB",
			"name": "主贷人身份证反面",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": "None",
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDBe423f7dfa12298159d05816a34efe81f.jpg"],
			"serialNum": 20,
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
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/CCFf9a4db9e4b93964bdf9f91a84bf43b22.jpg"],
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
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDF18ca204cbcc227b20d836d55059ab6b8.jpg",
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDBe423f7dfa12298159d05816a34efe81f.jpg"],
			"serialNum": 170,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": ["IDF", "IDB"]
		}, {
			"code": "BSR",
			"name": "业务调查报告",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/BSRd422e94b6a30cc970bda06bcbaffa233.jpg"],
			"serialNum": 200,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "CCIA",
			"name": "信用卡分期业务申请书",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/CCIA2568aedde2d9176f70857becee3f6ee4.jpg"],
			"serialNum": 210,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
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
			"urlListCode": None
		}, {
			"code": "RCMVA",
			"name": "机动车登记证书(过户后)",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/12847/RCMVAb22ca574f26ef08e6f0c329192e9553f.jpg"],
			"serialNum": 380,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
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
			"urlListCode": None
		}, {
			"code": "MVDLA",
			"name": "机动车行驶证(过户后)",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/12847/MVDLA3874c84bd0f0c43755c33ec908325002.jpg"],
			"serialNum": 400,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "LPPA",
			"name": "车牌号照片(过户后)",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/12847/LPPAc46a385868f2350d9b85b90ff95a0655.jpg"],
			"serialNum": 401,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
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
			"urlListCode": None
		}, {
			"code": "BF",
			"name": "银行流水",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": None,
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/10017/BFf78ad79a1554ddb9e931a708df498064.jpg"],
			"serialNum": 440,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "TLP",
			"name": "临时车牌",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": "",
			"existFlag": 0,
			"urlList": [
				"https://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/12847/TLP571cb6f51424e313ccdfa5865afa899b.jpg"],
			"serialNum": 840,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "INV",
			"name": "发票",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": "",
			"existFlag": 0,
			"urlList": [],
			"serialNum": 850,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "VOU",
			"name": "办理凭证",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": "",
			"existFlag": 0,
			"urlList": [],
			"serialNum": 860,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "FV",
			"name": "提档凭证",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": "",
			"existFlag": 0,
			"urlList": [],
			"serialNum": 870,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
		}, {
			"code": "AA",
			"name": "公证书",
			"meterialType": 2,
			"enableFlag": 0,
			"remark": "",
			"existFlag": 0,
			"urlList": [],
			"serialNum": 880,
			"linkType": 1,
			"updateFlag": 0,
			"optionalFlag": 0,
			"urlListCode": None
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
            url4 = api.API.SetUrl() + "work/handle/addFinanceInfo"
            data = json.dumps(payload2)
            response = requests.request("POST", url4, data=data, headers=headers)
            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            # print(response.text)
            print ("主贷人:" + customer + "  添加财务信息审核:" + response.text1["header"]["msg"][0])
# a=AddCaiWu.AddCaiWu()