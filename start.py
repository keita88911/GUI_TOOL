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
import Province


class GettoNode():
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
    def GettoZhuhang(self):
        step1 = createTD.create.addTD()

    @classmethod
    def GettoDianshen(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()

    @classmethod
    def GettoChejia(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()

    @classmethod
    def GettChuShen(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
    @classmethod
    def GettZhenxinBuchong(self):
        step1 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step2 = zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step3 = zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
    @classmethod
    def GettoProvince(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=chushen.ChuShen.chushen()

    @classmethod
    def GettoShenheZhuGuan(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=chushen.ChuShen.chushen()
        step8=Province.Province.province()

    @classmethod
    def GetttoShenheJingLi(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=chushen.ChuShen.chushen()
        step8 = Province.Province.province()
        step8=ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
    @classmethod
    def GettoShenheZongJingLing(cls):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=chushen.ChuShen.chushen()
        step8 = Province.Province.province()
        step8=ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
        step9=ShenheJingLi.ShenheJingLi.ShenheJL()
    @classmethod
    def GettoBuChongXinXi(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=chushen.ChuShen.chushen()
        step8 = Province.Province.province()
        step8=ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
        step9=ShenheJingLi.ShenheJingLi.ShenheJL()
        step10=ShenheZongJingLi.ShenheZongJingLi.ShenHeZongJL()
    @classmethod
    def GettoCheTuGPS(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=chushen.ChuShen.chushen()
        step8 = Province.Province.province()
        step8=ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
        step9=ShenheJingLi.ShenheJingLi.ShenheJL()
        step10=ShenheZongJingLi.ShenheZongJingLi.ShenHeZongJL()
        step11=buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13= zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14= zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step11 = buchongshenhehou.BuChongXinxi.BuChongxinxi()
    @classmethod
    def ZhiZhiZiLiao(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=chushen.ChuShen.chushen()
        step8 = Province.Province.province()
        step8=ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
        step9=ShenheJingLi.ShenheJingLi.ShenheJL()
        step10=ShenheZongJingLi.ShenheZongJingLi.ShenHeZongJL()
        step11=buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13= zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14= zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step1=CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()
    @classmethod
    def GettoCheLiangPingGuBaoGao(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=chushen.ChuShen.chushen()
        step8 = Province.Province.province()
        step8=ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
        step9=ShenheJingLi.ShenheJingLi.ShenheJL()
        step10=ShenheZongJingLi.ShenheZongJingLi.ShenHeZongJL()
        step11=buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13= zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14= zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()


    @classmethod
    def GettoChaoDan(self):
        step1 = createTD.create.addTD()
        step0 = StartZhengXin.StartZhengXin.StartZhengXin()
        step2 = zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4 = zhuhangSS.zhuhang.songshen()
        step5 = dianS.buchongdianS.dianSS()
        step6 = chejiaPG.CheJiaPingGu.chejiaPG()
        step7 = chushen.ChuShen.chushen()
        step8 = Province.Province.province()
        step8 = ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
        step9 = ShenheJingLi.ShenheJingLi.ShenheJL()
        step10 = ShenheZongJingLi.ShenheZongJingLi.ShenHeZongJL()
        step11 = buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13 = zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14 = zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step1 = CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()
        step20 = ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
    @classmethod
    def GettoChaoDanNeiQin(self):
        step1 = createTD.create.addTD()
        step0 = StartZhengXin.StartZhengXin.StartZhengXin()
        step2 = zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4 = zhuhangSS.zhuhang.songshen()
        step5 = dianS.buchongdianS.dianSS()
        step6 = chejiaPG.CheJiaPingGu.chejiaPG()
        step7 = chushen.ChuShen.chushen()
        step8 = Province.Province.province()
        step8 = ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
        step9 = ShenheJingLi.ShenheJingLi.ShenheJL()
        step10 = ShenheZongJingLi.ShenheZongJingLi.ShenHeZongJL()
        step11 = buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13 = zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14 = zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step1 = CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()
        step20 = ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
        step21=ChaoDan.ChaoDan.ChaoD()


    @classmethod
    def GettoKaika(self):
        step1 = createTD.create.addTD()
        step0 = StartZhengXin.StartZhengXin.StartZhengXin()
        step2 = zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4 = zhuhangSS.zhuhang.songshen()
        step5 = dianS.buchongdianS.dianSS()
        step6 = chejiaPG.CheJiaPingGu.chejiaPG()
        step7 = chushen.ChuShen.chushen()
        step8 = Province.Province.province()
        step8 = ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
        step9 = ShenheJingLi.ShenheJingLi.ShenheJL()
        step10 = ShenheZongJingLi.ShenheZongJingLi.ShenHeZongJL()
        step11 = buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13 = zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14 = zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step1 = CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()
        step20 = ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
        step21=ChaoDan.ChaoDan.ChaoD()
        step22=ChaoDanNeiQin.ChaoDanNeiQin.ChaoDanNeiQ()
    @classmethod
    def GettoZhuHangSongShen(self):
        step1 = createTD.create.addTD()
        step0 = StartZhengXin.StartZhengXin.StartZhengXin()
        step2 = zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4 = zhuhangSS.zhuhang.songshen()
        step5 = dianS.buchongdianS.dianSS()
        step6 = chejiaPG.CheJiaPingGu.chejiaPG()
        step7 = chushen.ChuShen.chushen()
        step8 = Province.Province.province()
        step8 = ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
        step9 = ShenheJingLi.ShenheJingLi.ShenheJL()
        step10 = ShenheZongJingLi.ShenheZongJingLi.ShenHeZongJL()
        step11 = buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13 = zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14 = zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step1 = CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()
        step20 = ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
        step21=ChaoDan.ChaoDan.ChaoD()
        step22=ChaoDanNeiQin.ChaoDanNeiQin.ChaoDanNeiQ()
        step23=KaiKa.KaiKa.Kaika()

    @classmethod
    def GettoWanCheng(self):
        step1 = createTD.create.addTD()
        step0 = StartZhengXin.StartZhengXin.StartZhengXin()
        step2 = zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4 = zhuhangSS.zhuhang.songshen()
        step5 = dianS.buchongdianS.dianSS()
        step6 = chejiaPG.CheJiaPingGu.chejiaPG()
        step7 = chushen.ChuShen.chushen()
        step8 = Province.Province.province()
        step8 = ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
        step9 = ShenheJingLi.ShenheJingLi.ShenheJL()
        step10 = ShenheZongJingLi.ShenheZongJingLi.ShenHeZongJL()
        step11 = buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13 = zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14 = zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step1 = CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()
        step20 = ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
        step21 = ChaoDan.ChaoDan.ChaoD()
        step22 = ChaoDanNeiQin.ChaoDanNeiQin.ChaoDanNeiQ()
        step23 = KaiKa.KaiKa.Kaika()
        step24=ZhuHangSongShen1.ZhuHangSongShen.ZhuHangSongShen()





# a=GettoNode.GettZhenxinBuchong()
