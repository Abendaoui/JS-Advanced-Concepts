from person import Person

per01 = Person('Adil','Bendaoui',22,'Rabat Morocco')

# print('First Name : {}'.format(per01.getfirst))
# print('Last Name : {}'.format(per01.getlast))
# print('Age : {}'.format(per01._Person__age)) # Accessing private attribute directly with name mangling
# print('Address : {}'.format(per01._address))
# per01.setaddress('Rommani')
# per01.setage(23)
# print("###################")
# print("###################")
# print('Age : {}'.format(per01.getage()))
# print('Address : {}'.format(per01.getaddress()))
# print(per01.full_name())
# print(per01.email)
# print('########################')
# per01.setfirst('john')
# print('########################')
# print(per01.email)

print(per01.full_name)
print(per01.email)

per01.full_name = 'John Smith'

print(per01.full_name)
print(per01.email)

del per01.full_name

print(per01.full_name)
print(per01.email)





