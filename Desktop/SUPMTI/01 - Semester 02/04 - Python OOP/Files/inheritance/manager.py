from employee import Employee


class Manager(Employee):
    #  __ : dunder
    def __init__(self,id,first,last,age,salary,subemployees=None):
        super().__init__(id,first,last,age,salary)
        if subemployees is None:
            self.subemployees = []
        else :
            self.subemployees = subemployees
    
    def getsubemps(self):
        if  self.subemployees is None or len(self.subemployees) == 0:
            print('{} Has No Sub Developers'.format(self.full_name()) )
        else:
            for subemployee in self.subemployees:
                print('Developer {} : {}'.format(subemployee.id,subemployee.full_name()))
                
    def addsubdevelopers(self,developer):
        if developer in self.subemployees:
            print('{} Is Already Sub Developer Of {}'.format(developer.full_name(),self.full_name()))
        else:
            self.subemployees.append(developer)
            
    def deletesubdevelopers(self,developer):
        if developer not in self.subemployees:
            print('{} Is Not Sub Developer Of {}'.format(developer.full_name(),self.full_name()))
        else:
            self.subemployees.remove(developer)
            
    def movedeveloper(self,manager,developer):
        if developer in self.subemployees:
            manager.addsubdevelopers(developer)
            self.deletesubdevelopers(developer)
        else:
            print('You Are Not Owned This Developer.')
        
    

