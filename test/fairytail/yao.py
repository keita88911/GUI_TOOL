#!usr/bin/python
# coding=utf-8

import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class getimg(object):



    def getmg(self):

        for n in range(0,545):
            for t in range(0, 2):
                for i in range(0,2):
                    for m in range(0, 10):
                        # http://img.jojoft.com/532/JOJO_002-003.jpg
                        m1=m+1
                        url1="http://img.jojoft.com/"+str(n)+"/JOJO_"+str(t)+str(i)+str(m)+".jpg"
                        url2="http://img.jojoft.com/"+str(n)+"/JOJO_"+str(t)+str(i)+str(m)+"-"+str(t)+str(i)+str(m1)+".jpg"
                        url3="http://img.jojoft.com/"+str(n)+"/JOJO_"+str(t)+str(i)+str(m)+".png"
                        url4="http://img.jojoft.com/"+str(n)+"/JOJO_"+str(t)+str(i)+str(m)+"-"+str(t)+str(i)+str(m1)+".png"

                        print(url1)
                        header={'Content-Type':'image/jpeg'}
                        ts=requests.get(url1,headers=header)
                        ts2=requests.get(url2,headers=header)
                        ts3=requests.get(url3,headers=header)
                        ts4=requests.get(url4,headers=header)

                        print(ts.status_code)
                        # print ts.iter_content(128)
                        # for chunk in ts.iter_content(128):
                        #     getimg.wirt(chunk)
                        if  ts.status_code==200:
                            a="第"+str(n)+"话"+str(t)+str(i)+str(m)+"页"+".jpg"
                            print(a)
                            with open(a.decode(), 'wb') as fd:
                                for chunk in ts:
                                    fd.write(chunk)
                        elif ts2.status_code==200:
                            a="第"+str(n)+"话"+str(t)+str(i)+str(m)+"-"+str(t)+str(i)+str(m1)+"页"+".jpg"
                            print(a)
                            with open(a.decode(), 'wb') as fd:
                                for chunk in ts:
                                    fd.write(chunk)
                        elif ts3.status_code==200:
                            a="第"+str(n)+"话"+str(t)+str(i)+str(m)+"页"+".png"
                            print(a)
                            with open(a.decode(), 'wb') as fd:
                                for chunk in ts:
                                    fd.write(chunk)
                        elif ts4.status_code==200:
                            a = "第" + str(n) + "话" + str(t) + str(i) + str(m) + "-" + str(t) + str(i) + str(
                                m1) + "页" + ".png"
                            print(a)
                            with open(a.decode(), 'wb') as fd:
                                for chunk in ts:
                                    fd.write(chunk)

                        else:
                            # a = "第" + str(n) + "话" + str(t) + str(i) +  + "0页" + ".jpg"
                            # print(a)
                            # with open(a.decode(), 'wb') as fd:
                            #     for chunk in ts:
                            #         fd.write(chunk)
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue


    @staticmethod
    def wirt(t):
        with open('demo.jpg', 'wb') as fd:
            fd.write(t)
            fd.close()
        # with open('demo.jpg', 'wb') as fd:
        #     for chunk in ts:
        #         fd.write(chunk)

a=getimg()
a.getmg()