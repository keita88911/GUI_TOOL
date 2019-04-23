# -*- coding: UTF-8 -*-
from Tkinter import *
from tkMessageBox import *
import tkFileDialog
from start import *
import createTD
import test11
import pachong
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from tkinter import messagebox as mBox
from StartTiE import *
from AddCaiWu import *
from CaiWuShenHe import *
from ChuNaDianKuan import *
from Start2 import *
from TiE import *
from CheLiangBuChongBaoGao import *
from DaiHuiKuan import *
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from tkinter import messagebox as mBox
from search import getsql
from Province import Province

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
win = tk.Tk()

# Add a title
win.title("Python 图形用户界面")

# Disable resizing the GUI
win.resizable(0, 0)

win.title("惠商车服软件部内部工具for erp  v9.0")
# tk.geometry("530x900+0+0")
lab = Menubutton(win, text="从excel批量创建订单")
Label(win, text="测试部工具", bg='#FFFF00', font=("Arial", 15)).pack()

win.resizable(0, 0)
tabControl = ttk.Notebook(win)  # Create Tab Control

aff = ttk.Frame(tabControl)  # Create a tab
tabControl.add(aff, text='不提额流程', sticky=S + N, )  # Add the tab

tab2 = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(tab2, text='审核员提额流程', )  # Make second tab visible

tab3 = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(tab3, text='单独流程节点审核', )  # Make second tab visible

tab4 = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(tab4, text='查询当前订单流程', )  # Make second tab visible

# tab3 = ttk.Frame(tabControl)  # Add a third tab
# tabControl.add(tab3, text='第三页')  # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible
monty = ttk.LabelFrame(aff,
                       text='=========================================================我是华丽的分割线===========================================================')
monty.grid(column=90, row=0, padx=8, pady=2)

# ttk.Label(monty, text="我是分隔符").grid(column=1, row=0, sticky='W',ipadx=1)
action = ttk.Button(monty, text="爬虫获取身份证", width=30, command=pachong.GetIdNumber.Idnumber)
action.grid(column=2, row=1, ipady=7, ipadx=470, columnspan=100, sticky=W)
action2 = ttk.Button(monty, text="填写基础数据", width=30, command=test11.open.openexcel)
action2.grid(column=2, row=2, ipady=7, ipadx=470, columnspan=100, sticky=W)
action3 = ttk.Button(monty, text="新建订单至达驻行节点", width=30, command=GettoNode.GettoZhuhang)
action3.grid(column=2, row=3, ipady=7, ipadx=470, columnspan=100, sticky=W)
action3 = ttk.Button(monty, text="新建订单至达电审节点", width=30, command=GettoNode.GettoDianshen)
action3.grid(column=2, row=4, ipady=7, ipadx=355, columnspan=100, sticky=W)
action4 = ttk.Button(monty, text="新建订单至车价评估节点", width=30, command=GettoNode.GettoChejia)
action4.grid(column=2, row=5, ipady=7, ipadx=355, columnspan=100, sticky=W)
action5 = ttk.Button(monty, text="新建订单至初审", width=30, command=GettoNode.GettChuShen)
action5.grid(column=2, row=6, ipady=7, ipadx=355, columnspan=100, sticky=W)
action5 = ttk.Button(monty, text="新建订单至省区经理", width=30, command=GettoNode.GettoProvince)
action5.grid(column=2, row=7, ipady=7, ipadx=355, columnspan=100, sticky=W)
action6 = ttk.Button(monty, text="新建订单至审核主管", width=30, command=GettoNode.GettoShenheZhuGuan)
action6.grid(column=2, row=8, ipady=7, ipadx=355, columnspan=100, sticky=W)
action7 = ttk.Button(monty, text="新建订单至审核经理", width=30, command=GettoNode.GetttoShenheJingLi)
action7.grid(column=2, row=9, ipady=7, ipadx=355, columnspan=100, sticky=W)
action8 = ttk.Button(monty, text="新建订单至审核总经理", width=30, command=GettoNode.GettoShenheZongJingLing)
action8.grid(column=2, row=10, ipady=7, ipadx=355, columnspan=100, sticky=W)

