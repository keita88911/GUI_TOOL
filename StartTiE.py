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
import createTD2
import TiE
import ZhuHangSongShen1
from AddCaiWu import *
from  CaiWuShenHe import *
from  ChuNaDianKuan import *
import StartZhengXin


class GettoNode1():
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
    def GettoZhuhang1(self):
        step1 = createTD.create.addTD()

    @classmethod
    def GettoDianshen1(self):
        step1 = createTD.create.addTD()
        step0 = StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()

    @classmethod
    def GettoChejia1(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()

    @classmethod
    def GettChuShen1(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
    @classmethod
    def GettZhenxinBuchong1(self):
        step1 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step2 = zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step3 = zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()

    @classmethod
    def GettoShenheZongJingLing1(cls):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=chushen.ChuShen.chushen()
        step8=ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
        step9=ShenheJingLi.ShenheJingLi.ShenheJL()
    @classmethod
    def GettoBuChongXinXi1(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=TiE.TiE.Tie()

    @classmethod
    def GettoCheTuGPS1(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=TiE.TiE.Tie()


        step11=buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13= zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14= zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
    @classmethod
    def ZhiZhiZiLiao1(self):
        step1=ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
    @classmethod
    def GettoCheLiangPingGuBaoGao1(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=TiE.TiE.Tie()

        step11=buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13= zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14= zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step15=CheTuGPS.CheTuGPS.GPS()

    @classmethod
    def GettoChaoDan1(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=TiE.TiE.Tie()

        step11=buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13= zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14= zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step15=CheTuGPS.CheTuGPS.GPS()

        # newcar=GettoNode.GetNewcar()
        # for i in range(0, len(newcar)):
        #     print(int(newcar[i]))
        #     if int(newcar[i])==0:

        step16=CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()
        step17 = ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
    @classmethod
    def GettoChaoDanNeiQin1(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=TiE.TiE.Tie()

        step11=buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13= zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14= zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step15=CheTuGPS.CheTuGPS.GPS()
        step16=CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()
        step17 = ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
        step18=ChaoDan.ChaoDan.ChaoD()


    @classmethod
    def GettoKaika1(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=TiE.TiE.Tie()

        step11=buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13= zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14= zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step15=CheTuGPS.CheTuGPS.GPS()
        step16=CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()
        step17 = ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
        step18=ChaoDan.ChaoDan.ChaoD()
        step19=ChaoDanNeiQin.ChaoDanNeiQin.ChaoDanNeiQ()
    @classmethod
    def GettoZhuHangSongShen1(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=TiE.TiE.Tie()

        step11=buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13= zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14= zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step15=CheTuGPS.CheTuGPS.GPS()
        step16=CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()
        step17 = ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
        step18=ChaoDan.ChaoDan.ChaoD()
        step19=ChaoDanNeiQin.ChaoDanNeiQin.ChaoDanNeiQ()
        step20=KaiKa.KaiKa.Kaika()
    @classmethod
    def GettoShenheZhuGuan1(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=TiE.TiE.Tie()

        step11=buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13= zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14= zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step15=CheTuGPS.CheTuGPS.GPS()
        step16=CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()
        step17 = ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
        step18=ChaoDan.ChaoDan.ChaoD()
        step19=ChaoDanNeiQin.ChaoDanNeiQin.ChaoDanNeiQ()
        step20=KaiKa.KaiKa.Kaika()
        step21=ZhuHangSongShen1.ZhuHangSongShen.ZhuHangSongShen()

    @classmethod
    def GetttoShenheJingLi1(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=TiE.TiE.Tie()

        step11=buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13= zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14= zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step15=CheTuGPS.CheTuGPS.GPS()
        step16=CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()
        step17 = ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
        step18=ChaoDan.ChaoDan.ChaoD()
        step19=ChaoDanNeiQin.ChaoDanNeiQin.ChaoDanNeiQ()
        step20=KaiKa.KaiKa.Kaika()
        step21=ZhuHangSongShen1.ZhuHangSongShen.ZhuHangSongShen()
        step22 = ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
    @classmethod
    def GetttoAddCaiWu(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=TiE.TiE.Tie()

        step11=buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13= zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14= zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step15=CheTuGPS.CheTuGPS.GPS()
        step16=CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()
        step17 = ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
        step18=ChaoDan.ChaoDan.ChaoD()
        step19=ChaoDanNeiQin.ChaoDanNeiQin.ChaoDanNeiQ()
        step20=KaiKa.KaiKa.Kaika()
        step21=ZhuHangSongShen1.ZhuHangSongShen.ZhuHangSongShen()
        step22 = ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
        step23=ShenheJingLi.ShenheJingLi.ShenheJL()
    @classmethod
    def GetttoCaiWuShenHe(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=TiE.TiE.Tie()

        step11=buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13= zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14= zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step15=CheTuGPS.CheTuGPS.GPS()
        step16=CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()
        step17 = ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
        step18=ChaoDan.ChaoDan.ChaoD()
        step19=ChaoDanNeiQin.ChaoDanNeiQin.ChaoDanNeiQ()
        step20=KaiKa.KaiKa.Kaika()
        step21=ZhuHangSongShen1.ZhuHangSongShen.ZhuHangSongShen()
        step22 = ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
        step23=ShenheJingLi.ShenheJingLi.ShenheJL()
        step24=AddCaiWu.AddCaiWu()
    @classmethod
    def GetttoChuNaiDianKuan(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=TiE.TiE.Tie()

        step11=buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13= zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14= zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step15=CheTuGPS.CheTuGPS.GPS()
        step16=CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()
        step17 = ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
        step18=ChaoDan.ChaoDan.ChaoD()
        step19=ChaoDanNeiQin.ChaoDanNeiQin.ChaoDanNeiQ()
        step20=KaiKa.KaiKa.Kaika()
        step21=ZhuHangSongShen1.ZhuHangSongShen.ZhuHangSongShen()
        step22 = ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
        step23=ShenheJingLi.ShenheJingLi.ShenheJL()
        step24=AddCaiWu.AddCaiWu()
        step24=CaiWuShenHe.CaiWuShenHe()
    @classmethod
    def GetttoWanCheng(self):
        step1 = createTD.create.addTD()
        step0=StartZhengXin.StartZhengXin.StartZhengXin()
        step2=zhuhangSS.zhuhang.ZhuHangDY()
        # step3=zhuhangSS.zhuhang.ZhengXinReport()
        step4=zhuhangSS.zhuhang.songshen()
        step5=dianS.buchongdianS.dianSS()
        step6=chejiaPG.CheJiaPingGu.chejiaPG()
        step7=TiE.TiE.Tie()

        step11=buchongshenhehou.BuChongXinxi.BuChongxinxi()
        step12 = zhengxinAfterCredit.zhegnxinAC.zhengxinJichu()
        step13= zhengxinAfterCredit.zhegnxinAC.zhengxinBiyao()
        step14= zhengxinAfterCredit.zhegnxinAC.zhenxinXuantian()
        step15=CheTuGPS.CheTuGPS.GPS()
        step16=CheLiangPingGuBaoGao.CheLiangPingGuBaoGao.CheLiangPingGuBG()
        step17 = ZhiZhiZiLiao.ZhiZhiZiLiao.ZhiZhiZL()
        step18=ChaoDan.ChaoDan.ChaoD()
        step19=ChaoDanNeiQin.ChaoDanNeiQin.ChaoDanNeiQ()
        step20=KaiKa.KaiKa.Kaika()
        step21=ZhuHangSongShen1.ZhuHangSongShen.ZhuHangSongShen()
        step22 = ShenheZhuGuan.ShenheZhuGuan.ShenheZG()
        step23=ShenheJingLi.ShenheJingLi.ShenheJL()
        step24=AddCaiWu.AddCaiWu()
        step24=CaiWuShenHe.CaiWuShenHe()
        step25=ChuNaDianKuan.ChuNaDianKuan()






# a=GettoNode.GettZhenxinBuchong()
