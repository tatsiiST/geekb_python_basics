#Задача 1-3: Узнать у пользователя число n и найти сумму чисел n + nn + nnn

x = int(input('Please enter number from 1-9:'))
a = int(x * 11)
b = int(x * 111)
sum = (int(x) + a + b)

print(sum)
