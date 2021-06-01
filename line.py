import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

#dotted
plt.plot(ypoints, linestyle = 'dotted')
plt.show()

#dashed
plt.plot(ypoints, linestyle = 'dashed')
plt.show()

#dotted
plt.plot(ypoints, ls = ':')
plt.show()