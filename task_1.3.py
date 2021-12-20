#Задача 1-3: Узнать у пользователя число n и найти сумму чисел n + nn + nnn

x = input("Please enter number positive number - ")
print(f'{x} + {x + x} + {x + x + x} = {int(x) + int(x + x) + int(x + x + x)}')
