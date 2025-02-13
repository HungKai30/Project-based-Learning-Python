def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

# Example usage
age = int(input("Enter the age: "))
status = check_age(age)
print(f"The person is an {status}.")