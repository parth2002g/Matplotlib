import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,6])
ypoints = np.array([0,250])

#plotting with line

plt.plot(xpoints, ypoints)
plt.show()

#plotting without line

plt.plot(xpoints, ypoints, 'o')
plt.show()

#plotting multiple points

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

#not specfying x point

xpoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(xpoints)
plt.show()