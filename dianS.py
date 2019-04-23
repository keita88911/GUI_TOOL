# -*- coding: UTF-8 -*-
import requests
import json
import applogin
import rdexcel
import MySQLdb
import getsql
import api
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class buchongdianS():
    @classmethod
    def dianSS(self):
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        token = applogin.gettoken.token()
        taskId1 = getsql.sql.getsqldata()[1]
        id1 = getsql.sql.getsqldata()[0]
        # print(taskId1)
        for i in range(0, len(listdata1)):
            taskId = taskId1[i]
            id = id1[i]
            headers = {'Content-Type': "application/json", }
            url = api.API.SetUrl() + "v1/app/mytask/commitPhoneAudit"
            newcar = int(listdata1[i]['newcar'])
            if newcar == 1:

                payload = {
                    "carVo": {
                        "carAge": 0,
                        "loanYears": 3,
                        "loanRate": 30,
                        "financeCost": 22,
                        "loanAmount": listdata1[i]['loanAmount'],
                        "pageNum": 0,
                        "pageSize": 0,
                        "pgPrice": 0,
                        "price": 0,
                        "type": 0
                    },

                    "imageList": [{
                        "code": "CCF",
                        "path": "erp/10017/CCFf9a4db9e4b93964bdf9f91a84bf43b22.jpg"
                    }, {
                        "code": "BSR",
                        "path": "erp/10017/BSRd422e94b6a30cc970bda06bcbaffa233.jpg"
                    }, {
                        "code": "CCIA",
                        "path": "erp/10017/CCIA2568aedde2d9176f70857becee3f6ee4.jpg"
                    }, {
                        "code": "BRB",
                        "path": "erp/10017/BRBff17a7e9398cf478f35466ac1e916358.jpg"
                    }, {
                        "code": "BF",
                        "path": "erp/10017/BFf78ad79a1554ddb9e931a708df498064.jpg"
                    }, {
                        "code": "CFD",
                        "path": "erp/10017/CFD36d3538a2b9091b9b2193dba51ff70af.jpg"
                    }, {
                        "code": "COS",
                        "path": "erp/10017/COS86cacb5e62a8142659ed5eca03fde4a0.jpg"
                    }, {
                        "code": "CB",
                        "path": "erp/10017/CB4f5d5da1887c19ad6d7fdd4da42de890.jpg"
                    }, {
                        "code": "FSC",
                        "path": "erp/10017/FSC9303f26272bfae3ec7f327fd52289e60.jpg"
                    }, {
                        "code": "CR",
                        "path": "erp/10017/CRff9413c5a407c29df3b72ab2f1ad613e.jpg"
                    }, {
                        "code": "CFR",
                        "path": "erp/10017/CFRbf1b0a58243451d51359002d6875ea4a.jpg"
                    }, {
                        "code": "CBR",
                        "path": "erp/10017/CBRd4591165be0836fdcec9be88421abef4.jpg"
                    }, {
                        "code": "CN",
                        "path": "erp/10017/CN416e0a028b2e601c59c5c9200a2094c5.jpg"
                    }, {
                        "code": "OPI",
                        "path": "erp/10017/OPI99b1f63f1af17af3fcf939093967fa8b.jpg"
                    }, {
                        "code": "PMC",
                        "path": "erp/10017/PMCd6c0ba52533a23f2d39db9c272057620.jpg"
                    },
                        {
                            "code": "ECI",
                            "path": "erp/10017/ECI1c21bb1c18b82e8ee6e4545371b5a8fc.jpg"
                        }, {
                            "code": "MCI",
                            "path": "erp/10017/MCIfa53388a962d32f7c87c186a580a0644.jpg"
                        }, {
                            "code": "SW",
                            "path": "erp/10017/SWe709f8ed2758bd015140d5e6a7152e20.jpg"
                        }, {
                            "code": "MSSS",
                            "path": "erp/10017/MSSS0c8bf74dcec5751166c440d354110cc1.jpg"
                        }, {
                            "code": "VSSS",
                            "path": "erp/10017/VSSS97ba8398a43fef74ff1a1b03d4f799ac.jpg"
                        }, {
                            "code": "SP",
                            "path": "erp/10017/SP5bbd21d169e0a545aaa89d16e450af88.jpg"
                        },

                    ],
                    "os": "android",
                    "phone": "18583287560",
                    "reqId": id,
                    "step": 2,
                    "taskId": taskId,
                    "token": token,

                }
            else:

                payload = {

                    "carVo": {
                        "mainLenderMeterial": [{
                            "id": "m1-1",
                            "uploadImages": [{
                                "code": "QL-YYZZ",
                                "path": "erp//QL-YYZZ20e9715a79b2c4ac39a214b9dfaa8c2e.jpg"
                            }, {
                                "code": "QL-JYCSZP",
                                "path": "erp//QL-JYCSZPf43a12200b11918e332f3d4d8072a798.jpg"
                            }],
                            "value": 1
                        }],
                        "loanYears": 3,
                        "loanAmount": listdata1[i]['loanAmount'],
                        "autohomeid": "143711",
                        "loanRate": 30,
                        "buessCheckDate": "",
                        "capacity": "6",
                        "carAge": 0,
                        "carCondition": 2,
                        "carDealer": "车商",
                        "carDes": "",
                        "carModel": "雪豹2.8-MT柴油前驱(国Ⅳ)5档 手动",
                        "city": "87",
                        "cityName": "长治市",
                        "color": "银灰色",
                        "financeCost": 200,
                        "gearBox": "手动",
                        "jsCarModel": "",
                        "km": "6.0",

                        "pageNum": 0,
                        "pageSize": 0,
                        "pgPrice": 0,
                        "price": 0,
                        "province": "4",
                        "regdate": "2018-10",
                        "skylightType": "内藏式",
                        "strongRiskDate": "",
                        "type": 0,
                        "useType": 1,
                        "vin": "JTHGM46F3B5044228",
                        "yearCheckDate": "",

                        "yearCheckDate": "2018-06"

                    },
                    "imageList": [
                        #                        {
                        #                		"code": "CCF",
                        # 	"path": "erp/10017/CCFf9a4db9e4b93964bdf9f91a84bf43b22.jpg"
                        # },
                        {
                            "code": "BSR",
                            "path": "erp/10017/BSRd422e94b6a30cc970bda06bcbaffa233.jpg"
                        }, {
                            "code": "CCIA",
                            "path": "erp/10017/CCIA2568aedde2d9176f70857becee3f6ee4.jpg"
                        }, {
                            "code": "BRB",
                            "path": "erp/10017/BRBff17a7e9398cf478f35466ac1e916358.jpg"
                        }, {
                            "code": "BF",
                            "path": "erp/10017/BFf78ad79a1554ddb9e931a708df498064.jpg"
                        }, {
                            "code": "CFD",
                            "path": "erp/10017/CFD36d3538a2b9091b9b2193dba51ff70af.jpg"
                        }, {
                            "code": "COS",
                            "path": "erp/10017/COS86cacb5e62a8142659ed5eca03fde4a0.jpg"
                        }, {
                            "code": "CB",
                            "path": "erp/10017/CB4f5d5da1887c19ad6d7fdd4da42de890.jpg"
                        }, {
                            "code": "FSC",
                            "path": "erp/10017/FSC9303f26272bfae3ec7f327fd52289e60.jpg"
                        }, {
                            "code": "CR",
                            "path": "erp/10017/CRff9413c5a407c29df3b72ab2f1ad613e.jpg"
                        }, {
                            "code": "CFR",
                            "path": "erp/10017/CFRbf1b0a58243451d51359002d6875ea4a.jpg"
                        }, {
                            "code": "CBR",
                            "path": "erp/10017/CBRd4591165be0836fdcec9be88421abef4.jpg"
                        }, {
                            "code": "CN",
                            "path": "erp/10017/CN416e0a028b2e601c59c5c9200a2094c5.jpg"
                        }, {
                            "code": "OPI",
                            "path": "erp/10017/OPI99b1f63f1af17af3fcf939093967fa8b.jpg"
                        }, {
                            "code": "PMC",
                            "path": "erp/10017/PMCd6c0ba52533a23f2d39db9c272057620.jpg"
                        }, {
                            "code": "ECI",
                            "path": "erp/10017/ECI1c21bb1c18b82e8ee6e4545371b5a8fc.jpg"
                        }, {
                            "code": "MCI",
                            "path": "erp/10017/MCIfa53388a962d32f7c87c186a580a0644.jpg"
                        }, {
                            "code": "SW",
                            "path": "erp/10017/SWe709f8ed2758bd015140d5e6a7152e20.jpg"
                        }, {
                            "code": "MSSS",
                            "path": "erp/10017/MSSS0c8bf74dcec5751166c440d354110cc1.jpg"
                        }, {
                            "code": "VSSS",
                            "path": "erp/10017/VSSS97ba8398a43fef74ff1a1b03d4f799ac.jpg"
                        }, {
                            "code": "SP",
                            "path": "erp/10017/SP5bbd21d169e0a545aaa89d16e450af88.jpg"
                        }, {
                            "code": "CJH",
                            "path": "erp/57039/CJHae342e3559dd546c786167f871955435.jpg"
                        }, {
                            "code": "RCMVB",
                            "path": "erp/57039/RCMVB1957a2db1b72ea52041a986f084dc309.jpg"
                        },
                        {
                            "code": "PRICE_300",
                            "path": "erp/75749/PRICE_300ed5c6b44bbedf31bf16db384993d1327.jpg"
                        },
                    ],
                    "os": "android",
                    "phone": "18583287560",
                    "reqId": id,
                    "step": 2,
                    "taskId": taskId,
                    "token": token

                }

            data = json.dumps(payload)

            response = requests.request("POST", url, data=data, headers=headers)
            response.text1 = json.loads(response.text)
            # print(response.text)
            customer = getsql.sql.GetName()[i]
            # print(response.text)
            print ("主贷人:" + customer + "  电审节点:" + response.text1["msg"])
# a=buchongdianS()
# a.dianSS()
