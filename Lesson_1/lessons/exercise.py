"""
Пользователь вводит два числа: перове - это до какого числа выводим числа, например. если 10, то 1,2...10,
второе - на какое число НЕ должно делиться выводимое число без остатка, например, если 2, то 1,3,5,7,9
"""

max_count = int(input("Введите максимальное число: "))
delimiter = int(input("Введите делитель: "))

i = 0

while True:
    if i == max_count:
        break  # остановка цикла

    i += 1

    if i % delimiter == 0:
        continue

    print(i)
   
