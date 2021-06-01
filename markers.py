import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

#point marker
plt.plot(ypoints, marker = 'o')

plt.show()

#star marker
plt.plot(ypoints, marker = '*')

plt.show()

#marker and line
plt.plot(ypoints, 'o:r')

plt.show()

#marker style
plt.plot(ypoints, marker = '*', ms=20)

plt.show()

#marker colour 
plt.plot(ypoints, marker = '*', ms=20, mec='r')

plt.show()