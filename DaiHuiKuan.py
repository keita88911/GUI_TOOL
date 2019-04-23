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
class DaiHuiKuan():
    @classmethod
    def daihuikuan(self):
        token = weblogin.gettoken.token()
        taskId1 = getsql.sql.auto('待回款任务池')[1]
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        # print(taskId1)
        for i in range(0, len(taskId1)):
            taskId = taskId1[i]
            headers = api.API.SetHeaders()
            payload1 = {
                "data": {
                    "moduleCode": "paymentTaskPool",
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
            print ("主贷人:" + customer + "  待汇款领取:" + response.text1["header"]["msg"][0])

            payload2={
	"data": {
        "custName": listdata1[i]['loanerName'],
        "custIdcard": listdata1[i]['loanerCardId'],
        "custMobile": listdata1[i]['mobile'],
		"salesmanName": "向进/高家鲜",
		"custMarriage": "",
		"custNation": None,
		"custRegister": None,
		"custRegisterAddress": None,
		"systemType": "",
		"ccSystemType": "",
		"auditWay": None,
		"financeCost": None,
		"provinceCode": None,
		"areaGroup": "",
		"carLicenseLocationProvinceCode": None,
		"riskAssessment": "",
		"carModel": "123",
		"loanAmount": None,
		"driverLicenseFlag": "",
		"replaceBuyFlag": "",
		"assessorAmount": 123,
		"loanYear": "",
		"loanRate": None,
		"premium": None,
		"otherCost": None,
		"gpsCost": None,
		"gpsQuantity": None,
		"payeeName": "啊啊啊~啊啊啊~",
		"payeePhone": None,
		"payeeBankAmount": None,
		"payeeOpenBank": None,
		"insuranceCompany": None,
		"otherContacts": None,
		"carType": "1",
		"carAuto": "",
		"carCapacity": None,
		"carMileage": None,
		"carColor": None,
		"carAge": None,
		"carSkylight": None,
		"carConfig": None,
		"environment": None,
		"carDealer": None,
		"vin": None,
		"regdate": "2018-05",
		"gearBox": None,
		"yearCheckDate": None,
		"buessCheckDate": None,
		"strongRiskDate": None,
		"sgNo": None,
		"reportNo": None,
		"appraisalTime": None,
		"carVin": None,
		"evaluationCompany": "东方航空公司",
		"rebate": "2323",
		"actualPay": "23232",
		"payerName": "3232323",
		"loanTime": "2018-09-19",
		"actualFinanceCost": "2323",
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
		"auditOpinion": None,
		"supplementOpinion": None,
		"sendBankRemark": None,
		"toPaymentPool": 0,
		"cback": True,
		"taskId": taskId,
		"completed": True,
		"push": False,
		"cityCode": None,
		"countryCode": None,
		"carLicenseLocationCityCode": None
	},
	"header": {
		"app": " ",
		"gps": " ",
		"os": " ",
		"ver": " ",
		"token": token
	}
}
            url4 = api.API.SetUrl() + "work/handle/paymentFinish"
            data = json.dumps(payload2)
            response = requests.request("POST", url4, data=data, headers=headers)
            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            # print(taskId)
            print ("主贷人:" + customer + "  抄单内勤审核:" + response.text1["header"]["msg"][0])
# a=ChaoDanNeiQin.ChaoDanNeiQ()