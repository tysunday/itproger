#-*- coding: cp1251 -*-

from ctypes.wintypes import SHORT


words = {'short' : 'Гоша', 'long' : 'Георгий'}
print(words['short'])

list = [5, "Stroka", True, 5.23, 7] # list
list.append("Hi")
b = [5,8,1,9,6]
list.extend(b)
list.remove(5)
list.remove(5)
list.pop(0)
b.reverse()
b.clear()
# print(list)
# print(b)

cor = (5, "Stroka", True, 5.23, 7) # tuple - кортеж
# cor[0] = 6 # нельзя изменять
# print(list[2:-2:2])

mult = set(list) # множество (всегда в разном порядке и все элементы уникальны)
print(mult)

f_mult = frozenset(list) # то же самое множество, но нельзя менять
print(f_mult)