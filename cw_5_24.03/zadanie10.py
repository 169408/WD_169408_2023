import numpy as np

arr = np.arange(1, 82).reshape(9, 9)

print(arr)

arr_a = arr.reshape(1, 81)
arr_b = arr.reshape(81, 1)
arr_c = arr.reshape(3, 27)
arr_d = arr.reshape(27, 3)

print(arr_a)
print(arr_b)
print(arr_c)
print(arr_d)