my_dict = {'Виталий': 2002, 'Ира': 2003}
print(my_dict)
print(my_dict['Виталий'])
my_dict['Егор'] = 2002
print(my_dict['Егор'])
my_dict.update({'Никита': 2004,
                'Андрей': 2001})
print(my_dict)
a = my_dict.pop('Ира')
print(my_dict)
print(a)
my_set = {1, 2, 3, 1, 2, 3, 4, 5, 6, True, 'Bob', (5,6,7)}
print(my_set)
my_set.update({7, 8,})
print(my_set)
print(my_set.discard(3))
print(my_set)