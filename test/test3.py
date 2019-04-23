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
        a=a.decode('utf-8')
        # print a
        # print(a)

        # for i in range(1,10):
        #     a=random.randint(10,20)
        #     print a
        # pattern = re.compile(r'\d+')
        #
        # res = re.findall(pattern, a)
        reg=r'<tr><td>(.*?)</td><td>'
        reg = re.compile(reg,re.S)
        # reg1=re.compile(r'\d+')
        res=re.findall(reg,a)
        # print(res)
        # res=unichr(res)
        # print(type(res[1]))
        for i in res:
            print(i)
            tit='姓名+身份证'
            f=open('{}.txt'.format(tit),'a')
            f.write(i+'\n')
            f.close()
        # res=str(res)
        # res=unicode(res, 'utf-8', 'ignore')
        # print(res)
        # print(type(res))
        # name=u"[\u4e00-\u9fa5]+"
        # name=re.compile(name,re.S)
        # res1=re.findall(name,res)
        # reg1=re.compile(r'\d+')
        # res1=re.findall(reg1,res)
        b=[]
        # print(res1)
        # # # print(res[2])
        # #
        # for i in res:
        #     name=u"[\u4e00-\u9fa5]+"
        #     name=re.compile(name,re.S)
        #     res1=re.findall(name,i)
        #     case_list_righ = str(res1).replace('u\'', '\'')
        #     # print case_list_righ.decode("unicode-escape")
        #     # b=unicode(case_list_righ, 'utf-8', 'ignore')
        #     a1=case_list_righ.decode("unicode-escape")     # list转换中文
        #     # print(a1)
        #     a1 = a1.replace("['", "")
        #     a1 = a1.replace("']", "")
        #     # print(a1)
        #     tit='姓名'
        #     f=open('{}.txt'.format(tit),'a')
        #     f.write(a1+'\n')
        #     f.close()


        # for i in res:
        #     # print unicode(i, 'utf-8', 'ignore')
        #     a=unicode(i, 'utf-8', 'ignore')
        #     a1=str(a)
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

da=GetIdNumber.Idnumber()


