# -*- coding: UTF-8 -*-
import sys
import json

import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')
# dict = {'主贷人姓名': '2341', '主贷人身份证': '9102', '所在节点': '3258', '审核状态': '3258', '审核人': '3258'}
#
# print( json.dumps(dict,encoding="UTF-8", ensure_ascii=False))
# print( json.dumps(dict,sort_keys=True, indent=1, separators=('', ': '),encoding="UTF-8", ensure_ascii=False))

class getsql():

    @classmethod
    def getsqldata(self,name):
        db = MySQLdb.connect("119.23.12.94", "root", "tm123456tm", "worklist", charset='utf8')
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        id = []
        taskId = []
        na1=name
        meeesage=[]
        sql = "SELECT a.customer_name,a.credential,b.segment_name,b.task_state,b.mater_audit_result, b.operator_name from loan_requests a,flow_run_task b WHERE a.credential='%s' and a.id=b.business_id" % na1
        cursor.execute(sql)
        results = cursor.fetchall()

        if not  results:

            a=u"暂无此人或者订单已完结"
            # print(a)
            return a

        # print(type(results))

        for row in (results):
            # meeesage.append(row)


            # for i in range(0,len(row)):
            #     meeesage.append(row[i])

            if row[3]==1:
                status ="已领取"
            elif row[3]==0:
                status = "未领取"
            elif row[3]==2:
                status = "已完成"
            if row[4]==0:
                meter_results="未办理"
            elif row[4]==1:
                meter_results = "办理通过"
            elif row[4]==2:
                meter_results = "有资料驳回"
            if not row[5]:
                results_name1 ="--"
                a = "主贷人姓名: " + str(row[0]) + " 主贷人身份证: " + str(row[1]) + " 所在节点: " + str(row[2]) + " 任务状态: " + status + " 审核结果: " + meter_results + " 审核人: " + results_name1

            else:
                a = "主贷人姓名: " + str(row[0]) + " 主贷人身份证: " + str(row[1]) + " 所在节点: " + str(row[2]) + " 任务状态: " + status + " 审核结果: " + meter_results + " 审核人: " + str(row[5])

            # print(a)
            meeesage.append(a)

        return meeesage


    @classmethod
    def getHistroy(self, name):
        db = MySQLdb.connect("119.23.12.94", "root", "tm123456tm", "worklist", charset='utf8')
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()

        na1 = name
        meeesage = []
        sql = "SELECT a.customer_name,a.credential,b.segment_name,b.task_state,b.result_name, b.operator_name from loan_requests a,flow_inst_task_history b WHERE a.credential='%s' and a.id=b.business_id" % na1
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        if not results:
            a1 = u"查无此人"
            # print("a:  " + a1)
            return a1

        # print(type(results))
        try:
            for row in (results):
                # meeesage.append(row)
                meter_results = str(row[4])
                if not row[4]:
                    meter_results = "--"+"          "
                    # print(type(row[4]))
                    # print(row[4])
                    # print(len(row[4]))


                elif len(row[4])<=4:
                    meter_results=str(row[4])+"        "
                # else :
                #     meter_results = str(row[4])
                #     continue
                # print len(row[2])
                if row == None:
                    print("row空")
                # for i in range(0,len(row)):
                #     meeesage.append(row[i])
                if row[3] == 1:
                    status = "已领取"
                elif row[3] == 0:
                    status = "未领取"
                elif row[3] == 2:
                    status = "已完成"
                if len(row[2])==2:
                    coner=str(row[2])+"                "
                elif   len(row[2])==4:
                    coner = str(row[2]) + "            "
                elif   len(row[2])==5:
                    coner = str(row[2]) + "             "
                elif   len(row[2])==7:
                    coner = str(row[2]) + "      "
                elif   len(row[2])==6:
                    coner = str(row[2]) + "        "
                else:
                    coner = str(row[2])
                # if row[4] == 0:
                #     meter_results = "未办理"
                # elif row[4] == 1:
                #     meter_results = "办理通过"
                # elif row[4] == 2:
                #     meter_results = "有资料驳回"
                if row[5] == None:
                    results_name1 = "--"
                    # meter_results = "--           "

                    # a1 = "主贷人姓名: " + str(row[0]) + " 主贷人身份证: " + str(row[1]) + " 所在节点: " + str(
                    #     row[2]) + "    任务状态: " + status + " 审核结果: " +meter_results + " 审核人: " + results_name1
                    a1 =  " 所在节点: " + coner + "             任务状态: " + status + " 审核结果: " +meter_results + "         审核人: " + results_name1
                else:
                    a1 = " 所在节点: " + coner + "             任务状态: " + status + " 审核结果: " + meter_results + "         审核人: " + row[5]
                # if a1 == None:
                #     a1 = "查无此人"
                meeesage.append(a1)
                # print(a1)
            # print(len(meeesage))
            # print str(meeesage).decode('string_escape')
            # print(meeesage)
            return meeesage
        except:
            a = u"查无此人"
            # print("a:  "+a)
            return meeesage
    # print(type(meeesage))
    # for i in range (0,len(meeesage)):
    #     # print(len(meeesage))
    #     for t in range(0,len(meeesage[i])):
    #         print(meeesage[i][t])
    # massege={'主贷人姓名': '2341', '主贷人身份证': '9102', '所在节点': '3258',"任务状态": '审核状态': '3258', '审核人': '3258'}

# a=getsql
# a.getsqldata(360100199702220867)