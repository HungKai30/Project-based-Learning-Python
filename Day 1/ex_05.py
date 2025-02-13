# Function to check if a number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        return "Chan"
    else:
        return "Le"

# Input from the user
try:
    num = int(input("Nhap so: "))
    result = check_odd_even(num)
    print(f"So {num} la {result}.")
except ValueError:
    print("Nhap so nguyen.")