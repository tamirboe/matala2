# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 08:43:20 2021

@author: Tamir
"""

def revword(word:str) ->str:
    i=len(word)
    for i in word:
        i=i-1
        new=i+word[i]
        
    return new.lower()
       

def countword() ->int:
    file= open('text.txt')
    first_line = file.readline()
    count=0
    for line in file:
        line=line.rsplit()
        for word in line:
            word= revword(word)
            if  word in first_line:
                count= count+1
    return(count)

   
      