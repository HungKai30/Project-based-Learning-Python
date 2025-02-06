def check(number):
    if number > 0:
        print("so duong")
    elif number < 0:
        print("So am")
    else:
        print("So 0")

if __name__ == "__main__":
    number = int(input("Nhap so: "))
    check(number)