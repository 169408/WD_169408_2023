import numpy as np
import matplotlib.pyplot as plt

x1 =np.arange(0.0,30.0,0.1)
x2 =np.arange(0.0,30.0,0.1)

y1 =np.sin(x1)+2
y2 =np.sin(-x2)


plt.plot(x1, y1, label='sin(x)')
plt.plot(x2, y2, 'orange', label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend(loc=1)
plt.show()