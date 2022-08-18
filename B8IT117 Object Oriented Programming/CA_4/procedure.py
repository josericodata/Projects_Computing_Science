#CA 1
#Student Name: Jose Maria Rico Leal - 10539218
#Module Name: B8IT117 Object Oriented Programming
#Presentation Date: Tuesday 26th of October

#Creating the class for the procedure, setting up attributes.
class Procedure:
    def __init__(self,name,date,doctor,charge):
        self.__name = name
        self.__date = date
        self.__doctor = doctor
        self.__charge = charge
                                                #Using get method to return the objects inserted.
    def get_name(self):
        return self.__name
    def get_date(self):
        return self.__date
    def get_doctor(self):
        return self.__doctor
    def get_charge(self):
        return self.__charge
    
    def set_name(self,name):
        self.__name = name
    def set_date(self,date):
        self.__date = date
    def set_doctor(self,doctor):
        self.__doctor = doctor
    def set_charge(self,charge):
        self.__charge = charge
        
    def __str__(self):                          #Returning the values as how we will see them in the console
        return 'Name: ' + self.__name + \
               '\nDate: ' + self.__date + \
               '\nDoctor: ' + self.__doctor + \
               '\nCharge: ' + self.__charge
