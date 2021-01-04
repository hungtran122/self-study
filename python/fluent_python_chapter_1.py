import collections
import math

from utils import print_tab

##### Using namedtuple to contruct class with no methods
print("[+] Using namedtuple to contruct class with no methods")
Student = collections.namedtuple('Student', ['GPA', 'department'])
student_1 = Student(3.5, 'Economy')
student_2 = Student._make((3.9, 'Computer Science'))

print_tab("Student 1: " +  str(student_1))
print_tab("Student 2: " +  str(student_2))

##### Implementing special methods
print('[+] Implementing special methods')
class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __repr__(self):
		return f"Vector x: {self.x}, y: {self.y}"
	def __str__(self):
		return f"Vector x: {self.x}, y: {self.y}"
	def __abs__(self):
		return math.sqrt(self.x ** 2 + self.y ** 2)
	def __bool__(self):
		return bool(abs(self))
	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x,y)
	def __mul__(self, other):
		x = self.x * other.x
		y = self.y * other.y
		return Vector(x,y)

v1 = Vector(2,3)
v2 = Vector(5,6)
print_tab("v1*v2: " + str(v1*v2))