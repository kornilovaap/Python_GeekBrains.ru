"""
1.Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

my_list = [2, 3.45, 'qwerty', True, 5, None]
for el in my_list:
    print(f"{el} - {type(el)}")
_________________________
2 - <class 'int'>
3.45 - <class 'float'>
qwerty - <class 'str'>
True - <class 'bool'>
5 - <class 'int'>
None - <class 'NoneType'>
 