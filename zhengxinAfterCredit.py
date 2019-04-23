#!usr/bin/python
# -*- coding: utf-8 -*-
import applogin
import rdexcel
import requests
import json
import sys
import getsql
import api
import weblogin

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
class zhegnxinAC():
    # token = applogin.gettoken.token()
    # taskId1 = getsql.sql.GetZhengxinID()[1]
    # id1 = getsql.sql.GetZhengxinID()[0]
    # headers = api.API.SetHeaders()
    @classmethod
    def zhengxinJichu(self):
        token = applogin.gettoken.token()
        taskId1 = getsql.sql.GetZhengxinID()[1]
        id1 = getsql.sql.GetZhengxinID()[0]
        headers = api.API.SetHeaders()
        url=api.API.SetUrl()+"v1/app/mytask/commitInfoAfterCredit"
        for i in range(0, len(taskId1)):
            token=token
            taskId = taskId1[i]
            id=id1[i]
            payload= {
                "imageList": [{
                    "code": "HVPIA",
                    "path": "erp/3934/HVPIA48d8731769e8c2548a0390435ac32ed7.jpg"
                }, {
                    "code": "HVPIA",
                    "path": "erp/3934/HVPIAd5a53a595c6c4c623b83a7aac4e985fe.jpg"
                } ,{
                    "code": "HVPOA",
                    "path": "erp/3934/HVPOA83e8b927b5397966982e7227c3b1346a.jpg"
                }, {
                    "code": "HVPOA",
                    "path": "erp/3934/HVPOAa24c0305bef9e2a2a52f2f9ecb0e3a8b.jpg"
                } ,{
                    "code": "ALOA",
                    "path": "erp/3934/ALOA830fdb11303f89d125b1c2d6b0d01a88.jpg"
                }],
                "os": "android",
                "phone": "18583287560",
                "reqId": id,
                "step": 3,
                "taskId": taskId,
                "token": token
                
            }
            data=json.dumps(payload)
            response=requests.request("POST", url, data=data, headers=headers)
            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            print("主贷人:"+customer+"  征信后必要基础资料提交:"+response.text1["msg"])
    @classmethod
    def zhengxinBiyao(self):
        token = applogin.gettoken.token()
        taskId1 = getsql.sql.GetZhengxinID()[1]
        id1 = getsql.sql.GetZhengxinID()[0]
        headers = api.API.SetHeaders()

        url=api.API.SetUrl()+"v1/app/mytask/commitInfoAfterCredit"
        for i in range(0, len(taskId1)):
            token=token
            taskId =taskId1[i]
            id=id1[i]
            payload={
    "os": "android",
    "paperList": [
        "GLC",
        "SD",
        "PLOC",
        "COI",
        "CPC",
        "LOG",
        "CLOC",
        "BN",
        "CCA",
        "MC",
        "BSR",
        "CCIA",
        "HVPI",
        "ALOA",
        "BF",
        "BRB"
    ],
    "phone": "18583287560",
    "reqId": id,
    "step": 5,
    "taskId": taskId,
    "token": token,
    "videoList": ["SV", "QAV", "HV"]
    }
            data = json.dumps(payload)
            response=requests.request("POST",url,data=data,headers=headers)
            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            print("主贷人:"+customer+"  征信后必要纸质资料提交:"+response.text1["msg"])
    @classmethod
    def zhenxinXuantian(self):
        token = applogin.gettoken.token()
        taskId1 = getsql.sql.GetZhengxinID()[1]
        id1 = getsql.sql.GetZhengxinID()[0]
        headers = api.API.SetHeaders()
        url = api.API.SetUrl() + "v1/app/mytask/commitInfoAfterCredit"

        for i in range(0, len(taskId1)):

            token = token
            taskId = taskId1[i]
            id =id1[i]
            payload ={
                "imageList": [{
                    "code": "CPCH",
                    "path": "erp/3934/CPCH77e2de124544029a4e34b1bf01d2dc90.jpg"
                } ,{
                    "code": "CPCH",
                    "path": "erp/3934/CPCHae71ce8c4f22a0e88463df1224665f4e.jpg"
                } ,{
                    "code": "CPCH",
                    "path": "erp/3934/CPCH46538b93aeaf19b78fdc72a1d7ba305c.jpg"
                } ,{
                    "code": "CPCH",
                    "path": "erp/3934/CPCHf97121c2a17595e2396426384d71e9d4.jpg"
                }, {
                    "code": "CPCH",
                    "path": "erp/3934/CPCH589790bb7e7ab48b8775e53f68be2261.jpg"
                } ,{
                    "code": "CPCH",
                    "path": "erp/3934/CPCHdb1b45dd32a47169e4b57c4c28df94c5.jpg"
                } ,{
                    "code": "CPT",
                    "path": "erp/3934/CPT50db4532964d3127ff0ee9735c11fc25.jpg"
                } ,{
                    "code": "SBHC",
                    "path": "erp/3934/SBHC6acfb05511ab15b8cdd92c36096e4a40.jpg"
                } ,{
                    "code": "BL",
                    "path": "erp/3934/BL5f50091676026963e1ae6f28bd5a45ec.jpg"
                } ,{
                    "code": "SWP",
                    "path": "erp/3934/SWP5069539f0c71c1266c7f71f465412b40.jpg"
                } ,{
                    "code": "CHPRC",
                    "path": "erp/3934/CHPRC163d311e1cc161dae1405c08b3fea0aa.jpg"
                } ,{
                    "code": "RT",
                    "path": "erp/3934/RTf3e87c299ff23fc9f84d5528003290b2.jpg"
                } ,{
                    "code": "MAC",
                    "path": "erp/3934/MAC192910f2db9a59aaa0fcabfd386641ef.jpg"
                } ,{
                    "code": "MAC",
                    "path": "erp/3934/MAC21ad6330f80f9e5a9bf01296b30f8960.jpg"
                }, {
                    "code": "DC",
                    "path": "erp/3934/DC7c127c98a14fdb13dfdabaf596f67387.jpg"
                }, {
                    "code": "DC",
                    "path": "erp/3934/DC411fffa0b5eab2419d7043d4e6ae93c0.jpg"
                } ,{
                    "code": "HB",
                    "path": "erp/3934/HB8c2aa2b73f20c4530e60bba0ddf6d7d7.jpg"
                } ,{
                    "code": "HB",
                    "path": "erp/3934/HB6f793f9ae96614b7047dca6f21e6d828.jpg"
                } ,{
                    "code": "HB",
                    "path": "erp/3934/HB2b6af99368d89d4abddd5a39445cc139.jpg"
                } ,{
                    "code": "HB",
                    "path": "erp/3934/HBbc9345e7b2e873f1efd9501907fe1cb0.jpg"
                }, {
                    "code": "HB",
                    "path": "erp/3934/HBc6ff32c6ea3501fdac34630c5bac09e8.jpg"
                }, {
                    "code": "RHA",
                    "path": "erp/3934/RHA30d1cffac267fe5f375c71fd76651964.jpg"
                } ,{
                    "code": "RHA",
                    "path": "erp/3934/RHA12885d06bb3b0da492d3a6142c9c1e7a.jpg"
                }, {
                    "code": "RHA",
                    "path": "erp/3934/RHAdabd490aa72a9fce83129c7fe7d20bbc.jpg"
                } ,{
                    "code": "RHA",
                    "path": "erp/3934/RHA80c9b4f22047f587910e30dcf4f681ea.jpg"
                }],
                "os": "android",
                "paperList": [
                    "CPCH",
                    "CPT",
                    "SBHC",
                    "BL",
                    "SWP"
                ],
               " phone": "18583287560",
                "reqId": id,
                "step": 6,
                "taskId": taskId,
                "token": token

            }
            data = json.dumps(payload)
            response = requests.request("POST", url, data=data, headers=headers)
            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            print("主贷人:" + customer + "  征信后选填资料提交:" + response.text1["msg"])






# a=zhegnxinAC.zhenxinXuantian()