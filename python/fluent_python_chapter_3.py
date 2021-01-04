from collections import defaultdict, UserDict

from utils import print_tab

### USE defaultdict TO HANDLE MISSING KEYS
print("USE defaultdict TO HANDLE MISSING KEYS")
dd = defaultdict(list)
country_city = [('HaNoi', 'VietNam'), ('Tokyo', 'Japan')]
for city, country in country_city:
    dd[country].append(city)
country_city = [('HaiPhong', 'VietNam'), ('Osaka', 'Japan')]
for city, country in country_city:
    dd[country].append(city)
print_tab(dd)

### USE UserDict TO CREATE A NEW MAPPING CLASS
print('USE UserDict TO CREATE A NEW MAPPING CLASS')
class StrKeyDict(UserDict):
    '''
    A MAPPING TYPE WHICH ONLY ACCEPT KEY AS STRING TYPE
    '''
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    def __contains__(self, item):
        return str(item) in self.data
    def __setitem__(self, key, value):
        self.data[str(key)] = value
