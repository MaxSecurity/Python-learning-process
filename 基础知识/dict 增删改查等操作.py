#!./usr/bin/env.python
#.-*- coding: utf-8 -*-
#._author_.=."Max丶"
#._Email:_.=."max@chamd5.org"

# dic = {
#     'name':['大猛','小萌'],
#     'py9':[{'mun':71,
#             'avg_AGE':18,}],
#     True:1,
#     (1,2,3):'wuyiyi',
#     2:'二哥'
#
# }
# print(dic)


#字典增加写法：
# dic = { 'age':18,'name':'max','sex':'male'}
# dic['high']=185  #没有high这个参数他会往里面增加 'heigh':185
# print(dic)

# dic = { 'age':18,'name':'max','sex':'male'}
# dic['hobby']='game'  #没有hobby这个参数他会往里面增加 'hobby':'game'
# print(dic)

# dic = { 'age':18,'name':'max','sex':'male'}
# dic['age']=19#如果里面有age通过这个可以覆盖
# print(dic)

# dic = { 'age':18,'name':'max','sex':'male'}
# # dic.setdefault('weight','nihao')  #还有一种写法就是.setdefault  如果nihao这个参数不写默认会是None
# dic.setdefault('age',25)  #但是记住一点！！如果字典里面有这个参数.setdefault是无法修改的
# print(dic)


#字典删除法：
# dic = { 'age':18,'name':'max','sex':'male'}
# dic.pop('age')   #又返回值的删除
# print(dic)

# dic = { 'age':18,'name':'max','sex':'male'}
# #小常识！！！如果你在写程序时候传过来的字典中不知道有没有tianji这个参数 时候这样写不会报错会返回一个None不存在的意思
# #None 这个可以自定义这个参数
# print(dic.pop('tianji',None))


# dic = { 'age':18,'name':'max','sex':'male'}
# dic.popitem()   #.popitem是从最后一个删除 但是在python 3.5里面是随机删除的  删除的又返回值 返回值格式是元组
# print(dic)

#清空字典所有
# dic = { 'age':18,'name':'max','sex':'male'}
# dic.clear()
# print(dic)

#删除字典
# dic = { 'age':18,'name':'max','sex':'male'}
# del dic
# print(dic)


#字典改方法
#第一种方法
# dic = { 'age':18,'name':'max','sex':'male'}
# dic['age'] = 16
# print(dic)

# #第二种：知识点！！.update意识是吧dic字典里面的东西更新到dic2里面 有相同的替换就是没有的添加进去
# dic = { 'name':'taibai','age':18,'sex':'male'}
# dic2 = { 'name':'max','weight':75}
# dic2.update(dic)
# print(dic)
# print(dic2)


#字典查询办法
# dic={ 'age':18,'name':'max','sex':'male'}
# print(dic.keys())
# print(dic.values())
# print(dic.items())

#循环打印查询方法：
# dic={ 'age':18,'name':'max','sex':'male'}
# for i in dic.keys():
#     print(i)
#
# for i in dic.values():
#     print(i)
#
# for i in dic.items():
#     print(i)

#第二种查询办法  这个办法有缺陷 查找字典里面没有的参数会报错
# dic={ 'age':18,'name':'max','sex':'male'}
#
# v1 = dic['name']
# print(v1)

#第三种办法：相比第二种办法的好处是 不会报错遇到没有的参数直接返回一个None 这个None 可以自定义
# dic={ 'age':18,'name':'max','sex':'male'}
# print(dic.get('name'))
# print(dic.get('name2','错误'))#这个是自定义返回的写法