#!/usr/bin/env python 
# -*- coding:utf-8 -*-
a = [(1, '惠商OA', 0, 1),
     (2, '登录接口', 1, 2),
     (3, '审核相关', 1, 2),
     (4, '财务相关', 1, 2),
     (5, '其他项目', 0, 1),
     (6, '其他项目-1', 5, 2),
     (7, '登录接口', 2, 3),
     (8, '其他接口', 1, 2),
     (11, '二级部门', 2, 3)
     ]
# 存储最后的数据列表
list_value = []
# 存储父ID所用
parent_id = []
# 最后的展示字典
dic = {}
# 记录二级父ID
k = []
# 一级 二级 关系字典表，三级处理时需要用到
one_two = {}

# 要用的空列表
H = []
# 循环获取开始
for dic_x in a:
    # 处理一级
    # 判断自身的父级ID是否存在这个所有ID表，如果没有，表明自身是一级数据，直接存入最终表，同时把自己的ID，作为二级ID存入K表
    if dic_x[2] not in parent_id:
        list_value.append(dic_x)
        parent_id.append(dic_x[0])
        k.append(dic_x[0])
        one_two[dic_x[0]] = []
    # 处理二级
    elif dic_x[2] in parent_id:
        parent_id.append(dic_x[0])
        try:
            # 这里用try的意思是，去二级K表查询自己父ID下标时，如果没查询到，会报错，说明这行数据是三级数据，另外处理
            # 定位二级ID在主显示表的位置
            index_k = k.index(dic_x[2])
            if type(list_value[index_k]) == list:
                list_value[index_k].append(dic_x)
            else:
                H.clear()
                H.append(list_value[index_k])
                H.append(dic_x)
                list_value[index_k] = H.copy()
        except ValueError:
            # 处理三级
            # 确认是三级数据后，先通过one_two字典表，找到自己父ID（二级）的上级ID，也就是一级ID
            for key, value in one_two.items():
                for z in value:
                    if z == dic_x[2]:
                        key_index = k.index(key)
                        L = value.index(z)+1
                        P = list_value[key_index]
                        # if用于第一次执行三级处理，else针对以后的
                        if type(P[L]) != list:
                            H.clear()
                            H.append(P[L])
                            H.append(dic_x)
                            P[L] = H.copy()
                        else:
                            P[L].append(dic_x)
                    break
        else:
            one_two[dic_x[2]].append(dic_x[0])

# 所有数据处理完成，存在一个列表后执行下面步骤，将列表以字典表形式存储并展示
for m in list_value:
    n = list_value.index(m)+1
    dic[n] = m
print(dic)


