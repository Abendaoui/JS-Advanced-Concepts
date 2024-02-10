from person import Person


class Employee(Person):
    def __init__(self,id,first,last,age,salary : int):
        super().__init__(id,first,last,age)
        self.email = '{}{}@company.com'.format(self.first,self.last).lower()
        self.salary = salary


