# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : python_subprocess.py
# Time       ：2022/4/21 17:52
# Author     ：Gao Shan
# Description：
"""
import subprocess

hostname=subprocess.getoutput("hostname")

print(hostname)