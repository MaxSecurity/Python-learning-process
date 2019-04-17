#!./usr/bin/env.python
#.-*- coding: utf-8 -*-
#._author_.=."Max丶"
#._Email:_.=."max@chamd5.org"


# 想要在函数内修改a=x需要global 一下啊那个变量名案例如下
#global 定义完成后下面所有函数调用a时候都是按照global修改后的值
# a=1
#
# def func():
#     global a
#
#     a += 1
# func()
# print(a)
#
# def test():
#     global a
#     a = 1
#
# test()
# print(a)
#
# def test2():
#     print(a)
#
# test2()

#global这个办法是非常不好的我们可以用更好的办法进行修改

a = 1
def test3(a):
    a = 2
    return a

shucu = test3(a)
print(shucu)
