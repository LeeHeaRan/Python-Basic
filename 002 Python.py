#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=10
while a<15:
    print('helloword')
    a+=1
    
a2=1
while a2<5:
    print('hi', end =' ')
    if a2>9:
        break
    a2+=1
else:
    print('good job')


# In[5]:


a3=1
while True:
    print('hi2', end = ' ')
    if a3>9:
        break
    a3+=1


# In[7]:


l = [10,20,30,40]
for i in l:
    print(i)


# In[9]:


set = {10,20,30,40,50,60}
for i in set:
    print(i)


# In[11]:


dictionary = {'one':10, 'two': 20}
for i in dictionary:
    print(i)


# In[18]:


print(type(range(10)))
print(1, list(range(10)))
print(2, list(range(5,10)))
print(3, list(range(2,10,2)))
print(4, list(range(10,5,-1)))
print(5, list(range(-10)))


# In[23]:


for i in 'hello':
    print(i)

for i in range(10):
    print(i, end =' ')
else:
    print('good job')
    
for i in range(10):
    print(i, end = ' ')
    if i==5:
        break
else:
    print('good job')


# In[24]:


l = list(range(101))
print(l)


# In[45]:


ll = []
for i in range(10):
    ll.append(i)
print(ll)

lll = [i for i in range(10)]
print(lll,'\n')

for i in range(2, 10):
    for j in range(1, 10):
        print('{}*{}={}'.format(i, j, i*j), end = ' ')
        
llll = ['{}*{}={}'.format(i, j, i*j) for i in range(2,10) for j in range(1,10)]
print('\n\n',llll)
        


# In[48]:


l = [(1,10), (2,20), (3,30), (4,40)]
for i, j in l:
    print(i,j)

for i, j in enumerate(range(100, 1000, 100), 1):
    print(i,j)


# In[52]:


for i in range(10):
    pass
    print('hello word1')
    
for i in range(10):
    continue
    print('hello word2')
    
for i in range(10):
    if i>5:
        continue
    print('hello word3')


# In[56]:


a =1
if a>10:
    print('hello word')
elif a<20:
    print('goob job')
else:
    pass

a =25
if a==10:
    print('hi 1')
elif a<20:
    print('hi 2')
elif a<30:
    print('hi 3')
elif a<40:
    print('hi 4')
elif 5<20:
    print('hi 5')
else:
    print('else')  


# ## Part 4 Class

# In[59]:


class Car(object):
    maxSpeed = 300
    maxPeople = 5
    def start(self):
        print('start')
    def stop(self):
        print('stop')

class Hybrid(Car):
    battery = 10000
    batteryKM = 300
    
k9 = Car()
k5 = Car()
k3 = Hybrid()

print(type(k9))
#print(dir(k9))
print(k9.maxPeople)
print(k5.maxSpeed)
print(k3.maxPeople)

