class Person:
    def __init__(self,name):
        self.name=name
    def introduce(self):
        print(f"Hi, I'm {self.name}.")

class Customer(Person):
    def __init__(self, name,address):
        super().__init__(name)
        self.address=address
    
    def place_order(self,item):
        self.item=item

class Driver(Person):
    def __init__(self, name,vehical):
        super().__init__(name)
        self.vehical=vehical
    
    def deliever(self,order):
        print(f"{self.name} is delivering {Customer.place_order} to {self.name} using {self.name}")
        self.order=order
        order="delivered"

class DeliveryOrder:
    def __init__(self,customer,item):
        self.customer=customer
        self.item=item
    
    def status():
        status="preparing"
        print(status)
    
    def assign_driver(self,driver):
        self.driver=driver
    
    def summary():
        print("delivered")

customer1name="Alice"
customer1order="Laptop"
customer2name="Bob"
customer2order="Headphones"
drivername="David"
customer1address= "applestreet"
customer2address="orangestreet"
drivervehical="motorcycle"

Alice=Customer(customer1name,customer1address)
Bob=Customer(customer2name,customer2address)
David=Driver(drivername,drivervehical)
Aliceorder=DeliveryOrder(customer1name,customer1order)
Boborder=DeliveryOrder(customer2name,customer2order)
Alice.introduce()
Bob.introduce()
David.introduce()
print(" ")
print("Order Summary: ")
print(f"Item: {Alice.place_order(customer1order)}")
print(f"Customer:{Alice.name}")
print(f"Status: {Aliceorder.status}")
print(f"Driver: {David.name}")
print(" ")
print("Order Summary")
print(f"Item: {Bob.place_order(customer1order)}")
print(f"Customer:{Bob.name}")
print(f"Status: {Boborder.status}")
print(f"Driver: {David.name}")
print(David.deliever(Aliceorder))
print(David.deliever(Boborder))
print(" ")
print("Final Status: ")
print("Order for Laptop → delivered")
print("Order for Headphones → delivered")






    
 