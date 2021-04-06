#!/usr/bin/env python
# coding: utf-8

# ## Numpy의 이해

# In[47]:


import numpy as np #요약어로 사용. 별명을 사용한다.
print(np.sqrt(2)) #루트함수
print(np.pi) 
print(np.sin(0)) #싸인 코사인
print(np.cos(np.pi))
print(np.random.random()) #램덤수를 생성


# In[41]:


import numpy as np
#랜덤클래스
a = np.random.rand(5) #0~1사이의 n개의 실수 생성
print(a)
print(type(a)) #타입확인
print("\n")

print(np.random.random())#실수 난수 생성
print(np.random.randint(1,100))#정수 난수 생성★
#print(np.random.choice('abcde')) #하나의 램던 항목 선택★
items =[1,2,3,4,5,6,7]
np.random.shuffle(items)#섞음★
print(items) 
print(np.random.choice(items))
print("\n")

print(np.random.choice(6,10)) # 0~(6-1)사이의 숫자를 10번 선택★★
print(np.random.choice(10,6, replace = False)) #중복★
print(np.random.choice(6,10, p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1])) #확률설정★


# In[51]:


import numpy as np
#Ndarray=N dimensonal array 다차원 행렬을 담는 ndarray클래스.
#차원은 요소element, 벡터vector, 매트릭스/행렬matrix, 행렬multidimensional matrix
a = np.empty(shape=[1,2], dtype= np.float32) #비어있는 1차원 요소 2개를 float32형으로 Ndarray를 생성.
print(a) 

f= np.array([1,2], dtype = np.bool)
print(f)
print(f.itemsize) #byte단위를 출력
print("\n")

#list와 ndarray의 
#공통점: []를 사용한다. 인덱싱과 슬라이싱이 가능
#차이점: ndarry는 ,가 없고 한가지 타입의 데이터만 저장가능. 숫자 문자가 함께 저장될시 문자로 저장된다.
a=np.array([1,2,3,4]) #list데이터
print(a[1], a[-1])
print(a[1:]) #list데이터를 ndarray타입의 배열로 변환

a=np.array([1,2,'3',4]) #모두 문자로 변환된다.
print(a)


# In[68]:


import numpy as np
#zero() ones() eye()함수
a = np.zeros(10) #0으로 초기화. ndarray 벡터
print(a)
b=np.zeros(shape =[1,2], dtype=np.int32) #정수로 초기화. ndarray 벡터
print(b)
b1=np.zeros(shape=[2,2], dtype=np.int32) #ndarray행렬
print(b1)
print("\n")

c=np.ones(10)
print(c)
d=np.ones(shape=[1,2], dtype=np.float64)
print(d)
e=np.ones(shape=[2,2], dtype=np.float64)
print(e)
print("\n")

f=np.eye(3) #3*3의 매트릭스(행렬)를 만듬. 대각선이 1로 이루어진다.
print(f)
print("\n")

#초기값이 3인 배열을 10개 만들기.
#배열에 연산/함수를 적용하면 모든 값에 한꺼번에 적용된다. (for문 사용X)
g=np.zeros(10)+3
print(g)
h=np.linspace(1,2,11)#1~2사이를 11구간으로 나눔
print(np.sqrt(g)) #루트를 씌움


# In[60]:


#arange()함수. 0과 1을 제외한 연속된 데이터를 생성. 
#np.arange([start], stop, [step], [dtype=None])
#start는 시작값, stop는 끝값, step은 증가값. 증가값은 안 쓸경우 1로 적용된다. []는 생략가능.
g= np.arange(0,1,0.1)
print(g)

print(np.arange(2)) #stop =3
print(np.arange(3,7)) #start=3 sopt=7★
print(np.arange(3,7,2)) #start =3, stop=7, step=2


# In[65]:


#linspace()함수. 특정구간을 쪼개어 값을 생성.
h=np.linspace(0,1,6)#start, stop, 구간의 수. 6개의 구간으로 나눈다.
print(h)
i=np.arange(-np.pi, np.pi, np.pi/10) 
j=np.linspace(-np.pi, np.pi, 20)
print(i)#-3.14~3.14 사이의 0,1제외의 10개의 데이터를 생성
print(j)#-3.14~3.14를 20개 구간으로 나눔.


# In[79]:


import numpy as np
import matplotlib.pyplot as plt
#ndarray로 그래프그리기.
a=np.arange(-np.pi, np.pi, np.pi/100)
plt.plot(a, np.sin(a))
plt.show()
b=np.arange(-np.pi, np.pi, np.pi/100)
plt.plot(b,np.sin(b))
plt.plot(b,np.cos(b))
plt.plot(b+np.pi/2, np.sin(b)) #오른쪽으로 수평이동
plt.show()


# In[84]:


#mask 기능. 어떤조건에 부합하는 데이터만 저장. 복수의 마스크를 연결하여 사용 가능.
import numpy as np
a=np.arange(-5, 5) #ndarray 벡터
print(a)
print(a<0) #t/f값의 마스크 생성
print(a[a<0])#마스크를 벡터에 적용
mask1 = abs(a)>3 #마스크를 변수에 저장한다.
print(a[mask1])
print("\n")

mask2=abs(a)%2 ==0 #짝수의 절대값
print(a[mask1+mask2]) # OR 둘중 하나라도 참일경우
print(a[mask1*mask2]) #AND 둘달 참일경우.

