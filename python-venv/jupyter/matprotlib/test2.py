import numpy as np
import matplotlib.pyplot as plt

#Prepare Data
x1 = np.linspace(0.0, 5.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
x2 = np.linspace(0.0, 3.0)
y2 = np.cos(2 * np.pi * x2) * np.exp(-x1)


# Figure instance
fig = plt.figure()
print(type(fig))

#ax1 instance
ax1 = fig.add_subplot(221)
ax1.plot(x1, y1)
ax1.set_title('line plot')
ax1.set_ylabel('Damped oscillation')
print(type(ax1))

#ax2 instance
ax2 = fig.add_subplot(222)
ax2.scatter(x1, y1, marker='o')
ax2.set_title('Scatter plot')

#ax3 instance
ax3 = fig.add_subplot(223)
ax3.plot(x2,y2)
ax3.set_ylabel('Damped oscillation')
ax3.set_xlabel('time (s)')

#ax4 instance
ax4 = fig.add_subplot(224)
ax4.scatter(x2, y2, marker='o')
ax4.set_xlabel('time (s)')

#Drawing
plt.show()  # pltでなくfigでも表示できる場合もあったが、pltでshow()するべきのようだ。
###fig.show()
