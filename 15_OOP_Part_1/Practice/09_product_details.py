class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def calculate_total(self, quantity):
        return self.price * quantity
    
    
product1 = Product("Laptop", 75000)

quantity = 2
 
print("Product:", product1.name)
print("Total Price:", product1.calculate_total(quantity))
 