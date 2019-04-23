import createTD
import zhuhangSS
import dianS
import chejiaPG
import zhengxinAfterCredit
import chushen
import ShenheZhuGuan
import ShenheJingLi
import buchongshenhehou
import ShenheZongJingLi
import ZhiZhiZiLiao
import CheTuGPS
import CheLiangPingGuBaoGao
import ChaoDan
import ChaoDanNeiQin
import KaiKa
import rdexcel
from AddCaiWu import *
from  CaiWuShenHe import *
from  ChuNaDianKuan import *
import ZhuHangSongShen1
import createTD2
import StartZhengXin


class toNode():
    @classmethod
    def GetNewcar(self):
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        listcar = []
        for i in range(0, len(listdata1)):
            listcar.append(listdata1[i]['newcar'])
            # print(listcar[i])
        return listcar
    @classmethod
    def createTD(self):
        step1 = createTD.create.addTD()
    @classmethod
    def zhuhangSS(self):
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
    @classmethod
    def dianSS(self):
        step5=dianS.buchongdianS.dianSS()
    @classmethod
    def chejiaPG(self):
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
    @classmethod
    def ZhenxinBuchong(self):
        step1 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step2 = zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step3 = zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
    @classmethod
    def chushen(self):
        step7=chushen.ChuShen.chushen()
    @classmethod
    def ShenheZG(self):
        step8=ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
    @classmethod
    def ShenheJL(cls):
        step9=ShenheJingLi.ShenheJingLi.ShenheJL()
    @classmethod
    def ShenheZongJL(cls):
        step10=ShenheZongJingLi.ShenheZongJingLi.ShenHeZongJL()
    @classmethod
    def ShenHehou(cls):
        step11=buchongshenhehou.BuChongXinxi.BuChongxinxi()
    @classmethod
    def BuChongZhengXin(self):
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13= zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14= zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
    @classmethod
    def ZhiZhiZiLiao(self):
        step1=ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
    @classmethod
    def GPS(self):
        step15=CheTuGPS.CheTuGPS.GPS()
    @classmethod
    def AddCaiWu(self):
        step17=AddCaiWu.AddCaiWu()
        step19=ChuNaDianKuan.ChuNaDianKuan()
    @classmethod
    def CaiWuShenHe(self):
        step18=CaiWuShenHe.CaiWuShenHe()
    @classmethod
    def ChuNaDianKuan(self):
        step19=ChuNaDianKuan.ChuNaDianKuan()
    @classmethod
    def ChaoD(self):
        step21=ChaoDan.ChaoDan.ChaoD()
    @classmethod
    def ChaoDanNeiQ(self):
        step22=ChaoDanNeiQin.ChaoDanNeiQin.ChaoDanNeiQ()
    @classmethod
    def Kaika(self):
        step23=KaiKa.KaiKa.Kaika()
    @classmethod
    def ZhuHangSongShen(self):
        step24=ZhuHangSongShen1.ZhuHangSongShen.ZhuHangSongShen()

    @classmethod
    def CheLiangPingGuBG(self):
        step16=CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()



# a=GettoNode.GettZhenxinBuchong()
