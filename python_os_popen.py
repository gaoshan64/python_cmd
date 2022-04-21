# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : python_os_popen.py
# Time       ：2022/4/21 15:36
# Author     ：Gao Shan
# Description：
"""
import os

p=os.popen('ipconfig')
print("p.read()",p.read())

