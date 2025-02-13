def add_two_numbers(a, b):
    return a + b

# chay lenh
if __name__ == "__main__":
    num1 = float(input("Nhap so thu nhat vao: "))
    num2 = float(input("Nhap so thu hai vao: "))
    result = add_two_numbers(num1, num2)
    print(f"Tong cua 2 so la {result}")