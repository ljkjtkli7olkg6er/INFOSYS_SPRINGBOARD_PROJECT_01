class Car:
    #First function is constructor which is created using init function
    def __init__(self,user,brand):
        self.brand=brand
        self.user=user
    # after constructor you can name any  function
    def fullName(self):
        return f"{self.brand}{self.user}"
    

    # call car class in my_car object // where self is connector to the class
my_car=Car("tpyota","farari")
print(my_car.user)
 

your_car=Car("jerry","bmw")
print(your_car.user,your_car.brand)

# fullName is an func  which returns 
print(my_car.fullName())   


    
 # here Electric_car inherits Car class
class Electric_car(Car):
    def __init__(self,user,brand, battery_size):
        # super matlb apne se uppar (inheritance)
        super().__init__(self,user,brand)
        self.battery_size=battery_size

Electric=Electric_car("jay","kumar","35")
print(Electric.battery_size)



