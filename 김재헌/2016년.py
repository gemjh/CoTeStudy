# -*- coding: utf-8 -*-
"""2016년

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KdAmXJto7SHorOtiXExR4tzlzlXqbQuC
"""

from datetime import datetime, date
def solution(a, b):
    today=['MON','TUE','WED','THU','FRI','SAT','SUN']
    answer=today[date(2016,a,b).weekday()]
    return answer