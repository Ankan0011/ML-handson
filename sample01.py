import numpy as np
import hashlib



matric =np.arange(15).reshape(3, 5)
print(matric)
x = 3
x = x + 0.5

print(type(x))
print(1,000,000)

matric = np.array([1,2], dtype= complex)
print (matric)

print(hashlib.md5((np.int64(34343434))).digest())
print(hashlib.md5((np.int64(34343434))).digest()[-1])
#np.dtype()

#numb = input("Enter a number: ")

#Dictionary (Key, Value)

d = {'cat':'cute' , 'dog':'not so cute'}
print(d['dog'])

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = a[1:, 1:3] #slicing ana array using index value
print(a)
print(b)
