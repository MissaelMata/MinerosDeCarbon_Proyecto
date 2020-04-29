#!/usr/bin/env python
# coding: utf-8

# In[1]:


grip = [
    [0,0,0,0,5,0,0,4,9],
    [0,0,0,0,7,3,8,5,0],
    [3,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [8,9,3,1,0,0,2,0,4],
    [6,0,0,3,9,0,5,0,0],
    [0,4,0,6,2,0,0,0,0],
    [0,0,6,8,0,9,0,0,0],
    [1,0,0,0,0,0,0,0,0]
]


# In[2]:


import numpy as np

def posible(y,x,n):
    global grip
    for i in range(0,9):
        if grip[y][i] == n:
            return False
    for i in range(0,9):
        if grip[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grip[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global grip
    for y in range(9):
        for x in range(9):
            if grip[y][x] == 0:
                for n in range(1,10):
                    if posible(y,x,n):
                        grip[y][x] = n
                        solve()
                        grip[y][x] = 0
                return
    print(np.matrix(grip))


# In[3]:


import pandas as pd

df = pd.read_csv('sudoku.csv',nrows=1)

df = df['puzzle']


table = []
for idP, p in df.items():
    print(p)
    
idx = 0
for i in range(9):
    row = []
    for j in range(9):
        row.append(int(p[idx]))
        idx+=1
    table.append(row)

        
for row in table:
    print(row)
    
    
grip = table


# In[4]:


solve()


# In[5]:


grip1 = [
    [1,2,3,4,5,6,7,8,9],
    [2,3,4,5,6,7,8,9,1],
    [3,4,5,6,7,8,9,1,2],
    [4,5,6,7,8,9,1,2,3],
    [5,6,7,8,9,1,2,3,4],
    [6,7,8,9,1,2,3,4,5],
    [7,8,9,1,2,3,4,5,6],
    [8,9,1,2,3,4,5,6,7],
    [9,1,2,3,4,5,6,7,8]
]

# extreme 27
# easy    36
# medium  31
# hard    25

