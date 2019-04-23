# -*- coding: UTF-8 -*-
import  MySQLdb
import rdexcel
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


def auto( type1):
    db = MySQLdb.connect("119.23.12.94", "root", "root", "worklist", charset='utf8')
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
        na1, type1)
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(type(results))
        # print((results))
        print(len(results))

        for row in results[0:1]:
            # print(row)
            # print(row[0])
            # print(row[1])

            id.append(row[0])
            taskId.append(row[2])
    print(taskId)
    db.close()
    return id, taskId
auto('车辆评估报告')