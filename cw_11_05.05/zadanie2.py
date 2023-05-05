import numpy as np
import matplotlib.pyplot as plt

np.random.seed(121345)

series = np.random.rand(5, 50)

color = ['r', 'b', 'g', 'y', 'm']
marker = ['o', '^', 's', 'D', 'v']

def randrange(n,vmin,vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 50
for i in range(5):
    xs = randrange(n, 0, 50)
    ys = randrange(n, 0, 50)
    ax.scatter(xs, ys, series[i], c=color[i], marker=marker[i])

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()