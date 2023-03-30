import numpy as np

tab = np.array(([4, 2, 14], [42,  10, 1]))
a = np.sin(tab)
print(a)

tab2 = np.array(([13, 2, 8], [98,  25, 1]))
b = np.cos(tab2)
print(b, "\n")

print(a+b)