len_var  = len("Hello world")

print(len_var)

lista = len([1,3,4,5,7])

print(lista)

max_length = max(1,5,7,69)

print(max_length)

sum_num = sum([1,4,5,6])

print(sum_num)

import math

class Shape:
    def area(Self):
        pass

    class Circle(Shape):
        def __init__(self,radius):
            self.radius = radius

            def area(self):
                return math.pi * self.radius ** 2
            
            circle = Circle(10)
            print("the area is:", circle.area())

