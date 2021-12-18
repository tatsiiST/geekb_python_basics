# Задача 1-5: Запросить у пользователя значение выручки и издержек фирмы. Определите результат
# Вывести сообщение о результате. Если фирма отработала с прибылью вычислите рентабельность выручки.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

income = int(input('Enter your company income: '))
costs = int(input('Enter your company costs: '))
if income > costs:
    profitability = income-costs
    rent = profitability/income
    print(f"Great job! You have {profitability} profitability")
    worker = int(input('How many people work at your company: '))
    print(f"Your company profitability for one worker is {profitability/worker} ")
elif income == costs:
    print('Not bad')
else:
    print('Good luck')
