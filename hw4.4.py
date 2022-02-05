src_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res_list = [x for x in src_list if src_list.count(x) == 1]

print('Source list: ', src_list)
print('Result list: ', res_list)