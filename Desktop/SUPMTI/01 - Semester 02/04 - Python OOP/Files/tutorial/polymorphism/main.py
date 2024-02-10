from cat import Cat
import datetime
cat01 = Cat('Kitty',3,'Female','Adil')
cat02 = Cat('Sua',5,'Male','Nora')
cat03 = Cat('Sua',5,'Male','Nora')
cat04 = Cat('Sua',5,'Male','Nora')


# print(cat01.__str__())
# print(cat01.__repr__())
# print("###################")
# print(str(cat01))
# print(repr(cat01))
print(cat01 + cat02)
print("###################")
date = datetime.date
print(date.today().year)
print(date.today().month)
print(date.today().day)


