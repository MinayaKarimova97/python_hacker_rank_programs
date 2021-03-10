# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:24:40 2021

@author: minaya.karimova

list1 = ['Harry', 37.21, 'Berry', 37.21, 'Tina', 37.2, 'Akriti', 41.0, 'Harsh', 37.21]



our_score = 37.21
n = len(list1)
pos = 0
k = 0

for item in list1:
    if item == our_score:
        print('yes')
        pos = list1.index(our_score, k)
        k = pos+1
        print(pos)
        
        
old_list = [[0,1,'f'], [4,2,'t'],[9,4,'afsd']]

#let's assume we want to sort lists by last value ( old_list[2] )
new_list = sorted(old_list, key=lambda x: x[2])
print("newlist")
print(new_list)

"""


list1 = list()
list2 = list()
listoflists = []
nested = [] 

for n in range(int(input())):
    name = input()
    score = float(input())
    listoflists.append(name)
    listoflists.append(score)
        
    
k = 0
ix = 0

while(ix <= len(listoflists)-2):
    nested.append(listoflists[ix:ix+2])
    ix += 2
        
new_list = sorted(nested, key=lambda x: x[1])
k=0
for i in range(n+1):
    if new_list[0][1] == new_list[k][1]:
        list1.append(new_list[k][0])
        k=k+1


m=len(new_list)-k
k_new=k

for i in range(m):
    if new_list[k][1] == new_list[k_new][1]:
        list2.append(new_list[k_new][0])
        k_new=k_new+1

        
list2.sort()

for i in range(len(list2)):
    print(list2[i])