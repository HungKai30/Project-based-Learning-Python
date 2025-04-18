odd_numbers = [x for x in range(1, 21) if x % 2 != 0]
print(odd_numbers)
hello_list = ["Hello" for _ in range(5)]
print(hello_list)
#generator tạo hết 1 lượt r in ra
squares_gen = (x * x for x in range(1, 6))
squares_list = list(squares_gen)
print(squares_list)