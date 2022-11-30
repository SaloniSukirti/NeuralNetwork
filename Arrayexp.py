import numpy as np


#Creating NumPy Arrays
x = [2, 4, 6, 8, 10]
arr = np.array(x)
print(arr)

y = [[1,2,3], [4,5,6], [7,8,9]]
arr = np.array(y)
print(arr)

arr = np.zeros((5,6))
print(arr)

arr = np.ones((5,6))
print(arr)

arr = np.random.random([3,2]) 
print(arr)

arr = np.arange(1,30,3)
print(arr)

arr = np.linspace(0,20,5)
print(arr)

print("_________________________________")

#Basic Array Operations
a = np.array([100,200,300])             #1D array
b = np.array([[20,25,30], [40,50,60]])  #2D array

np.add(a,b)
np.subtract(a,b)
np.multiply(a,b)
np.divide(a,b)

#NumPy Array Manipulation
#Reshaping an Array
#Creating another array within a given interval
np.arange(1,40,4)
np.arange(1,40,4).reshape(5,2)

#Transposing an Array
#Transposing a 2D array
arr = np.arange(1,40,4).reshape(5,2)
#Indexing Arrays
#Creating a 2D array of random numbers
arr = np.random.random((4,3))
print(arr)


#Creating an array
arr = np.arange(50)

#Slicing an Array
arr_slice = slice(12,42,2)   #(start,stop,step)
print(arr[arr_slice])

print(arr[3:13])

#Concatenating Arrays
arr1 = np.array([[1,2,3,4], [2,3,7,11]])
arr2 = np.array([[1,3,5,7], [2,4,6,8]])
 
 #Flattening an Array
arr = np.array([[20,25,30,35], 
                [40,50,60,70], 
                [45,48,51,54]])
 
np.ravel(arr)