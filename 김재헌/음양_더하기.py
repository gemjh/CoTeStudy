# -*- coding: utf-8 -*-
"""음양 더하기.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uQjQYSkEdUCPFeqeUPdPsDXcMPPH6WUM
"""

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer+=absolutes[i]
        else:
            answer-=absolutes[i]
    return answer