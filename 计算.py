# -*- coding: UTF-8 -*-
import rdexcel
import MySQLdb
import sys
import pymysql
from sshtunnel import SSHTunnelForwarder
import mysql.connector

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


# @classmethod
# def openDB(self):
    # self.db = MySQLdb.connect("119.23.12.94", "root", "tm123456tm", "worklist", charset='utf8')  # 测试库

    # with SSHTunnelForwarder(
    #         ('rm-wz9bh90u5tsn9mi8c.mysql.rds.aliyuncs.com', int(3306)),  # 跳板机的配置
    #         ssh_password= 'Uw0Gzh$@KHCnUWfoe',
    #         ssh_username= 'prod_worklist',
    #         remote_bind_address=('120.77.44.64', int(5726))) as server:  # MySQL服务器的配置
    #     conn = MySQLdb.connect(host='127.0.0.1', port=server.local_bind_port, user='root', passwd='YfEueU#g6p$@6rVK',
    #                            database='worklist')

    # server_id = ('rm-wz9bh90u5tsn9mi8c.mysql.rds.aliyuncs.com')  # 服务器地址我这是乱写的
    # ssh_password = 'Uw0Gzh$@KHCnUWfoe'
    # ssh_username = 'prod_worklist'
    #
    # with SSHTunnelForwarder((server_id, 5726), ssh_password=ssh_password, ssh_username=ssh_username,
    #                         remote_bind_address=(
    #                         'rm-wz9bh90u5tsn9mi8c.mysql.rds.aliyuncs.com', 3306)) as server:  # 这里的地址是重新绑定的地址，我这里是自己的本地相当于localhost，端口默认；
    #
    #     # 上面相当于连接服务器，下面就是连接数据库，之后无论是pymysql还是其它的MySQLdb之类的都是一样使用；
    #     # 主要是数据库使用的是utf-8的编码格式，所以需要这句charset='utf8'注意是8而不是-8，如果在开通设置了sys编码，这里好像就不需要了

    # with SSHTunnelForwarder(
    #         ('39.108.250.129', 5726),  # 跳板机的配置
    #      ssh_password='^0OumKsU&rrhf#KJC',
    #      ssh_username='root',
    #      remote_bind_address=('rm-wz9bh90u5tsn9mi8c.mysql.rds.aliyuncs.com', 3306)) as server:  # MySQL服务器的配置
    #      db =MySQLdb.connect(host='127.0.0.1', port=server.local_bind_port, user='prod_worklist',
    #                                passwd='Uw0Gzh$@KHCnUWfoe', db='worklist')
    #
    #     # self.db = MySQLdb.connect(host='127.0.0.1', port=conn.local_bind_port, user='root', passwd='YfEueU#g6p$@6rVK',
    #     #                      db='worklist', charset='utf8')
    # # server.start()
    # print(db)
    # cursor = db.cursor()
    # sql = "SELECT * from `user` where name='18583287565'"
    # # print(sql)
    # cursor.execute(sql)
    # results = cursor.fetchall()
#
#     #
#     # db.close()
#
#
#     # return self.db
# if __name__ == "__main__":
#     # 跳板机SSH连接
#     with SSHTunnelForwarder(
#             ('120.77.44.64', 5726),
#             ssh_username="root",
#             ssh_password="YfEueU#g6p$@6rVK",
#             remote_bind_address=('wz9bh90u5tsn9mi8c.mysql.rds.aliyuncs.com', 3306)
#     ) as tunnel:
#         # 数据库连接配置，host默认127.0.0.1不用修改
#         conn = pymysql.connect(
#             host='127.0.0.1',
#             port=tunnel.local_bind_port,
#             user='prod_worklist',
#             password='Uw0Gzh$@KHCnUWfoe',
#             db='worklist',
#             charset='utf8',
#             cursorclass=pymysql.cursors.DictCursor
#         )
#         # 获取游标
#         cursor = conn.cursor(cursor=MySQLdb.cursors.DictCursor)
#         # 查询数据库，查询一条数据，其他CURD操作类似
#         sql = "SELECT * FROM `user` "
#         # prams = ('1',)
#         cursor.execute(sql )
#         info = cursor.fetchone()
#         print(info)
#         # 关闭连接
#         cursor.close()
#         conn.close()
#         #
#         # cursor = conn.cursor()
#         # sql = "SELECT * from `user` where name='18583287565'"
#         # # print(sql)
#         # cursor.execute(sql)
#         # results = cursor.fetchall()


# -*- coding: utf-8 -*-

import MySQLdb
import os, sys
from sshtunnel import SSHTunnelForwarder


def mysql_test():
    with SSHTunnelForwarder(  # ssh的地址，端口，用户名，密码
            ('39.108.250.129', 5726),
            # ssh_pkey="秘钥文件",
            ssh_password="YfEueU#g6p$@6rVK",
            ssh_username="root",
            remote_bind_address=('wz9bh90u5tsn9mi8c.mysql.rds.aliyuncs.com', 3306),
            local_bind_address=('0.0.0.0', 3306)) as server:
        server.start()

        # print(server)
        conn = MySQLdb.connect(host='127.0.0.1',
                               port=3306,
                               user='prod_worklist',
                               passwd='Uw0Gzh$@KHCnUWfoe',
                               db='worklist',
                               charset='utf8')
        cursor = conn.cursor()  # .cursor()用来获得python执行Mysql命令的方法
        # select = sql
        sql = "SELECT * from `user`"
        cursor.execute(sql)  # .execute()执行mysql语句
        data = cursor.fetchall()  # fetchall()则是接收全部的返回结果行
        print data
        server.stop()
    return data


pass

if __name__ == "__main__":
    mysql_test()