class MobilePhone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def make_call(self):
        print(f"calling from {self.brand} {self.model}...")
    
    def display_battery(self):
        print(f"Battery: {self.battery}%")
        
phone1 = MobilePhone("Samsung", "Galaxy S24", 82)
phone1.make_call()
phone1.display_battery()

phone2 = MobilePhone("Apple", "iPhone 14 Pro Max", 90)
phone2.make_call()
phone2.display_battery()
