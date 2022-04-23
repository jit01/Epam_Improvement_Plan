""" Understanding of Descriptor in python using 3 types of examples

Defination :
Descriptor follow 3 different methods namely
__getters__(),
__setters__(),
__delete__()

If any of the above methods are defined to object,
we can say its as a descriptor.
Descriptors are just basic storage system,
you can use this for validate values that are being assigned to value.


.__get__(self, obj, type=None) : This attribute is called when you want to retrieve the information (value = obj.attr),
and whatever it returns is what will be given to the code that requested the attribute’s value.

__set__(self, obj, value) : This method is called to set the values of an attribute (obj.attr = 'value'),
and it will not return anything to you.

__delete__(self, obj) : This method is called when the attribute is deleted from an object (del obj.attr)
"""

"""
Descriptor Example :
In this Example a data descriptor sets and returns values normally and prints a message logging their access.
Code 1:
"""


class Descriptor(object):

    def __init__(self, name=''):
        self.name = name

    def __get__(self, obj, objtype):
        return "{}".format(self.name)

    def __set__(self, obj, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be string")


class EPAM(object):
    name = Descriptor()


e = EPAM()
e.name = "epam"
print(e.name)

"""
Creating a Descriptor using property() :
property(), it is easy to create a usable descriptor for any attribute. Syntax for creating property()

property(fget=None, fset=None, fdel=None, doc=None)
Code 2:
"""


class Descriptor1:
    def __init__(self, value):
        self._value = value

        # getting the values

    def getValue(self):
        print('Getting value')
        return self._value

        # setting the values

    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value

        # deleting the values

    def delValue(self):
        print('Deleting value')
        del self._value

    value = property(getValue, setValue, delValue, )


# passing the value
x = Descriptor1('epam')
print(x.value)
x.value = 'epam'
del x.value

"""
Creating a Descriptor using @property Decorator :
In this we use the power of property decorators which are a combination of property type method and Python decorators.
Code: 3
"""


class Descriptor2:
    def __init__(self, value):
        self._value = value

        # getting the values

    @property
    def value(self):
        print('Getting value')
        return self._value

        # setting the values

    @value.setter
    def value(self, value):
        print('Setting value to ' + value)
        self._value = value

        # deleting the values

    @value.deleter
    def value(self):
        print('Deleting value')
        del self._value

    # passing the value


x = Descriptor2('Ethan')
print(x.value)

x.value = 'Hunt'
del x.value


"""
Output:
epam
Getting value
epam
Setting value to epam
Deleting value
Getting value
Ethan
Setting value to Hunt
Deleting value
"""