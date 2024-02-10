from manager import Manager
from developer import Developer

dev_01 = Developer(1,'john','smith',26,15000,['javaScript','java'])
dev_02 = Developer(2,'Nancy','cloey',24,10000,['nodejs','reactjs','nestjs'])
dev_03 = Developer(3,'peter','zoug',29,25000,['typescript','php','laravel'])

emp_01 = Manager(5,'Adil','Bendaoui',31,50000, [dev_01,dev_02])
emp_02 = Manager(5,'Ayoub','Bendaoui',34,70000, [dev_03])






emp_01.movedeveloper(emp_02,dev_01)

print(emp_01.full_name())
emp_01.getsubemps()


print("##########################")
print("##########################")

print(emp_02.full_name())
emp_02.getsubemps()
