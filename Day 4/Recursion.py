#1
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

# Ví dụ
print(giai_thua(5))  # Kết quả: 120

#2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Ví dụ
print(fibonacci(6))  # Kết quả: 8

#3

def dao_nguoc_chuoi(s):
    if len(s) <= 1:
        return s
    return s[-1] + dao_nguoc_chuoi(s[1:-1]) + s[0]

# Ví dụ
print(dao_nguoc_chuoi("hello"))  # Kết quả: "olleh"
#4
def tong_mang(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + tong_mang(arr[1:])

# Ví dụ
print(tong_mang([1, 2, 3, 4, 5]))  # Kết quả: 15
#5

def kiem_tra_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return kiem_tra_palindrome(s[1:-1])

# Ví dụ
print(kiem_tra_palindrome("madam"))  # Kết quả: True
print(kiem_tra_palindrome("hello"))  # Kết quả: False
