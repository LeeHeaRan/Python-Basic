#!/usr/bin/env python
# coding: utf-8

# ## part 1

# In[ ]:


x= 3
y=10
print(x+y)
#hello world
'''hello world'''


# In[9]:


a = 10
b =10.1
c='hello world'
d = -1
e = 'lee'
f = 'heyran'
g = 10+2j
h = 0b1001
i = 0o1001
j = 0x1001
print(a+b)
print(type(a))
#print(dir(a))


# In[16]:


s = 'paullab CEO LeeHeyRan'
print(type(s))
print(s[0])
print(s[0:7])
print(s[0:15:2])
print(s[10:0:-1])
print(s[:10:2])
print(s[::2])
print(s[::-1])
print(s[-1])
print(s[::]) #print(s)


# In[23]:


s = 'paullab CEO LeeHeyRan'
ss= '       CEO      '
print(type(s))
#print(dir(s))
print(s.upper())
print(s.lower())
print(s.count('l'))
print(ss.strip())
print(ss.rstrip())
print(ss.lstrip())
a = (s.split(' '))
print(a)
print('!'.join(a))
print('my name {} and age is {}'.format('이혜란', 22))
print('my name {1} and age is {0}'.format('이혜란', 22))


# In[27]:


a=2019
b=9
c=24
print(a,b,c, sep='/', end=' ')
print(a,b,c)


# In[29]:


a=10
b='10'
print(a+int(b))
print((str(a)+b))


# In[34]:


a=True
b=False
print(type(a))
#print(dir(a))

print(bool(' '))
print(bool(''))
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(None))


# In[37]:


a=3 
b=10
print(a+b)
print(a-b)
print(b/a)
print(b//a)
print(b*a)
print(b**a)
print(b%a)


# In[38]:


#비교연산
#논리연산
#할당연산
#bit연산


# In[40]:


def f(x,y):
    z= x+y
    return z
print(f(3,5))


# In[44]:


def ff():
    print('1')
    print('2')
    print('3')
print('4')
ff() #왜 여기에서는 리턴값인 None이 안나올까?
print('-------')
def fff():
    print('1')
    print('2')
print('3')
print(4)
print(fff())
print('-------')
def ffff():
    print('1')
    print('2')
    return None
print('3')
print(4)
print(ffff())


# In[51]:


def circle(radius):
    return (radius*radius*3.14)
print(circle(10))


# In[63]:


a=10
def aplus():
    global a
    a +=10
    return a #왜 return a+=10 은 안될까?
print(aplus())


# ## part 2 리스트, 튜플, 딕셔너리, 셋

# In[57]:


list = [100,200,300,400]
print(list)
print(type(list))
#print(dir(list))
print(list[1])
list[1] = 500
print(list[1])


# In[61]:


list = [100,200,300,400]
print(type(list))
#print(dir(list))
print(list)
list.append(300)
print(list)
list.extend([100,200,300])
print(list)
print(list.count(300))
print(list.index(200))
list.insert(3, 1000)
print(list)
list.pop()
print(list)
list.remove(1000)
print(list)


# In[70]:


tuple01 = (100,200,300)
print(type(tuple01))
#print(dir(tuple))
print(tuple01)
list =[10,20]
tuple02 = (list, 100,200,300)
print(tuple02)


# In[76]:


set01 = {100, 200, 300, 300, 300}
print(type(set))
#print(dir(set))
print(set)
set02 = {1,2,3}
set01.add(500)
print(set01)
print(set01.union(set02))
#print(set('aabbcdddddeefggg'))


# In[88]:


dictionary ={'one':10, 'two': 20}
print(type(dictionary))
#print(dir(dictionary))
print(dictionary['one'])
print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())
#list = list(dictionary.items())
#print(list)


# In[90]:


jeju = {'banana':5000, 'orange':2000}
seoul = jeju.copy()
jeju['orange']=100000
print(seoul)
print(jeju)

