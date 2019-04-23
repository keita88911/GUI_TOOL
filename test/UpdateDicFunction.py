#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import uniout


def a():
    a = [(1, '惠商OA', 0, 1),
         (2, '登录接口', 1, 2),
         (3, '审核相关', 1, 2),
         (4, '财务相关', 1, 2),
         (5, '其他项目', 0, 1),
         (6, '其他项目-1', 5, 2),
         (7, '登录接口-1', 2, 3),
         (8, '其他接口', 1, 2),
         (9, '财务相关11', 5, 2),
         (10, '财务相关13', 5, 2),
         (11, '登录接口-2', 2, 3),
         (12, '登录接口-3', 11, 4)
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
    B = []
    # 循环获取开始
    for dic_x in a:
        # 处理一级
        if dic_x[2] not in parent_id:
            list_value.append(dic_x)
            parent_id.append(dic_x[0])
            k.append(dic_x[0])
            one_two[dic_x[0]] = []
        # 处理二级
        elif dic_x[2] in parent_id:
            parent_id.append(dic_x[0])
            index = parent_id.index(dic_x[2])
            try:
                index_k = k.index(dic_x[2])
                if index == index_k:
                    if type(list_value[index]) != list:
                        H = []
                        H.append(list_value[index])
                        H.append(dic_x)
                        list_value[index] = H
                    else:
                        list_value[index].append(dic_x)
                else:
                    if type(list_value[index_k]) == list:
                        H = []
                        H.append(list_value[index_k])
                        H.append(dic_x)
                        list_value[index_k] = H
                    else:
                        if type(list_value[index_k]) != list:
                            z = []
                            z.append(list_value[index_k])
                            z.append(dic_x)
                            list_value[index_k] = z
                        else:
                            list_value[index_k].append(dic_x)
            except ValueError:
                # 处理三级
                for key, value in one_two.items():
                    for z in value:
                        if z == dic_x[2]:
                            key_index=k.index(key)
                            L = value.index(z)+1
                            P = list_value[key_index]

                            # if用于第一次执行三级处理，else针对以后的
                            if type(P[L]) != list:
                                B=[]
                                B.append(P[L])
                                B.append(dic_x)
                                P[L] = B
                            else:
                                P[L].append(dic_x)
            else:
                one_two[dic_x[2]].append(dic_x[0])
    # 所有数据处理完成，存在一个列表后执行下面步骤，将列表以字典表形式存储并展示
    for m in list_value:
        n=list_value.index(m)+1
        dic[n]=m
    print(str(dic))

def b(a):
    a = [(1, '惠商OA', 0, 1),
         (2, '登录接口', 1, 2),
         (3, '审核相关', 1, 2),
         (4, '财务相关', 1, 2),
         (5, '其他项目', 0, 1),
         (6, '其他项目-1', 5, 2),
         (7, '登录接口-1', 2, 3),
         (8, '其他接口', 1, 2),
         (9, '财务相关11', 5, 2),
         (10, '财务相关13', 5, 2),
         (11, '登录接口-2', 2, 3),
         (12, '登录接口-3', 11, 4)
         ]
    father=[]
    for i in a:
        if str(i[0])==str(0):
            for n in a:
                if i[0] =
