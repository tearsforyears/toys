#coding=utf-8
import os, sys
print("回生")
# os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
os.system("python "+os.path.abspath(__file__))