action10 = ttk.Button(monty, text="通过征信后补充", width=30, command=GettoNode.GettZhenxinBuchong)
action10.grid(column=7, row=4, rowspan=8, ipady=150, ipadx=5, columnspan=150, sticky=E)
action11 = ttk.Button(monty, text="新建订单至车图GPS", width=30, command=GettoNode.GettoCheTuGPS)
action11.grid(column=6, row=12, ipady=7, ipadx=120, columnspan=100, sticky=W)
action9 = ttk.Button(monty, text="新建订单至补充信息审核后", width=30, command=GettoNode.GettoBuChongXinXi)
action9.grid(column=4, row=11, ipady=7, ipadx=135, columnspan=100, sticky=W)
action12 = ttk.Button(monty, text="新建订单至车辆评估报告", width=30, command=GettoNode.GettoCheLiangPingGuBaoGao)
action12.grid(column=2, row=11, ipady=7, ipadx=111, columnspan=100, sticky=W)
action13 = ttk.Button(monty, text="通过添加财务", width=30, command=AddCaiWu.AddCaiWu)
action13.grid(column=4, row=12, rowspan=1, ipady=7, ipadx=20, sticky=W)
action18 = ttk.Button(monty, text="通过财务审核", width=30, command=CaiWuShenHe.CaiWuShenHe)
action18.grid(column=4, row=13, rowspan=1, ipady=7, ipadx=250, columnspan=100, sticky=W)
action19 = ttk.Button(monty, text="通过出纳垫款", width=30, command=ChuNaDianKuan.ChuNaDianKuan)
action19.grid(column=4, row=14, rowspan=1, ipady=7, ipadx=250, columnspan=100, sticky=W)
action19 = ttk.Button(monty, text="通过待回款", width=30, command=DaiHuiKuan.daihuikuan)
action19.grid(column=4, row=15, ipady=48, ipadx=250, rowspan=7, columnspan=100, sticky=W)

action20 = ttk.Button(monty, text="新建订单至纸质资料", width=30, command=GettoNode.ZhiZhiZiLiao)
action20.grid(column=3, row=12, rowspan=1, ipady=7, padx=0, sticky=N)
action14 = ttk.Button(monty, text="新建订单至抄单", width=30, command=GettoNode.GettoChaoDan)
action14.grid(column=3, row=13, ipady=7, padx=0, sticky=W)
action14 = ttk.Button(monty, text="通过车辆报告补充", width=30, command=CheLiangBuChong.CheLiangBuChong)
action14.grid(column=2, row=12, ipady=110, ipadx=0, rowspan=7, sticky=W)
action15 = ttk.Button(monty, text="新建订单至抄单内勤", width=30, command=GettoNode.GettoChaoDanNeiQin)
action15.grid(column=3, row=14, ipady=7, padx=0, sticky=W)
action16 = ttk.Button(monty, text="新建订单至开卡", width=30, command=GettoNode.GettoKaika)
action16.grid(column=3, row=15, ipady=7, padx=0, sticky=W)
action17 = ttk.Button(monty, text="新建订单至驻行送审", width=30, command=GettoNode.GettoZhuHangSongShen)
action17.grid(column=3, row=16, ipady=7, padx=0, sticky=W)
action18 = ttk.Button(monty, text="完成后补充信息", width=30, command=GettoNode.GettoWanCheng)
action18.grid(column=3, row=17, ipady=7, padx=0, sticky=W)

# ==================================================    提额页   ==================================================================
tabControl.pack(expand=1, fill="both")  # Pack to make visible
monty = ttk.LabelFrame(tab2, text='====================我是华丽的分割线====================')
monty.grid(column=0, row=2, padx=8, pady=4)

# ttk.Label(monty, text="我是分隔符").grid(column=1, row=0, sticky='W',ipadx=1)
action = ttk.Button(monty, text="爬虫获取身份证", width=30, command=pachong.GetIdNumber.Idnumber)
action.grid(column=2, row=1, ipady=7, ipadx=120, columnspan=100, sticky=N)
action2 = ttk.Button(monty, text="填写基础数据", width=30, command=test11.open.openexcel)
action2.grid(column=2, row=2, ipady=7, ipadx=120, columnspan=100, sticky=N)
action3 = ttk.Button(monty, text="新建订单至达驻行节点", width=30, command=GettoNode.GettoZhuhang)
action3.grid(column=2, row=3, ipady=7, ipadx=0, sticky=N)
action3 = ttk.Button(monty, text="新建订单至达电审节点", width=30, command=GettoNode.GettoDianshen)
action3.grid(column=2, row=4, ipady=7, padx=0, sticky=N)
action4 = ttk.Button(monty, text="新建订单至车价评估节点", width=30, command=GettoNode.GettoChejia)
action4.grid(column=2, row=5, ipady=7, padx=0, sticky=N)
action5 = ttk.Button(monty, text="新建订单至初审", width=30, command=GettoNode.GettChuShen)
action5.grid(column=2, row=6, ipady=7, padx=0, sticky=N)

