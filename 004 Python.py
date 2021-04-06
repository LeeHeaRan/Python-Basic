#!/usr/bin/env python
# coding: utf-8

# ## Matplotlib의 이해

# In[7]:


import matplotlib.pyplot as plt#★
#plot() 직선, 꺽은선의 그래프
#show() 그래프 보여주기
xs=[1,2,3,4] #리스트
ys=[3,4,5,6]

plt.title('plotting') #그래프이름 title
plt.xlabel('x axis') #x축 이름 xlabel 
plt.ylabel('y axis') #y축 이름 ylabel
plt.plot(xs,ys)
plt.show()


# In[12]:


plt.plot(xs, ys, c='r') # color = 'red'와 동일. 'b', 'g', 'r', 'c', 'm', 'y', 'k', ‘w' 


# In[16]:


plt.plot(xs,ys,c='b', linestyle='--') # - -- -. :


# In[24]:


plt.plot(xs,ys,c='b',linestyle ='--', marker='s') #마커모양 변경 v . ^


# In[26]:


plt.plot(xs,ys,'r^--') #축약해서 사용하기. 색상 마커 선모양★


# In[27]:


plt.plot(xs,ys, 'r^--', label = 'main') # 그래프 업그레이드 label과 legend()외우기 ★★r이 아니라 l이다..
plt.legend(); #'main'이 범례의 이름이 된다.
plt.show();


# In[34]:


plt.plot(xs, ys,'g^--', label='main')
plt.xlim(0,10) #범위를 정한다. 제한. xlim
plt.ylim(5,10)
plt.legend()
plt.show()


# In[42]:


plt.scatter(x=[1,2,3,4,5], y=[2,4,6,8,10], s=30, alpha = 0.5, c='b', marker='.', label = 'example') 
#scatter는 plot와 반대로 점으로 표현한다. 축약형이 없다. s = 점의 크기 alpha = 컬러 투명도
plt.xlim(0,5)
plt.ylim(0.12)
plt.legend()
plt.show()


# #### 예제소스들

# In[40]:


import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0., 5., 0.2) # 0~5까까지 0.2단위로 생성.
plt.plot(t,t,'r1:',label='linear function')
plt.plot(t,t**2,'g<--',label='quadratic function')
plt.plot(t, t**3, 'b>-', label='cubic function')
plt.title('Graph')
plt.xlabel('xs')
plt.ylabel('ys')
plt.xlim(0, 5)
plt.ylim(0, 150)
plt.legend()
plt.show()


# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') #t,t 'r--' 그래프 t, t**2, 'bs'그래프 t,t**3,'g^'그래프  ★★★★★★
plt.xlabel('xs')
plt.ylabel('ys')
plt.xlim(0, 5)
plt.ylim(0, 150)
plt.title('Graph')
plt.legend()
plt.show()


# In[43]:


import matplotlib.pyplot as plt
plt.scatter(x=[1,2,3,4,5], y=[2,4,6,8,10], s=30, c='b',alpha=0.5, marker='.', label='example')
plt.scatter(x=[1,2,3,4,5], y=[8,9,10,11,12], s=30, c='r', alpha=0.5, marker='.', label='example_1')
plt.title('Scatter example')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0,5)
plt.ylim(0,12)
plt.legend()
plt.show()

