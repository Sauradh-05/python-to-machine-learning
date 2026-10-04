class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"{self.brand} {self.model} ({self.year})")
        
car1 = Car("Toyota", "Fortuner", 2024)
car2 = Car("Hyundai", "Crete", 2025)

car1.display_info()
car2.display_info() 
        