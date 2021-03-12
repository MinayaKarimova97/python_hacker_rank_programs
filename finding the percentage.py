# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:24:40 2021

@author: minaya.karimova


"""
list1 = list()
list2 = list()
list3 = list()
list4 = list()
string = ""
s=0
n=0

for n in range(int(input())):
    string = input()
    list1.append(string)

name = input()


for i in range(n+1):
    list2.append(list1[i])
    #list to string
    string = ""
    for x in list2:
        string += x

    #string to list
    list3 = string.split()
    
    if list3[0] == name:
        list4 = list3[1:]
        n=len(list4)
        for i in list4:
            num = float(i)
            s=s+num
        
    list2.clear()

avg=s/n
#Add zeros to a float after the decimal point in Python
print(format(float(avg), '.2f'))