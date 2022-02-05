src_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# index solution
res_list = [src_list[i] for i in range(1, len(src_list)) if src_list[i] > src_list[i-1]]
assert (res_list == [12, 44, 4, 10, 78, 123])

# enumerate + index solution
res_list = [item for i, item in enumerate(src_list[1:]) if item > src_list[i]]
assert (res_list == [12, 44, 4, 10, 78, 123])

# zip solution
res_list = [y for x, y in zip(src_list[:-1], src_list[1:]) if y > x]
assert (res_list == [12, 44, 4, 10, 78, 123])


print('Source list: ', src_list)
print('Result list: ', res_list)