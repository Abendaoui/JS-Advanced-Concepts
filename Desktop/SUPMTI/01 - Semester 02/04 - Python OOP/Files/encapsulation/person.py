class Person:
    
    def __init__(self,first,last,age,address):
        self.first = first
        self.last = last
        self._address = address
        self.__age = age
        
    @property
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    
    @full_name.setter
    def full_name(self,name):
        self.first,self.last = name.split(' ')
        
    @full_name.deleter
    def full_name(self):
        print('Deleted Success')
        self.first,self.last = None,None
    
    
    @property
    def email(self):
        return '{1}.{0}@email.com'.format(self.first,self.last).lower()
    
    def __str__(self):
        return "Hello {} You're {} Years Old".format(self.full_name(), self.__age)
    
    
    # Getter methods
    def getaddress(self) -> str:
        return self._address
    
    def getage(self) -> int:
        return self.__age
    
    # Setter methods
    def setfirst(self,value):
        self.first = value
        
    def setlst(self,value):
        self.last = value
        
    def setaddress(self, address):
        self._address = address
        
    def setage(self, age):
        self.__age = age
    
        
    # Property Decorate methods
    @property
    def getfirst(self):
        return self.first
    
    @property
    def getlast(self):
        return self.last
