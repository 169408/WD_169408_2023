import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 21, 1)
y = 1/x

plt.plot(x, y, label='f(x) = 1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(loc=1)
plt.show()

