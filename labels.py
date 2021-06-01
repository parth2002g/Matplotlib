import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)

font1 = {'family':'serif','color':'red','size':20}
font2 = {'family':'Apple Chancery','color':'blue','size':15}

plt.title("Sports Watch Data", fontdict = font1, loc = 'left')

plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.grid(color = 'red', linestyle = '--', linewidth = 0.5)

plt.show()