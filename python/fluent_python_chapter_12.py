from utils import print_tab
outline = ''' CHAPTER 12: Inheritance: For Good or For Worse
OUTLINE:
• The pitfalls of subclassing from built-in types which use C implementation
• Multiple inheritance and the method resolution order
'''
print('Subclassing from built-in types such as list, dict do not allow you to override the superclass methods'.upper())
class SomeDict(dict):
	def __getitem__(self, item):
		return 100 # always return 100 no matter what

somedict  = SomeDict(a = 'hello')
d = {}
d.update(somedict)
print_tab(f'Check getitem: {somedict["a"]}')
print_tab(f'getitem in dict init will ignore getitem inplementation in SomeDict class: {d["a"]}')
print_tab(f'All problems can be fixed if we subclass from collections.UserDict class')

print('METHOD RESOLUTION ORDER')
class A():
	def msg(self):
		return 'This is class A'

class B():
	def msg(self):
		return 'This is class B'

class C(A,B):
	def msg(self):
		return super().msg()
c = C()
print_tab(f'Using msg function in class C will invoke msg of class A: {c.msg()}')
print_tab(f'If you want to trigger msg function of B class you should call B.msg(c): {B.msg(c)}')
print_tab(f'Check method resolution order by __mro__: {C.__mro__}')

def print_mro(cls):
	# this function to print mro of a given class
	print_tab(', '.join([c.__name__ for c in cls.__mro__]))
print_mro(C)

print(f'HOW TO DO MULTIPLE INHERITANCE')
s = '''
1. Distinguish Interface Inheritance from Implementation Inheritance
    • Inheritance of interface creates a subtype, implying an “is-a” relationship.
	• Inheritance of implementation avoids code duplication by reuse.
2. Make Interfaces Explicit with ABCs
    In modern Python, if a class is designed to define an interface, it should be an explicit ABC.
3. Use Mixins for Code Reuse
    If a class is designed to provide method implementations for reuse by multiple unrelated
    subclasses, without implying an “is-a” relationship, it should be an explicit mixin class.
	Conceptually, a mixin does not define a new type; it merely bundles methods for reuse.
	A mixin should never be instantiated, and concrete classes should not inherit only from
	a mixin.
4. Make Mixins Explicit by Naming
    There is no formal way in Python to state that a class is a mixin, so it is highly recommended
    that they are named with a ...Mixin suffix.
5. An ABC May Also Be a Mixin; The Reverse Is Not True
    Because an ABC can implement concrete methods, it works as a mixin as well. An ABC
    also defines a type, which a mixin does not.
6. Don’t Subclass from More Than One Concrete Class
	Concrete classes should have zero or at most one concrete superclass.
7. Provide Aggregate Classes to Users
	If some combination of ABCs or mixins is particularly useful to client code, provide a
	class that brings them together in a sensible way
	class Widget(BaseWidget, Pack, Place, Grid):
		pass
	The body of Widget is empty, but the class provides a useful service
8. “Favor Object Composition Over Class Inheritance.”
    Once you get comfortable with inheritance, it’s too easy to overuse it
    Favoring composition leads to more flexible designs.
'''
print_tab(s)

s = '''SUMMARY:
• Subclassing from built-in classes (such as list, tuple) has some pitfalls and is not recommended
• Recommending to subclass from collections.abc (such as MutableSequence, Sequence, Sized)
• Method resolution order show the order of multiple inheritances. MRO will decide which methods will be inherited in case of same method names cross superclasses
• 8 disciplines to do inherit  
'''
print(s)
