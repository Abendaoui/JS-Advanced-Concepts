from datetime import datetime
class Person:
    PERSON_COUNTER = 0
    def __init__(self,first : str,last : str,age : int):
        self.first = first
        self.last = last
        self.age = age
        Person.PERSON_COUNTER += 1
        
    # Regular Methods
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def getAge(self):
        return 'Your Age : {}'.format(self.age)
    
    # Class Methods
    @classmethod
    def set_person_counter(cls,counter):
        cls.PERSON_COUNTER = counter
    
    # Alternative Construct
    @classmethod
    def constructor(cls,string):
        first,last,age = string.split('-')
        return cls(first,last,age)
    
    @classmethod
    def person(cls,obj):
        first,last,age = obj['first'],obj['last'],obj['age']
        return cls(first,last,age)
    
    # Static methods
    @staticmethod
    def is_workday():
        date = datetime.now()
        today = date.strftime("%A")
        print('Work Day' if today not in ('Saturday','Sunday') else 'Free Day')
    
    
   
adil = Person("Adil","Bendaoui",22)
ayoub = Person("Ayoub","Bendaoui",25)
aissa = Person.constructor('Aissa-Bendaoui-14')
khadija = Person.person({'first':'Khadija','last':'Razki','age':40})

Person.is_workday()


