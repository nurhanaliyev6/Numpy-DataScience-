#view veri_manipulasyonu.ipynb in google colab



import numpy as np

#ndim
#shape
#size
#dtpe

random_numbers=np.random.randint(10,size=10)
print(2*random_numbers)
print("Random number between 0-10:")
print(random_numbers)

print("dimension of array: ",random_numbers.ndim)
print("Size of array: ",random_numbers.size)
print("shape of array: ",random_numbers.shape)
print("dtype of array: ",random_numbers.dtype)

print("Two dimesnion---------------------------------------")
random_numbers2=np.random.randint(10,size=(3,5))
print("dimension of array: ",random_numbers2.ndim)
print("Size of array: ",random_numbers2.size)
print("shape of array: ",random_numbers2.shape)
print("dtype of array: ",random_numbers2.dtype)



#---------------------------------------------------------------

#reshape array

aranger=np.arange(0,10)

print(aranger)

print(aranger.reshape((2,5)))

print(aranger.shape)

#---------------------------------------------------------------


#concat array

arr=np.arange(1,4,1)
arr2=np.arange(4,7,1)

print(arr)
print(arr2)
print("Concated: ")
print(np.concatenate([arr,arr2]))
concated_arr=np.concatenate([arr,arr2])

#two dimension
arr3=np.array([[1,2,3],
              [4,5,6]])
print(np.concatenate([arr3,arr3],axis=0))
print("---------------------------------")
print(np.random.randint(10,size=(3,3,2)))

#----------------------------------------

print("---------------------------------")


x=np.array([1,2,3,4,5])
a,b,c=np.split(x,[2,4])
print(a,b,c)

m=np.arange(16).reshape(4,4)
print(m)
print(np.vsplit(m,[2]))

#------------------------------------------

ar=np.random.randint(0,12,12).reshape(3,4)

print(ar[0,0])
print(ar)

#fancy index-----------
print("fancy_index")