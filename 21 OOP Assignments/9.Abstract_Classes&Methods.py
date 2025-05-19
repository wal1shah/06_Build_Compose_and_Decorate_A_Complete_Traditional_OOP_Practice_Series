from abc import abstractmethod, ABC

class Shape((ABC)):
    
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
x = Rectangle(5,5)
print(x.area())