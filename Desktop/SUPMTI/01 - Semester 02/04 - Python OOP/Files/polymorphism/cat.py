class Cat:
    # Magic Method Constructor
    def __init__(self,name,age,gender,owner):
        self.name = name
        self.age = age
        self.gender = gender
        self.owner = owner
        
    def __str__(self):
        return 'Hello {} Is A {} Cat'.format(self.name,self.gender)
    
    def __repr__(self):
        return 'Cat({},{},{},{})'.format(self.name,self.age,self.gender,self.owner)
    
    def __add__(self,othercat):
        if isinstance(othercat,Cat):
            return sum([self.age,othercat.age])
        else:
            return "Cannot Add Because The Other Object is Not instance of Cat"
        
        
    