# action8 = ttk.Button(monty, text="新建订单至审核总经理", width = 30, command=GettoNode1.GettoShenheZongJingLing)
# action8.grid(column=2, row=16,ipady=7,ipadx=110, columnspan =100,sticky =N)
action9 = ttk.Button(monty, text="新建订单至补充信息审核后", width=30, command=GettoNode1.GettoBuChongXinXi1)
action9.grid(column=2, row=7, ipady=7, padx=0, sticky=N)
action10 = ttk.Button(monty, text="通过征信后补充", width=30, command=GettoNode1.GettZhenxinBuchong1)
action10.grid(column=3, row=3, rowspan=5, ipady=90, padx=0, ipadx=10, sticky=W)
action11 = ttk.Button(monty, text="新建订单至车图GPS", width=30, command=GettoNode1.GettoCheTuGPS1)
action11.grid(column=2, row=8, ipady=7, padx=0, sticky=N)
action12 = ttk.Button(monty, text="新建订单至车辆评估报告", width=30, command=GettoNode1.GettoCheLiangPingGuBaoGao1)
action12.grid(column=2, row=9, ipady=7, padx=0, sticky=N)
action13 = ttk.Button(monty, text="通过纸质资料", width=30, command=GettoNode1.ZhiZhiZiLiao1)
action13.grid(column=3, row=7, rowspan=4, ipady=30, padx=0, ipadx=10, sticky=W)
action14 = ttk.Button(monty, text="新建订单至抄单", width=30, command=GettoNode1.GettoChaoDan1)
action14.grid(column=2, row=10, ipady=7, ipadx=120, columnspan=100, sticky=N)
action15 = ttk.Button(monty, text="新建订单至抄单内勤", width=30, command=GettoNode1.GettoChaoDanNeiQin1)
action15.grid(column=2, row=11, ipady=7, ipadx=120, columnspan=100, sticky=N)
action16 = ttk.Button(monty, text="新建订单至开卡", width=30, command=GettoNode1.GettoKaika1)
action16.grid(column=2, row=12, ipady=7, ipadx=120, columnspan=100, sticky=N)
action17 = ttk.Button(monty, text="新建订单至驻行送审", width=30, command=GettoNode1.GettoZhuHangSongShen1)
action17.grid(column=2, row=13, ipady=7, ipadx=120, columnspan=100, sticky=N)
action8 = ttk.Button(monty, text="新建订单至添加财务信息", width=30, command=GettoNode1.GetttoAddCaiWu)
action8.grid(column=2, row=17, ipady=7, ipadx=120, columnspan=100, sticky=N)
action8 = ttk.Button(monty, text="新建订单至财务审核", width=30, command=GettoNode1.GetttoCaiWuShenHe)
action8.grid(column=2, row=18, ipady=7, ipadx=120, columnspan=100, sticky=N)
action8 = ttk.Button(monty, text="新建订单至出纳垫款", width=30, command=GettoNode1.GetttoChuNaiDianKuan)
action8.grid(column=2, row=19, ipady=7, ipadx=120, columnspan=100, sticky=N)
action6 = ttk.Button(monty, text="新建订单至审核主管", width=30, command=GettoNode1.GettoShenheZhuGuan1)
action6.grid(column=2, row=14, ipady=7, ipadx=120, columnspan=100, sticky=N)
action7 = ttk.Button(monty, text="新建订单至审核经理", width=30, command=GettoNode1.GetttoShenheJingLi1)
action7.grid(column=2, row=15, ipady=7, ipadx=120, columnspan=100, sticky=N)
action18 = ttk.Button(monty, text="完成后补充信息", width=30, command=GettoNode1.GetttoWanCheng)
action18.grid(column=2, row=20, ipady=7, ipadx=120, columnspan=100, sticky=N)

# ==================================================    单独审核节点   ==================================================================

monty = ttk.LabelFrame(tab3, text='====================我是华丽的分割线====================')
monty.grid(column=90, row=0, padx=8, pady=2)

