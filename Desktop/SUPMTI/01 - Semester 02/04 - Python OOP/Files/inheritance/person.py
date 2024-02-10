class Person:
    def __init__(self,id : int,first : str,last : str,age : int):
        self.id = id
        self.first = first
        self.last = last
        self.age = age
    
    def full_name(self):
        return '{} {}'.format(self.first, self.last)


    def get_age(self):
        return self.age
