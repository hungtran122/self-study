import matplotlib.pyplot as plt
import numpy as np

#########################################################
'''
TRANSFORM TUTORIALS 
'''
x = np.arange(0, 10, 0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
ax.plot(x, y)

xdata, ydata = 5, 0
xdisplay, ydisplay = ax.transData.transform((xdata, ydata))
bbox = dict(boxstyle='round', fc='0.8')
arrowprops=dict(arrowstyle='->', connectionstyle='angle, angleA=0, angleB=90, rad=10')
offset = 80
ax.annotate('data=(%.1f, %.1f)'%(xdata, ydata), (xdata, ydata), xytext=(-2*offset, offset), textcoords='offset points', bbox=bbox, arrowprops=arrowprops)
disp = ax.annotate('display=(%.1f, %.1f)'%(xdisplay, ydisplay), (xdisplay, ydisplay), xytext=(0.5*offset, -offset), xycoords='figure pixels', textcoords='offset points',
                   bbox=bbox, arrowprops=arrowprops)
plt.show()