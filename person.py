class Person:
    
    def __init__(self, name, address, tele_num):
        self.__name = name
        self.__address = address
        self.__tele_num = tele_num
        
    def set_name(self, name):
        self.__name = name
        
    def set_address(self, address):
        self.__address = address
    
    def set_tele_num(self, tele_num):
        self.__tele_num = tele_num
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_tele_num(self):
        return self.__tele_num
    
class Customer(Person):
    
    def __init__(self, name, address, tele_num, cust_num, mail_list= False):
        Person.__init__(self, name, address, tele_num)
        self.__cust_num = cust_num
        self.__mail_list = mail_list
        
    def set_cust_num(self, cust_num):
        self.__cust_num = cust_num
        
    def set_mail_list(self, mail_list):
        self.__mail_list = mail_list
        
    def get_cust_num(self):
        return self.__cust_num
    
    def get_mail_list(self):
        return self.__mail_list
                      
    
    
    