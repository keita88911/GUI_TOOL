import requests
import json
import sys


default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
s = requests.Session()
class test():
    @classmethod
    def ZhuHangSStoken(self):
        headers = {
                'Content-Type': "application/json",
            }
        url1 =  "http://ivt4.hschefu.com:9199/login"
        data1 = {"data": {"password": "12345678", "username": "18583287560"}}
        para1 = json.dumps(data1)
        r = s.post(url1, data=para1, headers=headers)
        token = r.cookies.items()[0][1]
        print(token)
        return (s)
# a=test.ZhuHangSStoken()
