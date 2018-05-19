#!/usr/bin/env python3
#coding:utf-8

#作者:daya
#许可:GPL
import re

Port ={}
Port1 =[]

f = open('mas.txt')
line = f.readline()
while line:
   Port[(re.search(r'port ([\d.]+)/tcp' , line)).group(1)]=line
   Port1.append(int((re.search(r'port ([\d.]+)/tcp' , line)).group(1)))
   #print((re.search(r'port ([\d.]+)/tcp' , line)).group(1))
   line =f.readline()
f.close()
Port1.sort()
for i in range(0,len(Port1)):
    print(Port[str(Port1[i])])