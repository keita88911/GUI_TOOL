# -*- coding: UTF-8 -*-
import rdexcel
import requests
import json
import weblogin
import  MySQLdb
import getsql
import api
import sys
import uniout
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
class zhuhang():

    @classmethod
    def ZhuHangDY(self):
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        token = weblogin.gettoken.token()
        taskId1 = getsql.sql.getsqldata()[1]
        id1=getsql.sql.getsqldata()[0]


        for i in range(0,len(taskId1)):
            taskId=taskId1[i]
            id=id1[i]
            headers = api.API.SetHeaders()
            payload1={
                 "data": {
                     "moduleCode": "creditPrint",
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
            url3 = api.API.SetUrl()+"work/receiveTask"
            data = json.dumps(payload1)
            # print(payload1)
            response = requests.request("POST", url3, data=data, headers=headers)

            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            print ("主贷人:" + customer + "  驻行打印领取:" + response.text1["header"]["msg"][0])

            '''征信编辑-快贷-房贷'''

            if listdata1[i]['fast_loan'] == "1":
                url5 = api.API.SetUrl() + "work/extra/updateBankCreditReport"
                payload5 = {
                        "data": {
                            "id": id,
                            "requestId": taskId,
                            "custName": listdata1[i]['loanerName'],
                            "custIdcard": listdata1[i]['loanerCardId'],
                            "trialPass": None,
                            "married": None,
                            "education": None,
                            "couple": "",
                            "baihu": None,
                            "jinru": None,
                            "yuqiCount": None,
                            "accountDetail": None,
                            "waibuqizha": None,
                            "has14": None,
                            "greyList": None,
                            "guaranteeCount": None,
                            "guaranteeAmount": None,
                            "guaranteeStatus": None,
                            "creditCardCount": None,
                            "usedMoney": None,
                            "overdue12": None,
                            "overdue24": None,
                            "yearA": None,
                            "monthA": None,
                            "nameA": "1",
                            "amountA": None,
                            "amountYueA": "11",
                            "loanFangshiA": None,
                            "loanQishuA": None,
                            "yearB": None,
                            "monthB": None,
                            "nameB": None,
                            "amountB": None,
                            "amountYueB": None,
                            "loanFangshiB": None,
                            "loanQishuB": None,
                            "yearC": None,
                            "monthC": None,
                            "nameC": None,
                            "amountC": None,
                            "amountYueC": None,
                            "loanFangshiC": None,
                            "loanQishuC": None,
                            "ghCreditLine": None,
                            "ghCardCount": None,
                            "allLoanTotal": None,
                            "allLoanAmount": None,
                            "repaymentTypeA": None,
                            "repaymentMonthA": "11",
                            "loanOverdueMonthA": None,
                            "currentOverdueAmountA": None,
                            "currentStatusA": None,
                            "repaymentTypeC": None,
                            "repaymentMonthC": None,
                            "loanOverdueMonthC": None,
                            "currentOverdueAmountC": None,
                            "currentStatusC": None,
                            "repaymentTypeB": None,
                            "repaymentMonthB": None,
                            "loanOverdueMonthB": None,
                            "currentOverdueAmountB": None,
                            "currentStatusB": None,
                            "creditCardOrg": None,
                            "accountCount": None,
                            "creditLine": None,
                            "usedLine": None,
                            "loanYearA": None,
                            "loanMonthA": None,
                            "loanCreditLineA": None,
                            "loanUsedLineA": None,
                            "overdueYearMonthA": None,
                            "overdueAmountA": None,
                            "overdueStatusA": None,
                            "loanYearB": None,
                            "loanMonthB": None,
                            "loanCreditLineB": None,
                            "loanUsedLineB": None,
                            "overdueYearMonthB": None,
                            "overdueAmountB": None,
                            "overdueStatusB": None,
                            "queryName": None,
                            "queryTime": None,
                            "remark": None,
                            "creditType": 0,
                            "changeCompany": None,
                            "riskRankFive": None,
                            "queryCountThree": None,
                            "loanerFlag": None,
                            "currentOverdue": None,
                            "loan": None,
                            "credit": None,
                            "daiAmount": None,
                            "creditUsedLimit": None,
                            "yuqiCountA": None,
                            "creditLoanRecordVos": [],
                            "creditResult": "第三方征信查询不通过",
                            "isNew": "1",
                            "bankName": "工行"
                        },
                        "header": {
                            "app": "",
                            "gps": "",
                            "os": "",
                            "ver": "",
                            "token": token
                        }

                }
                data = json.dumps(payload5)
                response = requests.request("POST", url5, data=data, headers=headers)
                response.text1 = json.loads(response.text)
                # print(data)
                # print(url5)
                # print(headers)
                # print( response.text1["header"])
                if response.text1['header']['ret']=="S":
                    print(u'征信编辑成功-房贷')
                print(u'即将修改第三方征信结果')
                updata=getsql.sql.updata_zhengxin()

            payload2={
                      "data": {
                        "completed": "true",
                        "creditMeterial": [
                            {
                                "code": "IDF",
                                "name": "........................",
                                "meterialType": 2,
                                "enableFlag": 0,
                                "remark": "null",
                                "existFlag": 0,
                                "urlList": [
                                    "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDF18ca204cbcc227b20d836d55059ab6b8.jpg"],
                                "serialNum": 10,
                                "linkType": 1,
                                "updateFlag": "null",
                                "optionalFlag": 0
                            }, {
                                "code": "IDB",
                                "name": "........................",
                                "meterialType": 2,
                                "enableFlag": 0,
                                "remark": "null",
                                "existFlag": 0,
                                "urlList": [
                                    "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDBe423f7dfa12298159d05816a34efe81f.jpg"],
                                "serialNum": 20,
                                "linkType": 1,
                                "updateFlag": "null",
                                "optionalFlag": 0
                            }, {
                                "code": "LE",
                                "name": "..............................",
                                "meterialType": 2,
                                "enableFlag": 0,
                                "remark": "null",
                                "existFlag": 0,
                                "urlList": [
                                    "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/LE58583af34c31202acc9bf3a3709bad08.jpg"],
                                "serialNum": 30,
                                "linkType": 1,
                                "updateFlag": "null",
                                "optionalFlag": 0
                            }, {
                                "code": "AP",
                                "name": "........................",
                                "meterialType": 2,
                                "enableFlag": 0,
                                "remark": "null",
                                "existFlag": 0,
                                "urlList": [
                                    "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/AP5b9708d50f9f8d8b1b2ef0cb82785e20.jpg"],
                                "serialNum": 40,
                                "linkType": 1,
                                "updateFlag": "null",
                                "optionalFlag": 0
                            },


                          {
                            "code": "string",
                            "enableFlag": 0,
                            "existFlag": 0,
                            "linkType": 0,
                            "meterialType": 0,
                            "name": "string",
                            "optionalFlag": 0,
                            "remark": "string",
                            "serialNum": 0,
                            "updateFlag": 0,
                            "urlList": [
                              "string"
                            ]
                          }
                        ],
                        "handleRemark": "string",
                        "push": "false",
                        "result": 1,
                        "segmentNo": 11,
                        "taskId": taskId,
                        "toUserId": 338
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
            url4 = api.API.SetUrl()+"work/handle/creditPrint"
            data = json.dumps(payload2)
            # print(data)
            response = requests.request("POST", url4, data=data, headers=headers)
            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            print ("主贷人:" + customer + "  驻行打印指派:" + response.text1["header"]["msg"][0])
    @classmethod
    def songshen(self):

        token = weblogin.gettoken.ZhuHangSStoken()
        id2=getsql.sql.getsqldata()[0]
        taskId1 = getsql.sql.getsqldata()[1]
        # token = weblogin.gettoken.token()
        process_id1 = getsql.sql.GetZhengxinReprot()[1]
        id1 = getsql.sql.GetZhengxinReprot()[0]
        # print(taskId1)

        for i in range(0,len(taskId1)):
            taskId=taskId1[i]
            headers = api.API.SetHeaders()
            url1 = api.API.SetUrl()+"work/receiveTask"
            payload1 = {
                      "data": {
                        "moduleCode": "credit",
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
            data = json.dumps(payload1)
            response = requests.request("POST", url1, data=data, headers=headers)
            #领取待办
            url2 = api.API.SetUrl()+"work/handle/credit"
            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            payload2 = {
                          "data": {
                            "completed": "true",
                            "creditMeterial": [{
                              "code": "IDF",
                              "name": "........................",
                              "meterialType": 2,
                              "enableFlag": 0,
                              "remark": "null",
                              "existFlag": 0,
                              "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDF18ca204cbcc227b20d836d55059ab6b8.jpg"],
                              "serialNum": 10,
                              "linkType": 1,
                              "updateFlag": "null",
                              "optionalFlag": 0
                            }, {
                              "code": "IDB",
                              "name": "........................",
                              "meterialType": 2,
                              "enableFlag": 0,
                              "remark": "null",
                              "existFlag": 0,
                              "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/IDBe423f7dfa12298159d05816a34efe81f.jpg"],
                              "serialNum": 20,
                              "linkType": 1,
                              "updateFlag": "null",
                              "optionalFlag": 0
                            }, {
                              "code": "LE",
                              "name": "..............................",
                              "meterialType": 2,
                              "enableFlag": 0,
                              "remark": "null",
                              "existFlag": 0,
                              "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/LE58583af34c31202acc9bf3a3709bad08.jpg"],
                              "serialNum": 30,
                              "linkType": 1,
                              "updateFlag": "null",
                              "optionalFlag": 0
                            }, {
                              "code": "AP",
                              "name": "........................",
                              "meterialType": 2,
                              "enableFlag": 0,
                              "remark": "null",
                              "existFlag": 0,
                              "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/510104198806031672/AP5b9708d50f9f8d8b1b2ef0cb82785e20.jpg"],
                              "serialNum": 40,
                              "linkType": 1,
                              "updateFlag": "null",
                              "optionalFlag": 0
                            },
                              {
                                "code": "IDF",
                                "enableFlag": 0,
                                "existFlag": 0,
                                "linkType": 1,
                                "meterialType": 0,
                                "name": "string",
                                "optionalFlag": 0,
                                "remark": "null",
                                "serialNum": 10,
                                "updateFlag": 0,
                                "urlList": [
                                  "string"
                                ]
                              }
                            ],
                            "handleRemark": "string",
                            "push": "true",
                            "result": 1,

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
            data = json.dumps(payload2)
            response2=requests.request("POST", url2, data=data, headers=headers)
            response.text1 = json.loads(response2.text)
            customer = getsql.sql.GetName()[i]
            print ("主贷人:"+customer+ "  驻行审核:"+response.text1["header"]["msg"][0])




# a=zhuhang.ZhuHangDY()
