#!./usr/bin/env.python
#.-*- coding: utf-8 -*-
#._author_.=."Max丶"
#._Email:_.=."max@chamd5.org"

txt = open('hosts.txt')#打开hosts文件
list = txt.read().split('\n') #定义一个list  list等于txt打印切片以换行为分隔符也就是,
print(list)#打印list
txt.close()#结束txt
with open('host.txt', 'r+') as f: #打开写入host  with后面接的对象返回的结果赋值给f
    for i in list:#我们循环list
        # print(i.split(',')[0])#(以，为分割取0位置上的值)
        f.write(i.split(',')[0]+'\n')   #f.write也就是写入
print('OJBK!!!')
