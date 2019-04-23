# -*- coding: UTF-8 -*-
menus = [
    {
        'text':'北京',
        'text2':'北京1',
        'children':[
            {'text':'朝阳','children':[]},
            {'text':'昌平','children':[
                {'text':'沙河','children':[]},
                {'text':'回龙观','children':[]},
                ]},
            ]
        },
    {
        'text':'上海',
        'children':[
            {'text':'朝阳1','children':[]},
            {'text':'昌平2','children':[]},
            ]
        }
    ]
print(len(menus[0]))
print(type(menus))
# list=[]
# for i in range(0,len(menus)):
#     list.append(menus[i]['text'])
#     for y in range(0,len(menus)):
#         # print(menus[i]['children'][y]['text'])
#         list.append(menus[i]['children'][y]['text'])
#         # print(list[i])
#         if y == 1 and i == 0:
#             for n in range(0,len(menus)):
#                 list.append(menus[i]['children'][y]['children'][n]['text'])
# for x in range(0,len(list)):
#     print(list[x])

# print(menus[1]['children'][1]['text'])
# print(menus[1]['children'][1]['children'][0]['text'])