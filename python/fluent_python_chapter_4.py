from utils import print_tab
### BYTES ESSENTIALS
print('BYTES ESSENTIALS')
# string to bytes is encoding,  bytes to string is decoding
cafe = bytes("đứng", encoding='utf-8')
print_tab(f'{cafe}, length = {len(cafe)}')
print_tab(f'{cafe.decode(encoding="utf - 8")}, length = {len(cafe.decode(encoding="utf-8"))}')

print('Bytes is immutable, Bytearray is mutable')
b = bytes("hello", encoding='utf-8')
b_array = bytearray(b)
print_tab(b)
print_tab(b_array)

print('STRUCT AND MEMORYVIEW')
print('Struct let you parse packed bytes into a tuple of values based on predefined format. Or it can do opposite converting from values to packed bytes')
print('Memoryview do not create a new buffer, but provides shared memory access to slices of data')

import struct
fmt = '3s3sHH' # 3s3s two sequence of 3 bytes, HH two short integer 16bits
with open('gif_img.gif', 'rb') as f:
    img = memoryview(f.read()) # no copy here
header = img[:10] # slicing, no copy here
print_tab(f'Pointer at: {header}, Byte values: {bytes(header)}')
print_tab(f'Unpacked by struck: {struct.unpack(fmt, header)}')

print('Understanding Encode/Decode Problems'.upper())
print('Handling Encode Errors')
city = 'São Paulo'
print_tab(f'Original character: {city}')
print_tab(f"uft-8 encoding: {city.encode('utf-8')}")
print_tab(f"uft_16 encoding: {city.encode('utf_16')}")
# print_tab(f"cp437 encoding: {city.encode('cp437')}")
print_tab(f"cp437 encoding, ignore errors: {city.encode('cp437', errors='ignore')}") #ignore error
print_tab(f"cp437 encoding, replace bad char with ?: {city.encode('cp437', errors='replace')}") #ignore error
print('Handling Decode Errors')
octets = b'Montr\xe9al'
print_tab(f"cp1252 decoding: {octets.decode('cp1252', errors='replace')}")
print_tab(f"uft-8 decoding: {octets.decode('utf-8', errors='replace')}")
print('Olá, Mundo!')

print('HANDLING TEXT FILES')
print('While handling text files, always explicitly use encoding argument. Because different os might use different encoding by default')
open('text.txt', 'w',  encoding='utf-8').write('xin chào mọi người')
print_tab(open('text.txt', encoding='utf-8').read())
print('Check encoding defaults')
expressions = """
locale.getpreferredencoding()
type(my_file)
my_file.encoding
sys.stdout.isatty()
sys.stdout.encoding
sys.stdin.isatty()
sys.stdin.encoding
sys.stderr.isatty()
sys.stderr.encoding
sys.getdefaultencoding()
sys.getfilesystemencoding()
"""
my_file = open('dummy', 'w')
for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))

print('NORMALIZE UNICODE FOR STRING COMPARISON')
from unicodedata import normalize
s1 = 'café'
s2 = 'cafe\u0301'
print_tab(f's1: {s1}, s2: {s2}')
print_tab(f'Compare s1 vs s2: {s1==s2}')
print_tab(f'Compare s1 vs s2 after normalized: {normalize("NFC", s1) == normalize("NFC", s2)}')

print('GOOD PRACTICE TO COMPARE STRING'.upper())
from unicodedata import normalize
def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)
def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())
print_tab(f'Compare s1 vs s2: {nfc_equal(s1, s2)}')

print('GOOD PRACTICE TO REMOVE DIACRITICS')
import unicodedata
import string
def remove_diacritic(txt):
    n_txt = normalize('NFD', txt)
    keep = []
    is_latin = False
    for c in n_txt:
        if unicodedata.combining(c) and is_latin:
            continue
        keep.append(c)
        if not unicodedata.combining(c):
            is_latin = c in string.ascii_letters
    ret = ''.join(keep)
    return unicodedata.normalize('NFC', ret)
Greek = 'Ζέφυρος, Zéfiro'
print_tab(f'Original text: {Greek}, after removed diacritics {remove_diacritic(Greek)}')

print('GOOD PRACTICE TO TRANSFORM TEXT TO ACSII')
order = '“Herr Voß: • 1⁄2 cup of Œtker ™ caffè latte • bowl of açaí.”'
single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—›""",
                           """'f"*^<''""--->""")
d = {
    '€': '<euro>',
    'Œ': 'OE',
    '™': 'TM',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
}
multi_map = str.maketrans(d)
multi_map.update(single_map)
def dewinize(txt):
    """Replace Win1252 symbols with ASCII chars or sequences"""
    return txt.translate(multi_map)
print_tab(f'Original text: {order}, ACSII text: {dewinize(order)}')

print('SORTING UNICODE TEXT, USING LOCALE, locale.strxfrm')
import locale
fruits = ['trung', 'tráng', 'trăng', 'trắng', 'trang']
locale.setlocale(locale.LC_COLLATE, 'vi_VN.utf8')
print_tab(f'Wrong sorted: {sorted(fruits)}, Correct sorted: {sorted(fruits, key=locale.strxfrm)}') # locale-aware comparison
print_tab('Sort string easier with pyuca lib')
import pyuca
coll = pyuca.Collator()
print_tab(f'Wrong sorted: {sorted(fruits)}, Correct sorted: {sorted(fruits, key=coll.sort_key)}') # locale-aware comparison

import inspect
print(inspect.getmembers('fluent_python_chapter_4', inspect.isfunction))