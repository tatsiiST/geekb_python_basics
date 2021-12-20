# Задача 1-2: Пользователь ввводит время в секундах
# вывидите указанное время в формате чч:мм:cc

current_time_sec = int(input('Please enter your local time in seconds:'))
hh = current_time_sec // 3600
mm = (current_time_sec // 60) - (hh * 60)
ss = current_time_sec % 60

print(f"Current time is: {hh:02}:{mm:02}:{ss:02}")

# time = int(input("Введите время в секундах - ")
# hours = time // 3600
# minutes = time / 60
# seconds = time / 60
#print(f"{hh:02}:{mm % 60:02}:{ss % 60:02}")
