# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:53:17 2020

@author: AD(HJC)
"""


def solution(data, n):
    # Your code here
    data.reverse()
    for val in data:
      num=data.count(val)
      if(num>n):
        for i in range(num):
          data.remove(val)
    data.reverse()
    return(data)
