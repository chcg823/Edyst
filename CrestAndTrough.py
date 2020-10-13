#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Defining funtion to find max crest [value,index]
def maxCrest(arr):
    crest = [0,0] # seting default to [0,0]
    l = len(arr)
    i = 1
    while i < l-1:
        # using variable for easier understanding
        right = arr[i-1]
        current = arr[i]
        left = arr[i+1]
        
        if current > left and right < current:
            if left>=right and crest[0]<=current-right:
                crest[0] = current-right
                crest[1] = i
                
            if right>left and crest[0]<=current-left:
                crest[0] = current-left
                crest[1] = i
        i+=1
    return crest


# In[12]:


# Defining function to find min crest [value,index]
def minCrest(arr):
    crest = [max(arr),0]
    l = len(arr)
    i = l-2
    while i > 0:
        # using variables for easier understanding
        right = arr[i-1]
        current = arr[i]
        left = arr[i+1]
        
        if current>left and right<current:
            if left>=right and crest[0]>=current-left:
                crest[0] = current-left
                crest[1] = i
            if right>left and crest[0]>=current-right:
                crest[0] = current-right
                crest[1] = i
        i-=1
    return crest


# In[13]:


# Defining function to find max trough [value,index]
def maxTrough(arr):
    trough = [0,0]
    l = len(arr)
    i = 1
    while i < l-1:
        # using variabes for easier understanding
        left = arr[i-1]
        current = arr[i]
        right = arr[i+1]
        if left>current and current<right:
            if left>=right and trough[0]<=left-current:
                trough[0] = left-current
                trough[1] = i
            if right>left and trough[0]<=right-current:
                trough[0] = right-current
                trough[1] = i
        i+=1
    return trough


# In[14]:


# Defining fucntion to find min trough [value,index]
def minTrough(arr):
    trough = [max(arr),0]
    l = len(arr)
    i = l - 2
    while i > 0:
        # using variables for easier understanding
        left = arr[i-1]
        current = arr[i]
        right = arr[i+1]
        if left>current and current<right:
            if left>=right and trough[0]>=right-current:
                trough[0] = right-current
                trough[1] = i
            if right>left and trough[0]>=left-current:
                trough[0] = left-current
                trough[1] = i
        i-=1
    return trough


# In[21]:


T = int(input())
while T:
    n = int(input())
    l = list(map(int, input().split()))
    max_c = maxCrest(l)
    min_c = minCrest(l)
    max_t = maxTrough(l)
    min_t = minTrough(l)
    if max_c==[0,0] or max_t==[0,0]:
        print(-1)
    else:
        #print("Max Crest :",max_c,"\nMin Crest :",min_c,"\nMax Trough :",max_t,"\nMin Trough :",min_t)
        print(max(abs(max_c[1]-min_c[1]),abs(max_t[1]-min_t[1])))
    T-=1


# In[ ]:





# In[ ]:





# In[ ]:




