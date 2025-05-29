# task 1
print("Task 1:")
hello = "Hello, Python World!"
print(hello)

# task 2
print("Task 2:")
a = int(input("Введіть ціле число:"))
b = int(input("Введіть ціле число:"))
print("a додати b = ", a+b)
print("a відняти b = ", a-b)
print("a помножити на b = ", a*b)
print("a поділити на b = ", a/b)

# task 3
print("Task 3:")
c = str(input("Введіть будь який текст:"))
d = str(input("Введіть будь який текст:"))
cd = c + d
cd_len = len(cd)
print("Об'єднані рядки:", cd,"; Довжина об'єднаного рядку:", cd_len)

# task 4
print("Task 4:") 
e = int(input("Введіть ціле число:"))
if e % 2 == 0:
    print("Число парне")
elif e % 2 == 1:
    print("Число непарне")
else:
    print("Можливо ви ввели не число?") # не знаю правда чи потрібне воно тут чи нє. Хай буде

# task 5 
print("Task 5:")
number = 0
while number < 10:
    number += 1 
    print(number)

# task 6
print("Task 6:")
num = int(input("Введіть ціле число n:"))
if num > 0:
    print("Позитивний")
elif num == 0:
    print("Нуль")
else:
    print("Негативний")

# Task 7
print("Task 7:")
for i in range (1, 11, 1):
    if i % 2 == 0:
        print(i)

# Task 8
print("Task 8:")
n = int(input("Введіть ціле число (додатнє і більше 1), а компудахтєр порахує вам суму арифметичної прогресії: "))
our_sum = 0
for i in range(1, n+1, 1):
    our_sum += i
print("Суму арифметичної прогресії від 1 до n =", our_sum)

# Task 9
print("Task 9:")
for i in range(10, 0, -1):
    print(i)

# Task 10
print("Task 10:")
for i in range(1, 11, 1):
    if i == 5:
        continue
    elif i == 7:
        break
    else:
        print(i)
# Але додам, що тут за умовою завдання не ясно - 7 має виводитись після бріку (чи брейку). 
# Чи на сімці цикл завершується і сімку вже виводити не потрібно? Умова трішки розмита,
# тож сподіваюсь що проблем не буде і це зарахується.

print("/n Домашка виконана!")