# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : python_cmd.py
# Time       ：2022/4/21 15:22
# Author     ：Gao Shan
# Description：
"""
# system函数可以将字符串转化成命令在服务器上运行；其原理是每一条system函数执行时，其会创建一个子进程在系统上执行命令行，子进程的执行结果无法影响主进程；
# 上述原理会导致当需要执行多条命令行的时候可能得不到预期的结果；
import os

os.system('cd /usr/local')
os.mkdir('aaa.txt')
# 上述程序运行后会发现txt文件并没有创建在/usr/local文件夹下，而是在当前的目录下；

# 使用system执行多条命令
#
# 为了保证system执行多条命令可以成功，多条命令需要在同一个子进程中运行；


#os.system 执行多条命令
os.system('cd /usr/local && mkdir aaa.txt')
# 或者
os.system('cd /usr/local ; mkdir aaa.txt')

# 基于上述使用的扩展使用：
#
# 模拟环境： 在服务器上启动守护进程，直接启动也会有异常退出，毕竟守护进程也是有重启次数的，
# 这个时候就可以， 单独创建一个启动文件，用启动文件启动 程序。
# 再用守护进程启动这个 启动文件，做个异常处理，可以保证稳定启动

import os,time

def start():
  try:
    os.system('cd /usr/local && scrapy crawl yourSpiderName')
    # 或者
    os.system('cd /usr/local ; scrapy crawl yourSpiderName')
  except Exception as e:
    print('MyErrorAtStart:  %s' % e)
    time.sleep(10)
    start()
if __name__ == '__main__':
    start()

# os.system ()出现乱码,因为pycharm控制台用的是UTF-8编码,而系统返回的GBK的文字,所以乱码

a=os.system('ping www.baidu.com')
print(a)#0
b=os.system('ping 172.0.0.1')
print(b)# 如果是0,则表示成功,如果是1,则表示失败
# os.system 的返回值 如果是0,则表示成功,如果是1,则表示失败