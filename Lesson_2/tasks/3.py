"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

mes = int(input("1-12 >>> "))

while mes not in range(1, 13):
    print("Такого месяца не существует")
    mes = int(input("1-12 >>> "))

year_dict = {"winter": (1, 2, 12),
             "summer": (6, 7, 8),
             "spring": (3, 4, 5),
             "autumn": (9, 10, 11)}

for key in year_dict.keys():
    if mes in year_dict[key]:
        print(key)

year_list = ['зима', 'весна', 'лето', 'осень']

year_ind = mes // 3 % 4
print(f"Время года: {year_list[year_ind]}")
