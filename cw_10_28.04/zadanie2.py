import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 21, 1)
y = 1/x

plt.plot(x, y,  'g^:', label='f(x) = 1/x')
plt.axis([0, 20, 0, 1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(loc=1)
plt.show()