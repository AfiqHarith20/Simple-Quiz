#!/usr/bin/env python
# coding: utf-8

# In[34]:


class Square:
    side = 1.0
    
    def __init__(self,side):
        self.side = side
        
    def setSide(self):
        if (self.side == 0 ):
            return self.side == 1
        
        elif (self.side <= 0):
            return 0
            
        else:
            return (self.side)
            
a = Square(1)
print(a.setSide())


# In[ ]:





# In[ ]:




