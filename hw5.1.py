#-*- coding: utf-8 -*-

def collaborate(file_path):
    with open(file_path, 'w') as f:
        while True:
            i = input("Please enter some string or type Enter to exit: ")
            if not i:
                break
            print(i, file=f)


if __name__ == '__main__':
    collaborate('task1_tmp.txt')