# ttk.Label(monty, text="我是分隔符").grid(column=1, row=0, sticky='W',ipadx=1)
action = ttk.Button(monty, text="爬虫获取身份证", width=30, command=pachong.GetIdNumber.Idnumber)
action.grid(column=2, row=1, ipady=7, ipadx=120, columnspan=100, sticky=N)
action2 = ttk.Button(monty, text="填写基础数据", width=30, command=test11.open.openexcel)
action2.grid(column=2, row=2, ipady=7, ipadx=120, columnspan=100, sticky=N)
action3 = ttk.Button(monty, text="驻行节点", width=30, command=toNode.zhuhangSS)
action3.grid(column=2, row=3, ipady=7, ipadx=0, sticky=N)
action3 = ttk.Button(monty, text="电审节点", width=30, command=toNode.dianSS)
action3.grid(column=2, row=4, ipady=7, padx=0, sticky=N)
action4 = ttk.Button(monty, text="车价评估节点", width=30, command=toNode.chejiaPG)
action4.grid(column=2, row=5, ipady=7, padx=0, sticky=N)
action5 = ttk.Button(monty, text="初审", width=30, command=toNode.chushen)
action5.grid(column=2, row=6, ipady=7, padx=0, sticky=N)
action6 = ttk.Button(monty, text="审核主管", width=30, command=toNode.ShenheZG)
action6.grid(column=2, row=7, ipady=7, padx=0, sticky=N)
action7 = ttk.Button(monty, text="审核经理", width=30, command=toNode.ShenheJL)
action7.grid(column=2, row=8, ipady=7, padx=0, sticky=N)
action8 = ttk.Button(monty, text="审核总经理", width=30, command=toNode.ShenheZongJL)
action8.grid(column=2, row=9, ipady=7, padx=0, sticky=N)
action9 = ttk.Button(monty, text="补充信息审核后", width=30, command=toNode.ShenHehou)
action9.grid(column=2, row=10, ipady=7, padx=0, sticky=N)
action10 = ttk.Button(monty, text="征信后补充", width=30, command=GettoNode.GettZhenxinBuchong)
action10.grid(column=3, row=3, rowspan=7, ipady=130, padx=0, ipadx=10, sticky=W)
action11 = ttk.Button(monty, text="车图GPS", width=30, command=toNode.GPS)
action11.grid(column=2, row=11, ipady=7, padx=0, sticky=N)
action12 = ttk.Button(monty, text="车辆评估报告", width=30, command=toNode.CheLiangPingGuBG)
action12.grid(column=2, row=12, ipady=7, padx=0, sticky=N)
# action13 = ttk.Button(monty, text="通过纸质资料", width = 30, command=GettoNode.ZhiZhiZiLiao)
# action13.grid(column=3, row=8,rowspan=7, ipady=70,padx= 0,ipadx=10,sticky =W)
action13 = ttk.Button(monty, text="添加财务", width=30, command=toNode.AddCaiWu)
action13.grid(column=3, row=9, rowspan=1, ipady=7, padx=0, ipadx=10, sticky=W)
action18 = ttk.Button(monty, text="财务审核", width=30, command=toNode.CaiWuShenHe)
action18.grid(column=3, row=10, rowspan=1, ipady=7, padx=0, ipadx=10, sticky=W)
action19 = ttk.Button(monty, text="出纳垫款", width=30, command=toNode.ChuNaDianKuan)
action19.grid(column=3, row=11, rowspan=1, ipady=7, padx=0, ipadx=10, sticky=W)
action20 = ttk.Button(monty, text="纸质资料", width=30, command=ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL)
action20.grid(column=3, row=12, rowspan=1, ipady=7, padx=0, ipadx=10, sticky=W)
action14 = ttk.Button(monty, text="抄单", width=30, command=toNode.ChaoD)
action14.grid(column=2, row=14, ipady=7, ipadx=120, columnspan=100, sticky=N)
action15 = ttk.Button(monty, text="抄单内勤", width=30, command=toNode.ChaoDanNeiQ)
action15.grid(column=2, row=15, ipady=7, ipadx=120, columnspan=100, sticky=N)
action16 = ttk.Button(monty, text="开卡", width=30, command=toNode.Kaika)
action16.grid(column=2, row=16, ipady=7, ipadx=120, columnspan=100, sticky=N)
action17 = ttk.Button(monty, text="驻行送审", width=30, command=toNode.ZhuHangSongShen)
action17.grid(column=2, row=17, ipady=7, ipadx=120, columnspan=100, sticky=N)
action18 = ttk.Button(monty, text="审核员提额", width=30, command=TiE.Tie)
action18.grid(column=2, row=18, ipady=7, ipadx=120, columnspan=100, sticky=N)
action18 = ttk.Button(monty, text="待回款", width=30, command=DaiHuiKuan.daihuikuan)
action18.grid(column=2, row=19, ipady=7, ipadx=120, columnspan=100, sticky=N)

# ==================================================    查询   ==================================================================


monty = ttk.LabelFrame(tab4,
                       text='===================================================我是华丽的分割线================================================================')
monty.grid(column=90, row=0, padx=8, pady=2)


