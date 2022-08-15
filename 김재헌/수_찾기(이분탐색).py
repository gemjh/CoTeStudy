# -*- coding: utf-8 -*-
"""수 찾기(이분탐색).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uQjQYSkEdUCPFeqeUPdPsDXcMPPH6WUM
"""

N=int(input())
A_list=list(map(int,input().split()))
M=int(input())
A_list.sort()
Question=list(map(int,input().split()))

# N=5
# A_list=[4,1,5,2,3]
# A_list.sort()
# M=6
# Question=[1,3,7,9,2,5]

for i in Question:
  start=0
  end=N-1
  mid=(end+start)//2
  while True:
    print(start,mid,end)
    if i in [A_list[start],A_list[mid],A_list[end]]:
      print(1)
      break  
    elif mid in [start,end]:
      print(0)
      break        
    if i<A_list[mid]:
      end=mid
      mid=(end+start)//2
    else:
      start=mid
      mid=(end+start)//2