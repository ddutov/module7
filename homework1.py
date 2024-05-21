# -*- coding: utf-8 -*-

hw1 = 'homework1.txt'
file = open(hw1, mode='r')
hw1_content = file.read()
file.close()
print(hw1_content)
