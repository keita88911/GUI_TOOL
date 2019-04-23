# -*- coding: utf-8 -*-

import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
a=[1,2,3,6,88,77]
b=[5,6,7,55,6,6]
c=["a按时打算大",]
#
# numb = len(a) - len(c)
# print(numb)
# if numb >= 0:
#     oo=0
#     for ii in range(numb, 0,-1):
#         oo-=1
#         # a[00-1]
#         print(oo)
#         print(a[oo])
#         # print(ii)
# def __init__(self):
#     self.c = []
#     self.c.append(test.A())


class test(object):

    @classmethod
    def A(self):
        print("inter A")
        a=1+1
        return a


    def B(self):

        b=test.A()
        print(b)


    def C(self):
        c=test.A()
        print(c)
ea=test()
print(ea.B())
print(ea.C())
# print(ea.B())


# d=[u'']
# v=[1]
# g=[1]
# print(d[0])
# print(str(d).replace('u\'','\'').decode('unicode_escape'))
# print(len(d))
# if  not (d and v and g):
#     print("null")
# else:
#     print("not null")