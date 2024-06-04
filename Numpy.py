import numpy as np

print(np.__version__)
arr = np.array([1,2,3,4,5]) # create array
print(arr)
print(type(arr))

#create tuple

tup = np.array((1,2,3,4,5))
print(tup)

#2D

arr = np.array([[1,2,3],[4,5,6]])
print(arr)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#more then 3 dimension

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)


#indexing

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0][-1])

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0][1][2])

#slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

print(arr[::2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])

#datatype

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)


arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

#reshape

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)

#iterator

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
  arr1 = np.array([1, 2, 3])

  arr2 = np.array([4, 5, 6])

  arr = np.stack((arr1, arr2), axis=1)

  print(arr)

  arr1 = np.array([1, 2, 3])

  arr2 = np.array([4, 5, 6])

  arr = np.hstack((arr1, arr2))

  print(arr)

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)

arr = np.array([1,2,3,4,5,6])

newarr = np.array_split(arr,4)
print(newarr)

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)

#reaser an array

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

arr = np.array([True, False, True])

print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))

#apply folter

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

from numpy import random
x=random.randint(100, size=(5))

print(x)

x = random.randint(100, size=(3, 5))

print(x)

x = random.rand(5)

print(x)

x = random.rand(3, 5)

print(x)

x = random.choice([3, 5, 7, 9])

print(x)

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)

x = random.choice([1,2,3,4,5], p=[0.1, 0.5, 0.3, 0.1, 0.0], size = (3,5))

print(x)

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))

import matplotlib.pyplot as plt

import seaborn as sb

#sb.distplot([1,2,3,4,5,6], hist=alse)

#plt.show()

#normal deviaion

x = random.normal(size=(2, 3))

print(x)
x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)

#sb.distplot(random.normal(size = 1000), hist = False)

#plt.show()

x = random.binomial(n=10, p=0.5, size=10)
#sb.distplot(random.binomial(n=10, p=0.5, size=1000), hist = True, kde = False)
print(x)

#plt.show()

#sb.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
#sb.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

#sb.distplot(random.poisson(lam=2, size=1000), kde=False)
#print(random.poisson(lam=2, size=1000))
#plt.show()
"""sb.distplot(random.uniform(size=1000), hist=False)
sb.distplot(random.logistic(size=1000), hist=False)
sb.distplot(random.exponential(size=1000), hist=False)
sb.distplot(random.chisquare(df=1, size=1000), hist=False)

sb.distplot(random.rayleigh(size=1000), hist=False)
sb.distplot(random.pareto(a=2, size=1000), kde=False)
sb.distplot(x[x<10], kde=False)

#plt.show()
plt.show()"""


#ufunc

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)

print(newarr)

arr = np.trunc([-3.1666, 3.6667])

print(arr)

arr = np.fix([-3.1666, 3.6667])

print(arr)

arr = np.around(3.1666, 2)

print(arr)

arr = np.floor([-3.1666, 3.6667])

print(arr)

arr = np.ceil([-3.1666, 3.6667])

print(arr)

arr = np.arange(1, 10)

print(np.log2(arr))

arr = np.arange(1, 10)

print(np.log10(arr))

arr = np.arange(1, 10)

print(np.log(arr))

#nplog = np.frompyfunc(log, 2, 1)

#print(nplog(100, 15))


arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])

print(newarr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr)

print(np.lcm(4,8))
print(np.lcm.reduce([2,4,8,16,20]))

print(np.gcd(4,8))
print(np.gcd.reduce([2,4,8,16,20]))
#plt.show()

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)

arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)

print(x)

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)

print(x)

x = np.arcsin(1.0)

print(x)

x = np.sinh(np.pi/2)

print(x)

x = np.arcsinh(1.0)

print(x)

arr = np.array([0.1, 0.2, 0.5])

x = np.arctanh(arr)

print(x)

#set operation
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)

print(x)