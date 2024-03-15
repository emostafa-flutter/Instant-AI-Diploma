#!/usr/bin/env python
# coding: utf-8

# In[9]:


def do_while():
    while True:
        isContinue = input("Do you want to continue? (y/n): ")
        if isContinue.lower() != 'y':
            break
do_while()


# In[ ]:




