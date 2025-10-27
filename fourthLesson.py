# #Импорт библиотеки математики
import math as mt

# num1 = 5.8574

# #Округление числа(1 это число после запятой ее мы и округляем)
# num3 = round(num1, 1)
# print(num3)

# #
# num3 = mt.ceil(num1)
# num4 = mt.ceil(num1)

# degree = 58

# #Перевод значений градусов в радианы
# rad = mt.radians(degree)
# print(rad)

# #Перевод значений радианов в градусы
# degree1 = round(mt.degrees(rad))
# print(degree1)

# #Возведение в степень
# num7 = mt.pow(3,5)
# prints(num7)

# #Взять корень
# num7 = mt.sqrt(25)
# print(num7)

# name1, name2, name3 = "John", "Alice", "Bob"
# list_num = [1,2,4,5,6,56,324,213]
# print(max(list_num))
# print(min(list_num))

# l, w, h = 1, 2, 3
# V = l*w*h
# print(V)

# r, h = 5, 10
# V = (mt.pi * mt.pow(r,2) * h)/3
# print(V)

# r, h = 5, 10
# V = mt.pi * mt.pow(r,2) * h
# print(V)

# r = 10
# V = ( 4 * mt.pi * mt.pow(r,3) ) * 3
# print(V)

# student1 = ["Tom", 29, True, "male", "bank"]

# #берем значению по индексу из массива и создаем новый список с 10 элементами с такими же значениями
# name_list = [student1[1]] * 10
# print(name_list)

# student1[0] = 'Oscar'
# print(student1[0])

# student1[1]+=10.00
# print(student1[1])

# #Фунция для подсчета длины строки
# print(len(student1))


student_names = ["Tom", "Bob", "Oscar", "Khabib", "Teddy", "Iman"]

# #Добавляет элемент в конец списка
# student_names.append("Conor")
# print(student_names)

# #Удяляет элемент списка
# student_names.remove("Conor")
# print(student_names)

# #Добавляет элемент в список в нужный индекс
# student_names.insert(2, "Conor")
# print(student_names)

# #Получаем список с:по ("по"-не включается в список)
# print(student_names[1:3])

# #Получаем список с:по ("по"-не включается в список), список идет с лево-направо
# print(student_names[1:-3])

# #Получаем список с:по:интервал ("по"-не включается в список), список идет с лево-направо
# print(student_names[1:-3:1])


student_names[-1], student_names[-2] = student_names[1], student_names[0]
print(student_names)

student_names_2 = ["Sam", "Max", "Leo", "Zac"]

student_names.extend(student_names_2)
print(student_names)

student_names.remove("Sam")
print(student_names)

sam_index = student_names.index("Leo")
student_names[sam_index] = "Leonardo"
print(student_names)