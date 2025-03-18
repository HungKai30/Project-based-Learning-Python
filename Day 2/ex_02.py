def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

# Example usage
age = int(input("nhap tuoi: "))
status = check_age(age)
print(f"nguoi nay la {status}.")