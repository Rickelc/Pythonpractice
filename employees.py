# Here we are going to be making the class Employee for exercise 1 and the subclass of Productionworker for the additional data attributes
class Employee:
    
    #making the inital function for the class with the general data attributes of the name and ID number for the employee
    def __init__(self, name, id_num):
        self.__name = name
        self.__id_num = id_num
        
    #now i am making the mutator and actuator methods for the class with the attributes
    def set_name(self, name):
        self.__name = name
        
    def set_id_num(self, id_num):
        self.__id_num = id_num
        
    def get_name(self):
        return self.__name
    
    def get_id_num(self):
        return self.__id_num
    
#here is where i am going to make the subclass of Productionworker for the additional attributes of the shift number and the hourly pay rate
class Productionworker(Employee):
    
    #setting the inital function so that it includes the variables i have already made in the superclass and the additional variables
    def __init__(self, name, id_num, shift_num, pay_rate):
        Employee.__init__(self, name, id_num)
        self.__shift_num = shift_num
        self.__pay_rate = pay_rate
    
    #making the methods for the new attributes in this subclass
    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num
        
    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate
        
    def get_shift_num(self):
        return self.__shift_num
    
    def get_pay_rate(self):
        return self.__pay_rate
    
#these classes will allow me to get input from the user for the attributes and set them as my variables and return them when the methods are called
    
    
    