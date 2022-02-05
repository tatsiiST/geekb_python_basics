# -*- coding: utf-8 -*-

def salary_analyze(file_path, salary_thr=20000.0):

    filtered_list = []
    salary_avr = 0
    items_count = 0
    try:
        with open(file_path, 'r') as f:
            for line in f:
                try:
                    name, salary = line.split(':')
                    salary = float(salary)
                    salary_avr += salary
                    items_count += 1
                    if salary < salary_thr:
                        filtered_list.append(name)
                except ValueError as err:
                    print('Found some wrong data at line:', line, f'Error {err}')
    except Exception as err:
        print(err)
    salary_avr = salary_avr / items_count if items_count else 0
    return filtered_list, salary_avr


if __name__ == '__main__':
    thr = 20000.0
    li, avr = salary_analyze('task3_tmp.txt', thr)
    if len(li):
        print(f'People, who has salary lower than {thr}:')
        for p in li:
            print('\t', p)
    else:
        print(f'There are no one who has salary lower than {thr}:')

    print(f'Salary average is {avr}')