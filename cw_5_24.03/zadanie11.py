import numpy as np

vec = np.array([4, 10, 8, 12, 1, 3, 4, 9, 12, 11, 2, 2])

print(vec)

mac1 = vec.reshape(3, 4)

print(mac1)

mac2 = vec.reshape(4, 3)
mac3 = vec.reshape(2, 6)

print(mac2)
print(mac3)

print(mac1.flatten())
print(mac2.flatten())
print(mac3.flatten())