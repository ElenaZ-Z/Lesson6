# homework6.py
#Словари
my_dict={'Anton':2013,'Lena':1981,'Sasha':1959,'Zina':1940}
print(my_dict)
print(my_dict['Sasha'])
my_dict['Tanya']=1958
print(my_dict['Tanya'])
my_dict.update({'Natasha':1987,'Nastya':2017})
print(my_dict)
del my_dict['Zina']
print(my_dict.get('Zina'))
print(my_dict)
#Множества
my_set={1,5,6,'1','5','5',1,6}
print(my_set)
my_set.add(7)
my_set.add('3')
my_set.remove('5')
print(my_set)