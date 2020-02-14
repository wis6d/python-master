import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, np.pi / 50)
sin_y = np.sin(x)
cos_y = np.cos(y)

plt.plot(x, sin_y)
plt.plot(x, cos_y)
plt.show()

