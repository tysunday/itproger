#-*- coding: cp1251 -*-

from ctypes.wintypes import SHORT


words = {'short' : '����', 'long' : '�������'}
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

cor = (5, "Stroka", True, 5.23, 7) # tuple - ������
# cor[0] = 6 # ������ ��������
# print(list[2:-2:2])

mult = set(list) # ��������� (������ � ������ ������� � ��� �������� ���������)
print(mult)

f_mult = frozenset(list) # �� �� ����� ���������, �� ������ ������
print(f_mult)