#!./usr/bin/env.python
#.-*- coding: utf-8 -*-
#._author_.=."Max丶"
#._Email:_.=."max@chamd5.org"

# dic= {
#     'name':['alex','wusir','taibai'],
#     'py9':{
#         'time':'1213',
#         'learn_money':19800,
#         'adder':'CBD',
#     },
#     'age':21
# }
#
# dic['age']=56  #在字典最后追加一个age：56
# print(dic)


# dic= {
#     'name':['alex','wusir','taibai'],
#     'py9':{
#         'time':'1213',
#         'learn_money':19800,
#         'adder':'CBD',
#     },
#     'age':21
# }
#
# dic['name'].append('libai')  #如何在name的列表里面添加一个libai：
# print(dic)


# #要求是把wusir全部大写
# dic= {
#     'name':['alex','wusir','taibai'],
#     'py9':{
#         'time':'1213',
#         'learn_money':19800,
#         'adder':'CBD',
#     },
#     'age':21
# }
#
# dic['name'][1]=dic['name'][1].upper()  #重点记住这这一行写法 更改办法都是这样写法
# print(dic)


#如何嵌套的情况下在py9的字典里面添加
dic= {
    'name':['alex','wusir','taibai'],
    'py9':{
        'time':'1213',
        'learn_money':19800,
        'adder':'CBD',
    },
    'age':21
}

dic['py9']['renshuo']=6
print(dic)