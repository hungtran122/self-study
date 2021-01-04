# Transforming Code into Beautiful, Idiomatic Python
# https://www.youtube.com/watch?v=OSGv2VnC0go

# Else in for loop
print('Else case in for loop')
seq = range(100)
def find(value, target):
	for i in target:
		if i == value:
			break
	else:
		return -1
	return i
print('\t',find(1000, seq))

# Working with dictionary
names = ['Dung', 'Trang', 'Tuan', 'Manh']
ages = [20, 15, 23, 21]
# Construct a dictionary
print('Construct a dictionary')
name_age = dict(zip(names, ages))
name_list = dict(enumerate(names))
print('\t',name_age, name_list)
# Loop over a dictionary
print('Loop over a dictionary')
def find_start_char(start_char, target):
	for k, v in target.items():
		if k.startswith(start_char):
			break
	else:
		return -1
	return k, v
print('\t', find_start_char('D', name_age))

# Counting list members with dictionaries
names = ['Dung', 'Tuan', 'Trang', 'Dung', 'Tuan', 'Hung', 'Dung', 'Trang']
print('Counting and Grouping with a dictionary')
d_count = {}
d_group = {}
for name in names:
	d_count[name] = d_count.get(name, 0) + 1
	key = len(name)
	d_group[key] = d_group.setdefault(key, []).append(name)
print('\t Counts', d_count)
print('\t Groups', d_group)
