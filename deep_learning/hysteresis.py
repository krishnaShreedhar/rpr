# Import matplotlib, numpy and math 
import matplotlib.pyplot as plt
import numpy as np
import math

x1 = np.linspace(-20, 20, 100)
z1 = 1 / (1 + np.exp(-x1))

x2 = np.linspace(-10, 20, 100)
z2 = 1 / (1 + np.exp(-(x2-10)))

plt.plot(x1, z1, 'b')
plt.plot(x2, z2, 'b')
plt.xlabel("x")
plt.ylabel("Sigmoid(X)")

plt.show() 