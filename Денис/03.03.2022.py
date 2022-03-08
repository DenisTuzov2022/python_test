# var = [1, 2, 3, 4]
# var = 123
#
#
# if type(var) == list:
#     print('это list')
#
# if isinstance(var, list):
#     print('это list')

# print(dir(var))


# my_list = ['Sergey', 'qwe','Denis', 'Dima', 'qwe', 'Ivan',  'S']
# my_list.append('Vova')
# my_list.extend([1, 2, 3])
# my_list.append([1, 2, 3])
# cutted_name = my_list.pop(1)
# print(cutted_name)
# my_list.remove('qwe1')
# print(my_list)
# print('qwe1' in  my_list)
# print(my_list.count('S'))
# print(my_list.index('qwe'))
# my_list.insert(1, 'asd')
# my_list1 = my_list.copy()
# print(my_list is my_list1)
# my_list.append('123')
# print(my_list)
# print(my_list1)
# my_list.reverse()
# my_list2 = list(reversed(my_list))
# print(my_list)
# print(my_list2)
# print(my_list[1:5:2]) # [start:stop:step]
# print(my_list[:5:2])
# print(my_list[::2])
# print(my_list[:6])
# print(my_list[:-2])
# print(my_list[::-1])
# print(my_list[::-2])
# print(my_list[2:5])
# print(my_list[:5])
# print(my_list[2:])

# a = ['декабрь', 'январь', 'февраль']
# a.sort()
# print(a)
# b = sorted(a)
# print(b)
# ord('я')
# chr(1103)

# tupe()
# my_tupe = (10, 20, 30)
# print(my_tupe)

# orig_list = [x for x in range(10000)]
# import sys
#
# print(sys.getsizeof(orig_list), 'list')
# my_tuple = tuple(orig_list)
# print(sys.getsizeof(orig_list), 'tuple')
#
# orig_list[0] = 10
# my_tuple[0] = 10

# print(chr(1103))
# print(chr(1103 - 31))

# for i in range(ord('а'), ord('я') + 1):
#     print(chr(i), end ='')
# print(ord('ё'))

# name = 'Ivan'
# age = 50
# money = 5.6521342342332
#
# print('Имя', name, 'Возраст', age, 'Деньги', money)
#
# out_info = 'Имя ' + name  + ' Возраст '  + str(age) +  ' Деньги ' + str(money)
# print(out_info)
#
# out_info2 = 'Имя %s Возраст %d Деньги %f' % (name, age, money)
# print(out_info2)
#
# out_info3 = 'Имя {} Возраст {} Деньги {}'.format(name, age, money)
# print(out_info3)
#
# out_info3 = f'Имя {name} Возраст {age} Деньги {money}'
# print(out_info3)
#
# out_info4 = f'Имя {name:>20} Возраст {age:05} Деньги {money:2f}'
# print(out_info4)

# my_str = 'Ekaterina PeTroVna ASD'
# my_str = 'qwe@mail.ru'
# срезы
# print(my_str.split('@'))
# print(my_str.lower())
# print(my_str.upper())
# print(my_str.capitalize())
# print(my_str.title())
# my_list = ['qwe', 'asd', 'zxc']
# print('/'.join(my_list))


# import copy
# a = [10, 20, 30, [ 100, 200]]

# b = a.copy( )

# b = coppy.deepcopy(a)
# b[3].append(300)

# print(a)
# print(b)
