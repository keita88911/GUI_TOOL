# -*- coding: UTF-8 -*-
from Tkinter import *
from tkMessageBox import *
import tkFileDialog
from start import *
import createTD
import test11
import pachong



tk=Tk()
tk.title("惠商车服软件部内部工具for erp  v1.3")
tk.geometry("800x800+0+0")
lab=Menubutton(tk,text="从excel批量创建订单")
Label(tk, text="测试部工具",  font=("Arial",15)).pack()
frm = Frame(tk)
frm_L = Frame(frm)

frm_T=Frame(frm)
btn4=Button(frm_T,text="爬虫获取身份证",width = 15,height = 1,fg = 'red',command=pachong.GetIdNumber.Idnumber).pack()
btn5=Button(frm_T,text="填写基础数据",width = 15,height = 1,fg = 'red',command=test11.open.openexcel).pack()
frm_T.pack(side=TOP)

# btn0=Button(frm_L,text="批量创建订单",width = 30,height = 2,fg = 'red',command=createTD.create.addTD).pack()
btn=Button(frm_L,text="新建订单至达驻行节点",width = 30,height = 2,fg = 'red',command=GettoNode.GettoZhuhang).pack()
btn2=Button(frm_L,text="新建订单至达电审节点",width = 30,height = 2,fg = 'red',command=GettoNode.GettoDianshen).pack()
btn7=Button(frm_L,text="新建订单至车价评估节点",width = 30,height = 2,fg = 'red',command=GettoNode.GettoChejia).pack()
btn6=Button(frm_L,text="新建订单至初审",width = 30,height = 2,fg = 'red',command=GettoNode.GettChuShen).pack()
btn9=Button(frm_L,text="新建订单至审核主管",width = 30,height = 2,fg = 'red',command=GettoNode.GettoShenheZhuGuan).pack()
btn10=Button(frm_L,text="新建订单至审核经理",width = 30,height = 2,fg = 'red',command=GettoNode.GetttoShenheJingLi).pack()
btn11=Button(frm_L,text="新建订单至审核总经理",width = 30,height = 2,fg = 'red',command=GettoNode.GettoShenheZongJingLing).pack()
btn15=Button(frm_L,text="新建订单至补充信息审核后",width = 30,height = 2,fg = 'red',command=GettoNode.GettoBuChongXinXi).pack()
# btn8=Button(frm_L,text="通过征信后补充",width = 30,height = 2,fg = 'red',command=GettoNode.GettZhenxinBuchong).pack()
frm_L.pack(side=LEFT)


frm_R = Frame(frm)
btn3=Button(frm_R,text="通过征信后补充",width = 30,height = 21,fg = 'red',command=GettoNode.GettZhenxinBuchong).pack()
frm_R.pack(side=RIGHT)

# frm_bt=Frame(frm)
# btn16=Button(frm_bt,text="新建订单至车图GPS",width = 50,height = 2,fg = 'red',command=GettoNode.GettZhenxinBuchong).pack()
# frm_bt.pack(side=BOTTOM)


frm2 = Frame(tk)
# frm_T2=Frame(frm2)
# btn16=Button(frm_T2,text="新建订单至车图GPS",width = 30,height = 2,fg = 'red',command=GettoNode.GettZhenxinBuchong).pack()
# frm_T2.pack(side=TOP)

frm_L2 = Frame(frm2)
btn16=Button(frm_L2,text="新建订单至车图GPS",width = 30,height = 3,fg = 'red',command=GettoNode.GettoCheTuGPS).pack()
btn17=Button(frm_L2,text="新建订单至车辆评估报告",width = 30,height = 3,fg = 'red',command=GettoNode.GettoCheLiangPingGuBaoGao).pack()
frm_L2.pack(side=LEFT)

frm_R2 = Frame(frm2)

btn15=Button(frm_R2,text="通过补充财务信息",width = 30,height = 1,fg = 'red',command=GettoNode.ZhiZhiZiLiao).pack()
btn15=Button(frm_R2,text="通过财务审核",width = 30,height = 1,fg = 'red',command=GettoNode.ZhiZhiZiLiao).pack()
btn15=Button(frm_R2,text="通过出纳垫款",width = 30,height = 1,fg = 'red',command=GettoNode.ZhiZhiZiLiao).pack()
btn14=Button(frm_R2,text="通过纸质资料确认",width = 30,height = 1,fg = 'red',command=GettoNode.ZhiZhiZiLiao).pack()

frm_R2.pack(side=RIGHT)

frm3 = Frame(tk)
frm_L3 = Frame(frm3)
btn18=Button(frm_L3,text="新建订单至抄单",width = 61,height = 2,fg = 'red',command=GettoNode.GettoChaoDan).pack()
btn19=Button(frm_L3,text="新建订单至抄单内勤",width = 61,height = 2,fg = 'red',command=GettoNode.GettoChaoDanNeiQin).pack()
btn20=Button(frm_L3,text="新建订单至开卡",width = 61,height = 2,fg = 'red',command=GettoNode.GettoKaika).pack()
btn21=Button(frm_L3,text="新建订单至驻行送审",width = 61,height = 2,fg = 'red',command=GettoNode.GettoZhuHangSongShen).pack()
frm_L3.pack(side=LEFT)



frm.pack()
# frm2.pack_propagate(0)
frm2.pack()
frm3.pack()
menubar = Menu(tk)

class ED():
    @classmethod
    def hello(self):
        print('hello')

    @classmethod
    def about(self):
        showerror("Answer", "请联系制作人QQ:41607699")
    @classmethod
    def updatalog(self):
        showinfo("updata", "5.30 V1.1新增内容：创建订单newcar字段在excel中控制\n6.11 V1.2新增内容：区别新车/二手车提交资料，流程自动控制\n7.18 V1.3 新增电审、审核后补充资料照片调整"  )
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=ED.about)
# helpmenu.add_command(label="详情", command=ED.updatalog)
menubar.add_cascade(label="帮助", menu=helpmenu)
helpmenu1 = Menu(menubar, tearoff=0)
helpmenu1.add_command(label="更新详情", command=ED.updatalog)
menubar.add_cascade(label="更新历史", menu=helpmenu1)
tk.config(menu=menubar)
# tk.config(menu=menubar1)
# text=Text()
# tk.iconbitmap('1.ico')

tk.mainloop()

