import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.title('sin(t) и cos(t)')
plt.plot(x, y_sin, label='sin(t)')
plt.plot(x, y_cos, label='cos(t)')
plt.legend()
plt.show()
