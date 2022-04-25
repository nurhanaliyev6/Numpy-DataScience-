
#numerical python
#for big arrays and matrix

#difference between list and numpyArray is that numpy is fixed only int or str. np.array([1,2,3]) array ->int fso

#list is mixed with str and int or other (not fixed) list[]=[1,2,3,4] 1 ucun ayri int,2 ucun ayri int, 3 ucun de

import numpy as np

a=[1,2,3]
b=[4,5,6]
#print(a*b) #not possible


A=np.array([1,2,3])
B=np.array([4,5,6])

print(A*B)

#-----------------------------------------------

year=np.array([2,0,0,1])
print(type(year))

year=np.array([2,0,0,1],dtype="float32")
print(year)
print(type(year))

#-------------------------------------------------

#sifirdan array yaratma

zeros=np.zeros(10,dtype=int)
print(zeros)

zeros2=np.zeros((4,3))
print(zeros2)

threes=np.full((4,3),3)#only 3
print(threes)

aranger=np.arange(0,10,3)
print(aranger)

ra=np.random.normal(10,2,(3,4))
print(ra)

