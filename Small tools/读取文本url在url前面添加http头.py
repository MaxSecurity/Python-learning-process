#!./usr/bin/env.python
#.-*- coding: utf-8 -*-
#._author_.=."Max丶"
#._Email:_.=."max@chamd5.org"

du = open('lob','r+',encoding='utf-8')  #打开一个txt
a ='' #定义一个空
du.seek(0)  #光标位置也就是在什么地方前添加
for i in du:
    data='http://'+i   #for循环添加http://
    a=data+a  #把修改好的文件放在a里面
    print(data)
with open('lob.txt','w') as xie:  #打开写入文本
    xie.write(a)  #把a里面文件写入

