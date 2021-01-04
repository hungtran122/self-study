from cycler import cycler
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# print(mpl.rcParams.keys())

########################################################
'''
STYLING WITH CYCLER
'''
# rc_context = {'xtick.color': 'black', 'lines.linewidth': 4, 'figure.autolayout': True}
# with plt.rc_context(rc_context):
#
# 	x = np.linspace(0, 2*np.pi, 50)
# 	offsets = np.linspace(0,2*np.pi, 4, endpoint=False)
# 	yy = np.transpose([np.sin(x+phi) for phi in offsets])
# 	default_cycler = (cycler(color=['r', 'g', 'b', 'y']) + cycler(linestyle=['-', '--', ':', '-.']))
# 	custom_cycler = (cycler(color=['b', 'r', 'g', 'y']) + cycler(lw=[1,2,3,4]))
# 	fig, ax = plt.subplots(2,1)
# 	ax[0].set_title('rgby scheme color')
# 	ax[0].set_prop_cycle(default_cycler)
# 	ax[0].plot(x, yy)
#
# 	ax[1].set_title('brgy scheme color')
# 	ax[1].set_prop_cycle(custom_cycler)
# 	ax[1].plot(x, yy)
# 	plt.show()
########################################################
'''
CUSTOMIZING FIGURE LAYOUTS USING GRIDSPEC AND OTHER FUNCTIONS
'''
'''
# 2x2 grid
# import matplotlib.gridspec as gridspec
# fig = plt.figure(constrained_layout=True)
# spec = gridspec.GridSpec(nrows=2, ncols=2, figure=fig)
# ax1 = fig.add_subplot(spec[0,0])
# ax2 = fig.add_subplot(spec[0,1])
# ax3 = fig.add_subplot(spec[1,0])
# ax4 = fig.add_subplot(spec[1,1])
# plt.show()

# allocate axes to gridspec with different width, height
# fig = plt.figure(constrained_layout=True)
# spec = fig.add_gridspec(3,3) # same as spec = gridspec.GridSpec(nrows=3, ncols=3, figure=fig)
# ax1 = fig.add_subplot(spec[0, :])
# ax1.set_title('spec[0,:]')
#
# ax2 = fig.add_subplot(spec[1, :-1])
# ax2.set_title('spec[1,:-1]')
#
# ax3 = fig.add_subplot(spec[1:, -1])
# ax3.set_title('spec[1,-1]')
#
# ax4 = fig.add_subplot(spec[-1, 0])
# ax4.set_title('spec[-1,0]')
#
# ax5 = fig.add_subplot(spec[-1, -2])
# ax5.set_title('spec[-1,-2]')
#
# plt.show()

# allocate axes to gridspec using lists of widths and heights
fig = plt.figure(constrained_layout=True)
widths = [1,1,1]
heights = [1,2,3]
spec = fig.add_gridspec(nrows=3, ncols=3, width_ratios=widths, height_ratios=heights)
axs = []
for r in range(len(heights)):
	for c in range(len(widths)):
		ax = fig.add_subplot(spec[r,c])
		txt = f'w:{widths[c]}, h: {heights[r]}'
		ax.annotate(txt, (0.1, 0.5), xycoords='axes fraction', va='center')
		axs.append(ax)
plt.show()
'''

'''
TIGHT LAYOUT
'''
x = np.linspace(0, 2*np.pi, 20)
y = np.sin(x)
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(5,5))
fontsize = 12
ax[0,0].plot(x, y)
ax[0,0].set_title('SIN', fontsize=fontsize)
ax[0,0].set_xlabel('X', fontsize=fontsize)

y = np.cos(x)
ax[1,0].plot(x, y)
ax[1,0].set_title('COS', fontsize=fontsize)
ax[1,0].set_xlabel('X', fontsize=fontsize)
y = np.tan(x)
ax[0,1].plot(x, y)
ax[0,1].set_title('TAN', fontsize=fontsize)
ax[0,1].set_xlabel('X', fontsize=fontsize)
y = np.cos(x + np.pi/2)
ax[1,1].plot(x, y)
ax[1,1].set_title('COS', fontsize=fontsize)
ax[1,1].set_xlabel('X + pi/2', fontsize=fontsize)
fig.tight_layout(pad=3.0, w_pad=1.0, h_pad=1.0)
plt.show()