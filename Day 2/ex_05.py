def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
while True:
    number = int(input("Nhap mot so (nhap -1 de thoat): "))
    if number == -1:
        break
    if is_prime(number):
        print(f"{number} la so nguyen to.")
    else:
        print(f"{number} khong phai so nguyen to.")