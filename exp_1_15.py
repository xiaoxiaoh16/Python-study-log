#-*- coding: UTF-8 -*- ''
## SyntaxError: Non-ASCII character '\xe7' in file 
## 出现这种错误的原因是程序中的编码出问题了，只要在程序的最前面加上

## 直接输入argv变量到你的程序中而每次使用它时又不想打sys，
##  在使用 from xxx import * 时，如果想精准的控制模块导入的内容，可以使用 __all__ = [xxx,xxx] 来实现

from sys import argv

## script是脚本（xxx.py）文件名，filename 分别是第1个命令行参数
script, filename = argv

## 打开文件后的句柄复值给txt
txt = open(filename)

## 打印文件名
print "Here's your file %r:" % filename

## 打印文件内容
print txt.read()

## 打印
print "Type the filename again:"

## 接受用户输入文件名并复值给file_again
file_again = raw_input("> ")

## 打开文件后的复值给txt_again
txt_again = open(file_again)

## 打印文件内容
print txt_again.read()

# close file
txt.close()
txt_again.close()

