# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 22:43:09 2021

@author: minaya.karimova
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())
list1=list()
list2=list()
copied_list1=list()
newlist = list()
counter = 0
    
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if i+j+k != n:
                list1.append(i)
                list1.append(j)
                list1.append(k)
                print(list1)
                copied_list1 = list1.copy()
                list2.insert(counter, copied_list1)
                counter = counter + 1
                list1.clear()
                
print('LIST2')
print(list2)
                

             


              
