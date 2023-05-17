#!/usr/bin/env python
# coding: utf-8

# Q1. Create one variable containing following type of data:
# (i) string
# (ii) list
# (iii) float
# (iv) tuple

# In[11]:


#string
string_sample = "Saola olaoluwa"
#list
list_sample = [1,2,3,4, "pheranmiey", "Enya"]
#float
float_sample = 123.4444
#tuple
tuple_sample = (1,2,3)


# In[ ]:





# Q2. Given are some following variables containing data:
# (i) var1 = ‘ ‘
# (ii) var2 = ‘[ DS , ML , Python]’
# (iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
# (iv) var4 = 1.

#  Ans:
#  var1 = string,
#  var2 = string,
#  var3 = list,
#  var4 = float

# In[ ]:





# Q3. Explain the use of the following operators using an example:
# (i) /
# (ii) %
# (iii) //
# (iv) **

# In[14]:


div=4/2
mod = 1223%234
floor_div = 345//32
power = 2**3


# In[17]:


print(div, mod, floor_div, power)


# In[ ]:





# Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
# element and its data type.

# In[21]:


my_stack = ['new age', 'enya', 'celtic', 'woman', 23.44, False, 'may', 17, 2023, 4+5j]


# In[22]:


for val in my_stack:
    print(val)
print('this is the end of my list')


# In[ ]:





# Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
# times it can be divisible.

# In[34]:


a= 1888
b =4


# In[39]:


while a%b ==0:
    div = int(a/b)
    print(f'a is purely divisible by b {div} times')
    break
else:
    print('a is not purely divisible by b')


# Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
# divisible by 3 or not.

# In[22]:


num = [25]

for n in num:
    if n%3==0:
        print('element is divisible by 3')
        
    else:
        print('element is not divisible by 3')


# Q7. What do you understand about mutable and immutable data types? Give examples for both showing
# this property.
# 
# 
# You have an immutable object if you can't change the object's state after you've created it. In contrast, a mutable object allows you to modify its internal state after creation

# # Mutable

# In[15]:



list__ = [1,3,4,9]
list__


# In[16]:


list__[2] = 'giraffe'
list__


# # Immutable 

# In[17]:


name = 'Feranmi'
name


# In[18]:


name[0]


# In[19]:


name[0] = 'y'

