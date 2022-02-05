def calculate_salary(production, rate, prize):

    return production * rate + prize


if __name__ == '__main__':
    from sys import argv

    try:
        print(f'Calculated salary: {calculate_salary(*map(float, argv[1:]))}')
    except Exception as err:
        print(f'Unexpected error: {err}')