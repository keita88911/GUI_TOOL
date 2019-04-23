# -*- coding: UTF-8 -*-
import rdexcel
import MySQLdb
import sys
from sshtunnel import SSHTunnelForwarder
import mysql.connector

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class sql():
    # @classmethod
    # def get_unpublished_data(self):

        # server_id = 'rm-wz9bh90u5tsn9mi8c.mysql.rds.aliyuncs.com'  # 服务器地址我这是乱写的
        # ssh_password = 'FKxycWwVDirWD0II'
        # ssh_username = 'bigdata'
        #
        # with SSHTunnelForwarder((server_id, 22),ssh_password=ssh_password,ssh_username=ssh_username,remote_bind_address= ('127.0.0.1', 3306)) as server:  # 这里的地址是重新绑定的地址，我这里是自己的本地相当于localhost，端口默认；
        #
        #     # 上面相当于连接服务器，下面就是连接数据库，之后无论是pymysql还是其它的MySQLdb之类的都是一样使用；
        #     # 主要是数据库使用的是utf-8的编码格式，所以需要这句charset='utf8'注意是8而不是-8，如果在开通设置了sys编码，这里好像就不需要了
        #     db =mysql.connector.connect(host='120.77.44.64', port=5726, user='root', passwd='YfEueU#g6p$@6rVK',
        #                          db='worklist', charset='utf8')


    @classmethod
    def openDB(self):
        self.db = MySQLdb.connect("119.23.12.94", "root", "tm123456tm", "worklist", charset='utf8') #测试库

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
        # db.close()
        return self.db



    @classmethod
    def getsqldata(self):

        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        id = []
        taskId = []
        for i in range(0, len(listdata1)):
            na1 = listdata1[i]['loanerCardId']
            sql = "SELECT loan_requests.id,loan_requests.customer_name,flow_run_task.id FROM loan_requests,flow_run_task where loan_requests.credential='%s' and loan_requests.id=flow_run_task.business_id ORDER BY  flow_run_task.create_time deSC" % na1
            cursor.execute(sql)
            results = cursor.fetchall()
            # print type(results)
            # print( len(results))
            # print results
            # fields = cursor.description
            # workbook = xlwt.Workbook()
            # sheet = workbook.add_sheet('table_message',cell_overwrite_ok=True)
            # fname = []
            # print results
            for row in results[0:1]:
                # print(type(id))
                # row1=int(row[0])
                # print(row1)
                id.append(row[0])
                # customer_name = row[1]
                taskId.append(row[2])
                # print(type(id))
                # print len(id),
        # print("即将关闭数据库")
        # print(id,taskId)
        db.close()
        return id, taskId

    @classmethod
    def GetName(self):

        db = self.openDB()
        cursor = db.cursor()
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        customer_name1 = []
        for i in range(0, len(listdata1)):
            na1 = listdata1[i]['loanerCardId']
            sql = "select customer_name from loan_requests where credential='%s'ORDER BY create_time desc" % na1
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                # print(row[0])
                customer_name1.append(row[0])
                # print customer_name1[i]
        db.close()
        return customer_name1

    @classmethod
    def GetZhengxinID(self):

        db = self.openDB()
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        id = []
        taskId = []
        for i in range(0, len(listdata1)):
            na1 = listdata1[i]['loanerCardId']
            sql = "SELECT loan_requests.id,loan_requests.customer_name,flow_run_task.id FROM loan_requests,flow_run_task where loan_requests.credential='%s' and loan_requests.id=flow_run_task.business_id  and flow_run_task.segment_name='征信后补充资料'  ORDER BY  loan_requests.create_time DESC" % na1
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results[0:1]:
                id.append(row[0])
                taskId.append(row[2])
        db.close()
        return id, taskId

    @classmethod
    def GetCheJiaPingGuID(self):
        db = self.openDB()
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        id = []
        taskId = []
        for i in range(0, len(listdata1)):
            na1 = listdata1[i]['loanerCardId']
            sql = "SELECT loan_requests.id,loan_requests.customer_name,flow_run_task.id FROM loan_requests,flow_run_task where loan_requests.credential='%s' and loan_requests.id=flow_run_task.business_id  and flow_run_task.segment_name='真实车价评估'  ORDER BY  loan_requests.create_time DESC" % na1
            cursor.execute(sql)
            results = cursor.fetchall()
            # print type(results)
            # print( len(results))
            # print results
            # fields = cursor.description
            # workbook = xlwt.Workbook()
            # sheet = workbook.add_sheet('table_message',cell_overwrite_ok=True)
            # fname = []

            for row in results[0:1]:
                # print(type(id))
                # row1=int(row[0])
                # print(row1)
                id.append(row[0])
                # customer_name = row[1]
                taskId.append(row[2])
                # print(type(id))
                # print len(id),
        # print id
        # print taskId
        db.close()
        return id, taskId

    @classmethod
    def GetZhengxinReprot(self):

        db = self.openDB()
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        id = []
        process_Id = []
        for i in range(0, len(listdata1)):
            na1 = listdata1[i]['loanerCardId']
            sql = "SELECT loan_requests.id ,bank_credit_report.id as id2 FROM loan_requests,bank_credit_report WHERE loan_requests.credential='%s' and loan_requests.process_id=bank_credit_report.process_id ORDER BY   loan_requests.create_time desc" % na1
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results[0:1]:
                # print(type(id)
                row1 = int(row[0])
                id.append(row[0])
                # customer_name = row[1]
                process_Id.append(row[1])
                # print(type(id))
        db.close()
        return id, process_Id

    @classmethod
    def GetShenheHouBuChongID(self):

        db = self.openDB()
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        id = []
        taskId = []
        for i in range(0, len(listdata1)):
            na1 = listdata1[i]['loanerCardId']
            sql = "SELECT loan_requests.id,loan_requests.customer_name,flow_run_task.id FROM loan_requests,flow_run_task where loan_requests.credential='%s' and loan_requests.id=flow_run_task.business_id  and flow_run_task.segment_name='审核后补充资料'  ORDER BY  loan_requests.create_time DESC" % na1
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results[0:1]:
                id.append(row[0])
                taskId.append(row[2])
        db.close()
        return id, taskId

    @classmethod
    def GetZhiZhiZiLiaoID(self):
        db = self.openDB()
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        id = []
        taskId = []
        for i in range(0, len(listdata1)):
            na1 = listdata1[i]['loanerCardId']
            sql = "SELECT loan_requests.id,loan_requests.customer_name,flow_run_task.id FROM loan_requests,flow_run_task where loan_requests.credential='%s' and loan_requests.id=flow_run_task.business_id  and flow_run_task.segment_name='纸质资料确认'  ORDER BY  loan_requests.create_time DESC" % na1
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results[0:1]:
                id.append(row[0])
                taskId.append(row[2])
        db.close()
        return id, taskId

    @classmethod
    def GetCheLiangPingGuBaoGaoID(self):
        db = self.openDB()
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        id = []
        taskId = []
        for i in range(0, len(listdata1)):
            na1 = listdata1[i]['loanerCardId']
            sql = "SELECT loan_requests.id,loan_requests.customer_name,flow_run_task.id FROM loan_requests,flow_run_task where loan_requests.credential='%s' and loan_requests.id=flow_run_task.business_id  and flow_run_task.segment_name='车辆评估报告'  ORDER BY  loan_requests.create_time DESC" % na1
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results[0:1]:
                id.append(row[0])
                taskId.append(row[2])
        # print(taskId)
        db.close()
        return id, taskId

    @classmethod
    def ChuShenID(self):
        db = self.openDB()
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        id = []
        taskId = []
        for i in range(0, len(listdata1)):
            na1 = listdata1[i]['loanerCardId']
            sql = "SELECT loan_requests.id,loan_requests.customer_name,flow_run_task.id FROM loan_requests,flow_run_task where loan_requests.credential='%s' and loan_requests.id=flow_run_task.business_id  and flow_run_task.segment_name='初审'  ORDER BY  loan_requests.create_time DESC" % na1
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results[0:1]:
                id.append(row[0])
                taskId.append(row[2])
        # print(taskId)
        db.close()
        return id, taskId

    @classmethod
    def AddCaiWu(self):
        db = self.openDB()
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        id = []
        taskId = []
        for i in range(0, len(listdata1)):
            na1 = listdata1[i]['loanerCardId']
            sql = "SELECT loan_requests.id,loan_requests.customer_name,flow_run_task.id FROM loan_requests,flow_run_task where loan_requests.credential='%s' and loan_requests.id=flow_run_task.business_id  and flow_run_task.segment_name='添加财务信息'  ORDER BY  loan_requests.create_time DESC" % na1
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results[0:1]:
                id.append(row[0])
                taskId.append(row[2])
        # print(taskId)
        db.close()
        return id, taskId

    @classmethod
    def CaiWuSheHe(self):
        db = self.openDB()
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        id = []
        taskId = []
        for i in range(0, len(listdata1)):
            na1 = listdata1[i]['loanerCardId']
            sql = "SELECT loan_requests.id,loan_requests.customer_name,flow_run_task.id FROM loan_requests,flow_run_task where loan_requests.credential='%s' and loan_requests.id=flow_run_task.business_id  and flow_run_task.segment_name='财务审核'  ORDER BY  loan_requests.create_time DESC" % na1
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results[0:1]:
                id.append(row[0])
                taskId.append(row[2])
        # print(taskId)
        db.close()
        return id, taskId

    @classmethod
    def ChuNaDianKuan(self):
        db = self.openDB()
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        id = []
        taskId = []
        for i in range(0, len(listdata1)):
            na1 = listdata1[i]['loanerCardId']
            sql = "SELECT loan_requests.id,loan_requests.customer_name,flow_run_task.id FROM loan_requests,flow_run_task where loan_requests.credential='%s' and loan_requests.id=flow_run_task.business_id  and flow_run_task.segment_name='出纳垫款'  ORDER BY  loan_requests.create_time DESC" % na1
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results[0:1]:
                id.append(row[0])
                taskId.append(row[2])
        # print(taskId)
        db.close()
        return id, taskId

    @classmethod
    def auto(self, type):
        db = self.openDB()
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        # print(type)
        cursor = db.cursor()
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        id = []
        taskId = []
        for i in range(0, len(listdata1)):
            na1 = listdata1[i]['loanerCardId']
            sql = "SELECT loan_requests.id,loan_requests.customer_name,flow_run_task.id FROM loan_requests,flow_run_task where loan_requests.credential='%s' and loan_requests.id=flow_run_task.business_id  and flow_run_task.segment_name='%s'  ORDER BY  loan_requests.create_time DESC" % (
                na1, type)
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results[0:1]:
                id.append(row[0])
                taskId.append(row[2])
        # print(taskId)
        db.close()
        return id, taskId

    @classmethod
    def StartZhengXin(self):
        db = self.openDB()
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        id = []
        taskId = []
        for i in range(0, len(listdata1)):
            na1 = listdata1[i]['loanerCardId']
            sql = "SELECT a.id  from loan_requests a,flow_instance b where a.id=b.business_id and a.credential='%s' and b.flow_state ='2'  " % na1
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results[0:1]:
                id.append(row[0])

        # print(process_id)
        db.close()
        return id

    @classmethod
    def Province(self):
        db = self.openDB()
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_bysheet("add1.xlsx", 0, 0)
        hasprovince = []
        sqldata = []
        for i in range(0, len(listdata1)):
            AppUsername = listdata1[i]['AppUsername']
            sql = "SELECT id,parent_id,general_manager_id,type,level from department where id=(SELECT department_id FROM `user` WHERE username='%s')" % AppUsername
            cursor.execute(sql)
            results = cursor.fetchall()
            # print(results)
            for row in results:
                departmentid = row[1]
                if row[3] == 3:
                    # print("省区经理即将审核")
                    return True
                if row[1]:
                    for levels in range(int(row[4]), 0, -1):
                        # print(levels)

                        # results1 = cursor.execute("SELECT id,parent_id,general_manager_id,type,level from department where id=row[1]").fetchall()
                        sql1 = "SELECT id,parent_id,general_manager_id,type,level from department where id='%s'" % departmentid

                        cursor.execute(sql1)
                        results1 = cursor.fetchall()
                        # print(list(results1))
                        # print(list(results1)[0])
                        if int(list(results1)[0][3]) == 3:
                            # print("省区经理即将审核")
                            return True
                        elif int(list(results1)[0][1]) == 0:
                            # print("此业务员所在地区不存在省区经理,即将跳过此节点")
                            return False
                        departmentid = list(results1)[0][1]
                else:
                    # print("此业务员所在地区不存在省区经理，即将跳过此节点")
                    return False
                    # if row[3]==3:
                    #     return False

        # print(sqldata)
        db.close()
        return id

    '''快贷修改第三方征信'''
    @classmethod
    def updata_zhengxin(self):
        db = self.openDB()
        cursor = db.cursor()
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)

        for i in range(0, len(listdata1)):
            if  listdata1[i]['fast_loan']=="1":
                na1 = listdata1[i]['loanerCardId']
                sql = "UPDATE loan_requests SET process_id = '189764' where credential= '%s'" % na1
                cursor.execute(sql)
                cursor.connection.commit()
                # print(listdata1[i]['fast_loan'])
        # print("即将关闭数据库")
        db.close()
        return True
# a = sql.getsqldata()
# b=sql.auto("省区经理审核")
# a=sql.openDB()