#!usr/bin/python
# coding=utf-8

import requests
class getimg(object):
    def __init__(self):
        for n in range(1,3):
            for m in  range(1,2):
                self.url="http://img.jojoft.com/"+str(n)+"/JOJO_00"+str(m)+".jpg"
                print(self.url)

    def getmg(self):
        ts=requests.get(self.url)
        print(ts.status_code)
        # print ts.iter_content(128)
        # for chunk in ts.iter_content(128):
        #     getimg.wirt(chunk)
        if  ts.status_code==404:
            print("error")
        else:
            with open('demo.jpg', 'wb') as fd:
                for chunk in ts:
                    fd.write(chunk)

    @staticmethod
    def wirt(t):
        with open('demo.jpg', 'wb') as fd:  # 若是'wb'就表示写二进制文件
            fd.write(t)
            fd.close()
        # with open('demo.jpg', 'wb') as fd:
        #     for chunk in ts:
        #         fd.write(chunk)

a=getimg()
a.getmg()