a= ["293","6234","5552","5896"]

a.sort()

print(a)
b="".join(a)
cc=(sorted(b))
print("".join(cc))
# ll=[]
# for  i in a:
#     for n in range(0,len(i)):
#         m = 0
#         m=m+n
#         n=n+1
#         ll.append(i[m:n])
# ll.sort(reverse=True)
# ll="".join(ll)
# print(ll)
# # for i in ll:
# li=[2,1,4,5,0]
# li.sort()
# print li
# a=[str(i) for i in a]
# a.sort(reverse=True)
# a="".join(a)
# print(a)
# import os
# print os.getcwd()
# @classmethod
# def answer6(number_list):
#     # max length of number for filling
#     max_len = max(len(str(x)) for x in number_list)
#     # left adjustment of number, filling last digit of number at right
#     fillings = (str(x).ljust(max_len, str(x)[-1]) for x in number_list)
#     # build data structure to hold mapping between filled number and original number
#     # not dict because of duplicated filled number key
#     m = zip(fillings, number_list)
#     # sort in reverse string order by filled number
#     sorted_l = sorted(m, key=lambda x: x[0], reverse=True)
#     # join original number in the order sorted as above
#     return ','.join(str(x[1]) for x in sorted_l)
# a=answer6(['7864','284','347','88','7732','7721','8498','9','99','2','11111','999','888','8'])
# print(a)
# ac="pwwkew"
# aa=list(ac)
# formatList = list({}.fromkeys(aa).keys())
# print(len(formatList))