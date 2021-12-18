# Задача 1-2: Пользователь ввводит время в секундах
# вывидите указанное время в формате чч:мм:cc

current_time_sec = int(input('Please enter your local time in seconds:'))
hh = current_time_sec // 3600
hh_res = current_time_sec % 3600
mm = hh_res // 60
ss = hh_res % 60

print(f"Current time is: {hh}:{mm}:{ss}")
