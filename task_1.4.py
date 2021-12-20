#Задача 1-4: Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# используйте цикл while и арифметические операции

num_init = int(input('Введите целое положительное цисло - '))
maximum = num_init % 10
num = num_init

while num > 0:
    digit = num % 10
    if digit > maximum:
        maximum = digit

    if digit == 9:
        break

    num //= 10 # num = num // 10
    print(num)

print(f"Наибольшая цифра в числе {num_init} равна {maximum}")
