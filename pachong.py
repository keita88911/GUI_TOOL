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
        url = "http://sfz.ckd.cc/"
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        a=response.read()
        # print a
        # print(type(a))

        # for i in range(1,10):
        #     a=random.randint(10,20)
        #     print a
        pattern = re.compile(r'\d+')
        res = re.findall(pattern, a)
        b=[]
        for i in res:
            # print unicode(i, 'utf-8', 'ignore')
            a=unicode(i, 'utf-8', 'ignore')
            a1=str(a)
            if len(a1)== 18:
                # print a1
                b.append(a1)
                tit='身份证号'
                f=open('{}.txt'.format(tit),'a')
                f.write(a1+'\n')
                f.close()

        if len(b):
            a = '爬取身份证号成功，请打开根目录txt把身份证号输入到基础数据中！'
            msg = a.decode('gbk')
            print(msg)
        else:
            a = '爬取失败！'
            msg = a.decode('gbk')
            print(msg)

# for i in range(0,100):
#
#     a=GetIdNumber.Idnumber()
#

