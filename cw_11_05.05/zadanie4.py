import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 4))
ax1 = fig.add_subplot(421, projection='3d')
ax2 = fig.add_subplot(422, projection='3d')
ax3 = fig.add_subplot(423, projection='3d')
ax4 = fig.add_subplot(424, projection='3d')
ax5 = fig.add_subplot(425, projection='3d')
ax6 = fig.add_subplot(426, projection='3d')
ax7 = fig.add_subplot(427, projection='3d')
ax8 = fig.add_subplot(428, projection='3d')

_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1

ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
ax1.set_title('Wykres zacieniony')
ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
ax2.set_title('Wykres nie zacieniony')
ax3.bar3d(x+1, y+2, bottom, width, depth, top, shade=True, color='r')
ax3.set_title('Wykres zacieniony')
ax4.bar3d(x+1, y+2, bottom, width, depth, top, shade=False, color='r')
ax4.set_title('Wykres nie zacieniony')
ax5.bar3d(x, y, bottom, width, depth, top, shade=True, color='g')
ax5.set_title('Wykres zacieniony')
ax6.bar3d(x, y, bottom, width, depth, top, shade=False, color='g')
ax6.set_title('Wykres nie zacieniony')
ax7.bar3d(x, y, bottom, width, depth, top, shade=True, color='y')
ax7.set_title('Wykres zacieniony')
ax8.bar3d(x, y, bottom, width, depth, top, shade=False, color='y')
ax8.set_title('Wykres nie zacieniony')

plt.show()