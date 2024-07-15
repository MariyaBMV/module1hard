#DZ dopolnitelnoe
#На вход даны следующие данные:
"""Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
Необходимо посчитать среднюю оценку каждого ученика."""
'''Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.'''

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grade_a = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]),
           sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])] #вывели среднее значение каждого ученика. с помощью метода sum i len
print(grade_a) #вывели среднее арифметическое оценок каждого ученика на консоль.
students_sort = sorted(students) #с помощью метода sorted,мы отсортировали имена студентов по алфавиту.
print(students_sort) # вывели имена студентов в алфавитном порядке на консоль

dict1 = dict(zip(students_sort, grade_a)) #с помощью метода zip мы соеденили значения двух переменных students_sort, grade_a , А с помощью методы dict преобразовали списки в словарь.

print(dict1) #вывели на консоль словарь , который имеет ключ (имя студента по алфавиту) и значение его среднеарифметическую оценку.




