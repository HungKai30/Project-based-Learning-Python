'''Đảo ngược mảng'''

my_list = [1, 2, 3, 4]
reversed_list = []
for item in my_list[::-1]:
    reversed_list.append(item)
print(reversed_list)

'''Tìm số lớn thứ 2 trong mảng'''

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
max_num = max(my_list)
second_max = None
for num in my_list:
    if num < max_num:
        if second_max is None:
            second_max = num
        elif num > second_max:
            second_max = num
print(second_max)

'''Xóa phần tử trùng lặp trong mảng'''

my_list = [4,4,5,1]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)