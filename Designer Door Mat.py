# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 13:54:12 2021

@author: kerim

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat 
with the following specifications:

    Mat size must be 

X. ( is an odd natural number, and is times
.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

"""
n1,n2=map(int,input().split())


fillchar='-'
word_string = "WELCOME"
string1 = ".|."
string2=string1
n=3
n3=n1-2
flag=0

for i in range(n1):
    if i==(n1//2):
        print(word_string.center(n2, fillchar))
        flag=1
    elif flag==0:
        print(string2.center(n2, fillchar))
        string2 = string1*n
        n=n+2
    elif flag==1:
        string3=string1*n3
        n3=n3-2
        print(string3.center(n2, fillchar))
        
    
    
    
        
    
    