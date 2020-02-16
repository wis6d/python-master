import numpy as np
import matplotlib.pyplot as pyplot

x = np.arange(-np.pi, np.py, np.py / 50)
sin_y = np.sin(x)
cos_y = np.cos(x)

plt.plot(x, sin_y, label='sin')
plt.plot(x, cos_y, label='cos')
plt.title('Sin/Cos Graph')
plt.xlabel('degree')
plt.ylabel('value')
plt.grid(which='major', axis='x', color='gray', alpha=0.5, linestyle='-', linewidth=1)
plt.grid(which='major', axis='y', color='gray', alpha=0.5, linestyle='-', linewidth=1)
plt.legend()
plt.show()
