# -*- coding: cp936 -*-
import urllib
import urllib2
import  re
import  xlwt
import  xlrd

import random
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)



class GetIdNumber():

    @classmethod
    def Idnumber(self):
        url = "http://www.quanshuwang.com/book/0/269/32229420.html"
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        a=response.read()
        a=a.decode('gbk')
        # print(a)
        # print(type(a))

        # for i in range(1,10):
        #     a=random.randint(10,20)
        # #     print a
        # pattern = re.compile('\d+')
        # res = re.findall(pattern, a)
        # pattern = re.compile("&nbsp;&nbsp;&nbsp;&nbsp" +'.*? '+"<br />")
        reg=r'</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'
        reg = re.compile(reg,re.S)
        res=re.findall(reg,a)
        # res=res.replace('&nbsp;&nbsp;&nbsp;&nbsp;',"")
        # print(res)
        for i in res:
            i=i.replace('&nbsp;&nbsp;&nbsp;&nbsp;', "")
            i=i.replace('<br />', "")
            print(i)
        b=[]
        # for i in res:
        #     # print unicode(i, 'utf-8', 'ignore')
        #     a=unicode(i, 'utf-8', )
        #     a1=str(a)
        #     print(i)
        #     if len(a1)== 18:
        #         # print a1
        #         b.append(a1)
        #         tit='身份证号'
        #         f=open('{}.txt'.format(tit),'a')
        #         f.write(a1+'\n')
        #         f.close()
        #
        # if len(b):
        #     a = '爬取身份证号成功，请把身份证号输入基础数据中！'
        #     msg = a.decode('gbk')
        #     print(msg)
        # else:
        #     a = '爬取失败！'
        #     msg = a.decode('gbk')
        #     print(msg)
        #
a1=GetIdNumber.Idnumber()


