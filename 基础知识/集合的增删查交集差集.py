#!./usr/bin/env.python
#.-*- coding: utf-8 -*-
#._author_.=."Max丶"
#._Email:_.=."max@chamd5.org"

#集合的增：
# #第一种：add这个添加时候是随机添加进去的
# li = {'max', 'max2', 'sec', 'anquan'}
# li.add('TIANJI')
# print(li)

#第二种：updata
# li = {'max', 'max2', 'sec', 'anquan'}
# li.update('abc')
# print(li)

#集合删除
#第一种办法：随机删除合集里面东西
# li = {'max', 'max2', 'sec', 'anquan'}
# li.pop()
# print(li)

#第二种办法指定按元素删除
# li = {'max', 'max2', 'sec', 'anquan'}
# li.remove('sec')
# print(li)

#第三种直接删除所有集合：
# li = {'max', 'max2', 'sec', 'anquan'}
# del li
# print(li)

#第四种如果不想删除所有合集只删除里面元素写法
# li = {'max', 'max2', 'sec', 'anquan'}
# li.clear()
# print(li)

#集合查询办法
# li = {'max', 'max2', 'sec', 'anquan'}
#
# for i in li:
#     print(i)


#合集取出交集元素的方法
#
# li1={1,2,3,4,5}
# li2={4,5,6,7,8}
# #有两个办法
# print(li1 & li2)#第一个办法 &
# print(li1.intersection(li2))#第二个办法 [个人推荐第一个办法]代码少

#合集的并集方法 把两个合集何在一起相同的只显示一个
# li1={1,2,3,4,5}
# li2={4,5,6,7,8}
#
# print(li1 | li2)
#
# print(li1.union(li2))


#合集反交集
# li1={1,2,3,4,5}
# li2={4,5,6,7,8}
#
# print(li1 ^ li2)
# print(li1.symmetric_difference(li2))


#合集的差集

# li1={1,2,3,4,5}
# li2={4,5,6,7,8}
#
# print(li1 - li2)
# print(li1.difference(li2))


#去重办法
li= [1,3,5,4,5,45,2,6,2,3]
li1=set(li)
li = list(li1)
print(li)