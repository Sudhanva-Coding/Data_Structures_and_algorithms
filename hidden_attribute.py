class User:
    # hidden variable
    __password = "Abc@123"

    def __init__(self, name, email, Username):
        self.name = name
        self.email = email
        self.Username = Username

    def get_password(self):
        return(self.__password)

    def set_password(self):
        old_password = input("Enter your old password : ")
        if old_password == self.__password:
            new_password = input("Enter your new password : ")
            self.__password = new_password

        else:
            print("Please enter the correct password")

class Car:
    def __init__(self, brand, model, fuel, color):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.color = color

    def get_color(self):
        return(self.color)
    
    def set_color(self, newcolor):
        self.color = newcolor
    
    def showCar(self):
        print("Car - {} - {}, Fuel Type - {}, Color - {}".format(self.brand, self.model, self.fuel, self.color))

class SUV(Car):
    def __init__(self, brand, model, fuel, color, transmission, turbo):
        Car.__init__(self, brand, model, fuel, color)
        self.transmission = transmission
        self.turbo = turbo

    def showCar(self):
        print("Car - {} - {}, Fuel Type - {}, Color - {}, Transmission - {}, Turbo True/False - {}".format(self.brand, self.model, self.fuel, self.color, self.transmission, self.turbo))


# concept of hidden variable
Sudhanva = User("Sudhanva","sudhanvaakshay7@gmail.com", "Sudhanva12")
print(Sudhanva.name)
#print(Sudhanva.__password)
print(Sudhanva.get_password)
print(Sudhanva.set_password)

# Concept of inheritance
Ford = SUV("Ford", "Cortina", "Petrol", "Black", "Manual", True)
print(Ford.get_color())
Ford.set_color("Red")
Ford.showCar()

        



    