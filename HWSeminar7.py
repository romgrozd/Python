# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько
# просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе 
# несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает 
# в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все 
# не в порядке

# list_g = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
# stih = input('Введите стих: ').split()
# a = list()
# for i in range(len(stih)):
#     a.append(list(filter(lambda x: x in list_g, stih[i]))) 
# b=list(map(lambda x: True if len(x) == len(a[0]) else False,a))
# print('Парам пам-пам' if sum(b) == len(b) else 'Пам парам')

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента
# функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов 
# таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows+1):
#         for j in range(1, num_columns+1):
#             if i == 1 or j == 1:
#                 print(i*j, end=" ")
#             if i > 1 and j > 1:
#                 print(operation(i, j), end=" ")
#         print()

# print_operation_table(lambda x,y:x*y)