def clickMe():
    action.configure()
    # action.configure(state='disabled')  # Disable the Button Widget
    a = search()[0]
    b = search()[1]
    # print(b)
    # print(type(b))
    return a, b


def search():
    name1 = name.get()
    result = getsql.getsqldata(name1)
    result2 = getsql.getHistroy(name1)
    # print(result2)
    # print(type(result2))
    # print("result2::    "+result2)
    return result, result2


def _spin():
    value = clickMe()[0]
    value2 = clickMe()[1]
    # 清空展示框
    scr.delete("0.0", END)
    scr2.delete("0.0", END)
    # print(1)

    # print(value2)
    # print(value2.decode('gbk').encode('utf-8'))
    # print(type(value2))
    # print(len(value2))
    if len(value) == 11:
        scr.insert(tk.INSERT, "暂无此人或者订单已完结" + '\n')
    else:
        for i in range(0, len(value)):
            # print(value2[i])
            # print(type(value2[i]))

            scr.insert(tk.INSERT, value[i] + '\n')

    if len(value2) == 4:
        scr2.insert(tk.INSERT, "查无此人" + '\n')

    else:
        for i in range(0, len(value2)):
            # print(value2[i])
            # print(type(value2[i]))

            scr2.insert(tk.INSERT, value2[i] + '\n')


ttk.Label(monty, text="输入身份证号:").grid(column=0, row=0, sticky='W')

# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=40, textvariable=name)
nameEntered.grid(column=0, row=1, sticky='W')

action = ttk.Button(monty, text="查询", width=10, command=_spin)
action.grid(column=1, row=1, ipady=5, ipadx=10, sticky='W')

ttk.Label(monty, text="当前流程节点:").grid(column=0, row=2, sticky='W')
scrolW = 140;
scrolH = 20
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, row=3, sticky='WE', columnspan=18)

ttk.Label(monty, text="历史流程明细:").grid(column=0, row=4, sticky='W')
scrolW = 160;
scrolH = 20
scr2 = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr2.grid(column=0, row=5, sticky='WE', columnspan=18)

# action.grid(column=2, row=1, ipady=7,ipadx=120, columnspan =100,sticky =N)


menubar = Menu(win)


class ED():
    @classmethod
    def hello(self):
        print('hello')

    @classmethod
    def about(self):
        showerror("Answer", "如有问题请联系制作人QQ:41607699")

    @classmethod
    def updatalog(self):
        showinfo("Updata",
                 "5.30 V1.1新增内容：创建订单newcar字段在excel中控制\n6.11 V1.2新增内容：区别新车/二手车提交资料，流程自动控制\n7.18 V2.0 新增内容：新增电审、审核后补充资料照片调整、新增提额流程\n8.02 V2.1新增内容：纸质资料节点流程调整、流程图片优化、"
                 "新增接口地址从excel手动修改、新增财务相关流程操作以及完成后补充资料节点操作\n8.09 V2.2新增内容：征信不通过时，系统自动重启订单\n8.15 V3.0新增内容：流程修改适配、新增独立节点审核功能\n9.01 V3.1新增客户手机号基础数据\n9.03 V3.2电审节点新增贷款金额，融费用字段\n"
                 "9.25 V4.0新增货款额基础数据、新增920需求所有节点资料修改、新增流程变更UI流程图界面适配、新增回款节点，车辆补充报告节点、\n10.18 V4.1新增内容：新增订单流程查询功能、新增二手车电审节点车型必填匹配、新增自动识别货款额5万+审核部流程\n10.25"
                 "V4.2新增内容：新增订单满足面签要求\n11.07 V5.0新增内容：新增程序自动判断业务员地区是否需要省区经理审核、GUI新增省区经理节点、基础资料新增省区经理登录相关字段填入、新增审核必填字段验证\n11.08 V5.1新增内容：BUG修复"
                 "\n11.28 V6.0新增内容：适配点融项目订单资料（买车人工作单位，紧急联系人，车商等） \n 12.14 V7.0新增内容：创单录入快贷相关数据，新增工行、农行渠道，更改数据驱动方式\n19.01.25 V8.0新增内容：新增快贷订单通道\n19.02.14 V8.1新增内容：新增电审车300照片"
                 "\n19.02.25 V9.0新增内容：适配最新流程、新增联通大数据")


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=ED.about)
# helpmenu.add_command(label="详情", command=ED.updatalog)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu1 = Menu(menubar, tearoff=0)
helpmenu1.add_command(label="更新详情", command=ED.updatalog)
menubar.add_cascade(label="更新历史", menu=helpmenu1)
win.config(menu=menubar)
# tk.config(menu=menubar1)
# text=Text()

tk.mainloop()
