#!/usr/bin/python
# -*- coding: UTF-8 -*-
import  re
from os import path
import  os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import  sys
import time
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

def findnewest(test_report):
    lists2=[]
    lists = os.listdir(test_report)                                    #列出目录的下所有文件和文件夹保存到lists
    for i in   range(0,len(lists)):
        p=re.compile(r'(.*?.html)')                                    #获取当前最新的html
        if  p.findall(lists[i]):
            para=p.findall(lists[i])
            lists2.append(para[0])
    # print(lists)
    # print(lists2)
    lists2.sort(key=lambda fn:os.path.getmtime(test_report + "\\" + fn))#按时间排序
    # print(lists.sort(key=lambda fn:os.path.getmtime(test_report + "\\" + fn)))
    file_new = os.path.join(test_report,lists2[-1])                     #获取最新的文件保存到file_new
    print(file_new)
    return file_new

def sendmail():
    # 第三方 SMTP 服务
    mail_host="smtp.qq.com"  #设置服务器
    mail_user="412607699@qq.com"   #用户名
    mail_pass="jknliplqwkixcbbd"   #口令

    sender = '412607699@qq.com'
    receivers = ['654995076@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("测试组", 'utf-8')#发件人
    message['To'] = Header("接收人", 'utf-8')#收件人
    subject = 'OA接口测试报告' #邮件title
    message['Subject'] = Header(subject, 'utf-8')

    # 格式化成2016-03-20 11:45:39形式
    times=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 邮件正文内容
    message.attach(MIMEText(times+ '  OA测试报告结果见附件', 'plain', 'utf-8'))#正文

    # 构造附件1，传送当前目录下的 test.txt 文件

    # 20180907160553.html
    att1 = MIMEText(open("20180907172851.html", 'rb').read(), _subtype='html', _charset='utf-8')
    # att1 = MIMEText(open("姓名.txt".decode(), 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'

    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test.html"'
    message.attach(att1)

    # 构造附件2，传送当前目录下的 runoob.txt 文件
    # att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
    # message.attach(att2)

    try:
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(mail_host, 465)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers,
        message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"



test_report = path.dirname(__file__)
# test_report="\\test"
a=findnewest(test_report)
b=sendmail()

