
# coding: utf-8

# In[1]:


#連続した5つの整数の積が平方数になるかチェックするためのコード
import numpy as np
import math

n = 6
while n < 3000:
    a = n*(n-1)*(n-2)*(n-3)*(n-4)
    b = math.sqrt(a)
    print(isinstance(b, int))
    n += 1


# In[2]:


import numpy as np
import math

n = 6
while n < 3000:
    a = n*(n-1)*(n-2)*(n-3)*(n-4)
    b = math.sqrt(a)
    print(b)
    n += 1

