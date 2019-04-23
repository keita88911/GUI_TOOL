# -*- coding: UTF-8 -*-
import datetime
import MySQLdb
import sys

import time

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class sql():
    @classmethod
    def openDB(self):
        self.db = MySQLdb.connect("119.23.12.94", "root", "tm123456tm", "testData", charset='utf8')
        return self.db

    # 登录
    @classmethod
    def getsqldata(self):
        tt = time.time()
        db = self.openDB()
        cursor = db.cursor()
        id = []
        taskId = []


        sql = "SELECT * FROM test_tree "
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    @classmethod
    def digui(self):
        results=self.getsqldata()

        data={}
        num=0
        qiepian=0
        print(results)
        for cow in results:
            department = []
            num=num+1
            # print(cow)
            if len(cow[2]) == 2:
                father_one = cow[2]
                print(father_one)
                department.append(father_one)
                for father in  results:
                    # qiepian=qiepian+2
                    if father[2][:2]==cow[2]:
                        # print(father)
                        # print father[2][-2:]
                        department.append(father)
                        data[num]=department

        print(str(data).replace('u\'','\'') .decode("unicode-escape"))
a=sql.digui()
# a="0201"
#
# print(a[:2] )