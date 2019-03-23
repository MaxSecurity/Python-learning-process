#!./usr/bin/env.python
#.-*- coding: utf-8 -*-
#._author_.=."Max丶"
#._Email:_.=."max@chamd5.org"

#元组是什么？只读列表，可查询，可切片。
#那么元组里面什么可以改？？？[]元组里面的列表可以改

# tu = (1,2,3,'MAX',[2,3,4,'tianji'],'baibai')
# print(tu[3]) #查询
# print(tu[0:4])#切片
# for i in tu:
#     print(i)#循环输出tu里面所有元素

#把tianji修改为全部大写
# tu = (1,2,3,'MAX',[2,3,4,'tianji'],'baibai')
# tu[4][3]=tu[4][3].upper()
# print(tu)

#追加一个libai 知识点需要.append() append默认追加在最后
# tu = (1,2,3,'MAX',[2,3,4,'tianji'],'baibai')
# tu[4].append('libai')
# print(tu)


#join用法   用字符连接元素  +可以替换任何符合数字字符
# s='libai'
# s1 = '+'.join(s)
# print(s1)


#列表转换字符串 join 不写任何东西无缝添加 list ---》str
# nb=['woqwsda','sdakjs','tianji','李太白']
# su = ''.join(nb)
# #str --》list  split（）
# print(su)


#range函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表。
# for i in range(0,10):#或者直接写10
#     print(i) #打印的都是一个一个的打印下去
#range 也可以加补偿 就是相隔几位输出数
# for i in range(0,10,2):
#     print(i)

#倒着跑输出
# for i in range(10,0,-1):
#     print(i)
#另一种相隔两位输出 相隔几位输出修改-2就可以  或者中间0修改成-1 结果为 10 8 6 4 2 0
# for i in range(10,0,-2):
#     print(i)

#有可能会是考试题 这个不会报错 不会输出 啥都不会输出
# for i in range(0,10,-1):
#     print(i)