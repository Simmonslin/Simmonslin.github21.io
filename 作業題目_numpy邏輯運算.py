#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# 作業目標<br>
# 熟悉邏輯運算<br>
# 作業重點<br>
# 五大類邏輯函式與其對應的函式操作

# 題目:<br>
# english_score = np.array([55,89,76,65,48,70])<br>
# math_score = np.array([60,85,60,68,55,60])<br>
# chinese_score = np.array([65,90,82,72,66,77])<br>
# 上3列共六位同學的英文、數學、國文成績，第一個元素代表第一位同學，舉例第一位同學英文55分、數學60分、國文65分，運用上列數據回答下列問題。<br>
# 1. 有多少學生英文成績比數學成績高?
# 2. 是否全班同學最高分都是國文?
# 
# 
# 

# In[ ]:


import numpy as np


# In[6]:


#1.有多少學生英文成績比數學成績高

import numpy as np

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])

ans=english_score>math_score

c=0
for i in range(len(ans)):
    if ans[i]==True:
        c+=1
        
print("有 %d 位學生英文成績比數學成績高" % c)

        
        


# In[19]:


#2.是否全班同學最高分都是國文?

import numpy as np

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])


vs1=np.greater(chinese_score,english_score)
vs2=np.greater(chinese_score,math_score)

c=0

c2=0
    
for i in range(len(vs1)):
    if vs1[i]==vs2[i]==True:
        print("是")
        c+=1
        if c>=1:
            break
            
    else:
        print("否")
        c2+=1
        if c2>=1:
            break
        
        



# In[ ]:




