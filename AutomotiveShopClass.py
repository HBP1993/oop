
#cellphone class
class CellPhone:
    def __init__(self, manufact, model, retail_price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = retail_price

    def set_manufact(self, manufact):
        self._manufact = manufact

    def set_model(self, model):
        self._model = model

    def set_retail_price(self, retail_price):
        self._retail_price = retail_price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price


#customer class
class Customer:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
        
    def set_name(self, name):
        self.__name = name
        
    def set_address(self, address):
        self.__address = address
        
    def set_phone(self, phone):
        self.__phone = phone
        
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_phone(self):
        return self.__phone
    
    
    
# car class
class Car: 
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        
    def set_make(self, make):
        self._make = make
        
    def set_model(self, model):
        self._model = model
        
    def set_year(self, year):
        self._year = year
        
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year
    
    
    
 
#sales tax rate
tax_rate = 0.10

#class ServiceQuote
class ServiceQuote:
    def __init__(self, pcharges, lcharges, taxrate):
        self.__pcharges = pcharges
        self.__lcharges = lcharges
        self.__taxrate = taxrate

    def pcharges(self, pcharges):
        self.__pcharges = pcharges

    def lcharges(self, lcharges):
        self.__lcharges = lcharges

    def get_salestax(self):
        return self.__taxrate * self.__pcharges

    def get_totalcharges(self):
        return self.__lcharges + self.__pcharges + self.get_salestax()

    def get_pcharges(self):
        return self.__pcharges

    def get_lcharges(self):
        return self.__lcharges    
