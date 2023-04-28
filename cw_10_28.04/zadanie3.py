import numpy as np
import matplotlib.pyplot as plt

x1 =np.arange(0.0,30.0,0.1)
x2 =np.arange(0.0,30.0,0.1)

y1 =np.sin(x1)
y2 =np.cos(x2)


plt.plot(x1, y1, 'b', label='sin(x)')
plt.plot(x2, y2, 'y', label='cos(x)')
plt.xlabel('x')
plt.ylabel('y=sin(x), y=cos(x)')
plt.legend(loc=1)
plt.show()