# -*- coding: UTF-8 -*-
import tkFileDialog
import os,sys
class open():
    @classmethod
    def openexcel(self):
        # os.path.realpath(__file__)
        # a=os.path.dirname(os.path.realpath(__file__))
        # filename = tkFileDialog.askopenfilename(initialdir=a)
        # os.path.split(os.path.realpath(__file__))[0]
        # os.path.abspath(__file__)
        # os.getcwd()
        # sys.path[0]
        # sys.argv[0]
        # b='D:\oa2tes\Add1.xlsx'
        os.startfile('add1.xlsx')
        # print( a)
        # print filename
# a=open.openexcel()