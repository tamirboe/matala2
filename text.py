-- coding: utf-8 --
"""
Created on Sun Mar 28 08:43:20 2021

@author: Tamir
"""


def revword(word: str) -> str:
    n = ""
    for i in range(len(word) - 1, -1, -1):
        n = n + word[i]

    return n.lower()


def countword() -> int:
    file = open('text.txt')
    firstline = file.readline().replace("\n", "")
    count = 1
    for line in file:
        line = line.rsplit()
        for word in line:
            word = revword(word)
            if word._eq_(firstline):
                count = count + 1
    return count
