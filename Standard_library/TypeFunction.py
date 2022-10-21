'''
Input - one onject
Output - type of a given input(int, string, float, et
'''

r = range(0, 30)
print(type(r))
print(type(10))
print(type("a"))
print(type("Hi there"))

'''
isisntance()
Input = one object and one class info
output - Boolean representing whether or not the object is a instance of the class given by class info
    objects is an instance of the class -> True
    object is not an instance of the class -> False
'''
class Car:
    pass

class Truck(): # class Truck(Car):
    pass

c = Car()
t = Truck()
convert = Car()
print(type(c))
print(type(t))
print(type(c) == type(t)) # False
print(type(c) == type(convert)) # True
print(isinstance(c, Car)) # True
print(isinstance(t, Car)) # True Truck enheirant from Car
print(isinstance(t, Car))  # False because Truck no longer enheirants from Car

if isinstance(r, range):
    print(list(r))