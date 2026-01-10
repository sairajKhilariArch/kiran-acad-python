

class rectangle:
    
    
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return  2 * self.area()
    
    
    def diagonal(self):
        # return ((self.length * self.length ) + (self.width * self.width)) * 0.5 
        # return ((self.length**2)+(self.width**2))*0.5
        return self.perimeter()*0.5
    
    
    def details(self):
        area = self.area()
        perimeter = self.perimeter()
        diagonal = self.diagonal()
        
        data = f"""
Rectangle 
------------------------------------
Length      : {self.length}
Width       : {self.width}
Area        : {area}
Perimeter   : {perimeter}
Diagonal    : {diagonal}
        
        """
        return data
    
    
    
shape = rectangle(10,10)

# hi = circle.area()
# hi = circle.perimeter()
# hi = circle.diagonal()
hi = shape.details()

print(hi)



class circle:
    pi = 3.14
    
    def __init__(self,radius):
        self.radius = radius
        self.pi = 3.14
    
    
    def area(self):
        return self.pi * self.radius**2
    
    
    def circumference(self):
        return self.pi * self.radius * 2
    
    
    def pi_get(cls):
        return cls.pi
    
    def diameter(self):
        return 2* self.radius
    
    def details(self):
        radius = self.radius
        data = f"""

CIRCLE
----------------------
Radius          : {radius}
Area            : {self.area()}
Circumference   : {self.circumference()}
Diameter        :{self.diameter()}
PI              : {self.pi_get()}


        
        """

        return data




shape = circle(10)

# print(shape.area())
# print(shape.circumference())
# print(shape.pi())
print(shape.details())