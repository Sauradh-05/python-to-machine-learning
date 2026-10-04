class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def Calculate_area(self):
        return self.length * self.width
    
rect1 = Rectangle(5, 3)
print("Area", rect1.Calculate_area())
