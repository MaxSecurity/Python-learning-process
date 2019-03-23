#!./usr/bin/env.python
# .-*- coding: utf-8 -*-
# ._author_.=."Max丶"
# ._Email:_.=."max@chamd5.org"

#查询0位置是什么
# li= ['max','max2','sec','anquan']
# l1= li[0]
# print(l1)


# 在列表里面添加写法 关键点是.append


# while 1:
#     username= input('>>>')
#     if username.strip().upper()== "Q":#.strip().upper()意思是无视大小写无视空格输入q就可以直接pass
#      break
#     else:
#         li.append(username)
# print(li)

# 随意插入位置：关键点.insert  插入位置从0开始数数到那个位置在加1就可以在那个位置后面插入
# while 1:
#     username= input('>>>')
#     if username.strip().upper()== "Q":
#      break
#     else:
#         li.insert(3,username)
# print(li)

# 删关键是.pop
# li = ['max', 'max2', 'sec', 'anquan']

# li.pop(1)
# print(li)

#查看删除的是什么又返回值随便定义一个名称让它等于.pop删除的通过print打印name可以知道删除的是什么
# name=li.pop(1)
# print(name,li)

#什么都不写默认删最后一个
# name=li.pop()
# print(name,li)

#按照元素删除关键字.remove
# li.remove('max')
# print(li)

# #清空这个列表我们可以用.clear
# li.clear()
# print(li)


# li = ['max', 'max2', 'sec', 'anquan']

# #还有一种毁尸灭迹的删除方法那就是 del
# del li
# print(li)

#切片删除  顾头不顾尾所以说只需要前面两个从0开始数数到那个位置在加1就可以截取那个位置上的了
# del li[2:]
# print(li)
#如果需要删前两个
# del li[0:2]
# print(li)

#如果想修改里面怎么改？直接修改
# li[0]='baibai'
# print(li)

#还有一种类型修改切片修改：
# li[0:3]='akhdsadhakd'
# print(li)

# li = ['max', 'max2', 'sec', 'anquan']

# #for循环查询所有元素
# for i in li:
#     print(i)

#for切片查询元素 查询输出是列表
# for i in li:
#     print(i)
# print(li[0:2])


#公共方法查询元素方法
# #第一种办法：查询有几位元素
# li = ['max', 'max2', 'sec', 'anquan']
# s =len(li)
# print(s)
# #第二种方法查询某个元素出现几次
# max23=li.count('max')
# print(max23)
# #第三种：查询某个元素的位置
# print(li.index('sec'))


# #排序方法
# #正向排序
# li= [1,3,2,4,5,4,8,6,0,9,7]
# li.sort()
# print(li)


# #反向排序
# li= [1,3,2,4,5,4,8,6,0,9,7]
# li.sort(reverse=True)
# print(li)

#反转排序：
# li= [1,3,2,4,5,4,8,6,0,9,7]
# li.reverse()
# print(li)


#列表嵌套
#查找列表里面的太这个字输出
# li = ['max', '李太白', '浩哥',['tianji','name',89],23]
# sun=li[1][1]
# print(sun)
#查找列表里面的太这个字输出第二种写法
# print(li[1][1])

#找到max大写M然后放回去 知识点：.capitalize()把首字母大写
# li = ['max', '李太白', '浩哥',['tianji','name',89],23]
# name=li[0].capitalize()
# #print(name)
# li[0] =name
# print(li)

#找到浩哥改成浩弟弟
#第一个办法直接改
# li = ['max', '李太白', '浩哥',['tianji','name',89],23]
# li[2]='浩弟弟'
# print(li)
#第二个办法 关键点replace()方法语法：把需要替换的写在前面把需要的写在后面就好了
# li = ['max','李太白','浩哥',['tianji','name',89],23]
# li[2]=li[2].replace('哥','弟弟') #这一句意思是找到li[2]元素也就是浩哥 把他的哥替换成弟弟然后重新赋给li[2]变成浩弟弟
# print(li)

#把tianji修改成全部大写放回去 (知识点获取列表中的列表是这样[3][0]不是[3[0]])
# li = ['max', '李太白', '浩哥',['tianji','name',89],23]
# li[3][0]=li[3][0].upper()
# print(li)

