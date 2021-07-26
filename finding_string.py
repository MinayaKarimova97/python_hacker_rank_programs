# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 14:57:57 2021

@author: kerim

In this challenge, the user enters a string and a substring. You have to print the number of 
times that the substring occurs in the given string. String traversal will take place from 
left to right, not from right to left. 
"""

def count_substring(string, sub_string):
    count = 0
    substr_len = len(sub_string)
    for i in range(0, len(string)):
        number = string.find(sub_string) 
        if number!=-1 :
            count = count + 1
        
        string = string[number+(substr_len-1):]
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)