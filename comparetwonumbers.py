def compare_two_numbers(a, b):
    if a > b:
        return f"{a} lon hon {b}"
    elif a < b:
        return f"{a} nho hon {b}"
    else:
        return f"{a} bang {b}"

# Example usage
num1 = float(input("Nhap so thu nhat: "))
num2 = float(input("Nhap so thu hai: "))
result = compare_two_numbers(num1, num2)
print(result)