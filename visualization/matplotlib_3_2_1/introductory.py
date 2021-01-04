import numpy as np
import pandas as pd
import matplotlib as mlp
from matplotlib import pyplot as plt
import os
from matplotlib_3_2_1.templates import *
import matplotlib
# matplotlib.use('qt5agg')

'''
##########################################

cur_dir = os.path.dirname(__file__)
df = pd.read_csv('../dev_salary_by_age.csv')
fig, ax = plt.subplots(1,1)
out = my_plotter(ax, df['Age'].values, df['Python'].values, {'label':'Python', 'marker': 'o', 'markevery': 10})
out = my_plotter(ax, df['Age'].values, df['JavaScript'].values, {'label':'JavaScript', 'marker': '.'})
ax.set_xlabel('Salary in USD')
ax.set_ylabel('Age')
ax.axis([10,60,0,130000])
ax.legend()
plt.show()

##########################################
# Plotting with keywords (data)

data = {'a': np.arange(50),
        'c': np.random.randint(0,50,50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('a entry')
plt.ylabel('b entry')
plt.show()

##########################################
# Working with multiple figures
plt.style.use('fivethirtyeight')
def f(t):
	return np.exp(-t)*np.cos(2*np.pi*t)
t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)
plt.figure('1st figure')
plt.subplot(211)
plt.plot(t1, f(t1),'bo', t2, f(t2),'k')
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2),'r--')

plt.figure('2nd figure')
plt.subplot(211)
plt.plot(t1, f(t1),'bo', t2, f(t2),'k')
plt.grid(True)
plt.show()

###########################################
# Lifecycle of a Plot
from matplotlib.ticker import FuncFormatter
def currency(x, pos):
	if x>1e6:
		s='${:1.1f}M'.format(x*1e-6)
	elif x>1e3:
		s='${:1.0f}K'.format(x*1e-3)
	else:
		s = '$'.format(x * 1e-3)
	return s
formatter = FuncFormatter(currency)

plt.rcParams.update({'figure.autolayout':True})
data = {'Bartorn LLC': 109438.50,
        'Apple': 135841.99,
		'Fritsch, Russel and Anderson': 112214.71,}
names = list(data.keys())
revenue = list(data.values())
rc_context = {
	'xtick.color': 'red',
	'axes.facecolor':'black',
	'xtick.minor.size': 3,
	'axes.spines.right':False,
	'axes.spines.top': False,
	'axes.grid':True,
	'axes.grid.which': 'both'
}
with plt.rc_context(rc_context):
	fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10,6))
	ax.barh(names, revenue)
	labels = ax.get_xticklabels()
	plt.setp(labels, rotation=45, horizontalalignment='right')
	ax.set(xlabel='Revenue', ylabel='Company', title='Company Revenue')
	ax.xaxis.set_major_formatter(formatter)
plt.show()
'''
###########################################
'''
1. create figure with two axes
2. plot line in 1st axes
3. plot bar in 2nd axes
4. plot pie in 3rd axes
5. change some axes params using rc_context
6. modify ticks and ticklabels
7. format axis ticklabels
'''
from matplotlib.ticker import FormatStrFormatter
df = pd.read_csv('../dev_salary_by_age.csv')
print(df.head())
py_sal = df['Python'].values
ja_sal = df['JavaScript'].values
x = np.arange(len(py_sal))
py_mean = np.mean(py_sal)
ja_mean = np.mean(ja_sal)
all_mean = np.mean(df['All_Devs'])
py_max = np.max(py_sal)
ja_max = np.max(ja_sal)
all_max = np.max(df['All_Devs'])
py_min = np.min(py_sal)
ja_min = np.min(ja_sal)
all_min = np.min(df['All_Devs'])


plt.rcParams.update({'figure.autolayout': True})
# print(plt.rcParams.keys())
rc_context = {'xtick.color': 'b',
               'axes.grid':True,
              'xtick.bottom': False,
              }
plt.style.use('seaborn')
with plt.rc_context(rc_context):
	fig, ax = plt.subplots(3, 1, figsize=(15,15))
	ax[0].plot(x, py_sal, label='Python', color='r', linestyle='-.', marker='o', linewidth=1, markevery=5)
	ax[0].plot(x, ja_sal, label='JavaScript', color='y')
	formatter = FormatStrFormatter('$%1.0f')
	ax[0].tick_params(axis='y', rotation=45)
	ax[0].set_xticks(np.arange(0, 40, 5))
	ax[0].set_xlabel('Age')
	ax[0].set_ylabel('Income')
	ax[0].yaxis.set_major_formatter(formatter)
	ax[0].locator_params(nbins=3)
	ax[0].legend()

	width = 0.25
	ax[1].bar(np.arange(3), [all_mean, py_mean, ja_mean], label='Mean', color='b', width=width)
	ax[1].bar(np.arange(3) + width, [all_max, py_max, ja_max], label='Max', color='r', width=width)
	ax[1].bar(np.arange(3) - width, [all_min, py_min, ja_min], label='Min', color='r', width=width)
	ax[1].set_xlabel('Language')
	ax[1].set_ylabel('Income')
	ax[1].set_xticks([0,1,2])
	ax[1].set_xticklabels(['All', 'Python', 'JavaScript'])
	# ax[1].legend(loc=(0.01, 1.01))
	ax[1].legend(loc='best')

	# pie chart
	x = [500, 800, 1200]
	explode=[0.01, 0.01, 0.05]
	# explode: relative distance of parts to the center
	# autopct: format string value
	# wedgeprops: dict of properties of wedge
	ax[2].pie(x, labels=['Python', 'Java', 'C++' ], explode=explode, startangle=150, autopct='%2.2f%%', wedgeprops={'edgecolor': 'blue'}, shadow=True)
	ax[2].legend(loc=(0.01, 1.01))
	plt.tight_layout()
	plt.show()