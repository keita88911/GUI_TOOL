# -*- coding: UTF-8 -*-
import re
pile="token"
token1="111"
com=re.compile(pile)
data={"token":"!{token}","data":[1,23,4,5,6,],"okid":"!id"}
# print(com)
data1="123123po!{token}ppop"
v1 = re.sub(com, token1, data1, 0)
for i ,v in data.items():
    try:
        v=re.sub(com,token1,v,0)
    except:
        print("falid")
        False
# data="qqweqwe!token123213"
#     out=re.sub(com,token1,i,0)
#     print(i,v)

# print(v1)
key = "!{" + pile + "}"
values = token1
api_data="!{token}12123123:123123123:123123"
com = re.compile(key)
api_data1 = re.sub(com, values, api_data, 0)
# print(api_data1)
a=123456
b=str(a)
c=list(map(int,str(a)))
c.reverse()

print(len(b),c)