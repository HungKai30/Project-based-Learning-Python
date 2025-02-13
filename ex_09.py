
def int_to_str(data):
    if isinstance(data, int):
        return str(data)
    else:
        raise ValueError("not int")
integer_value = 123
string_value = int_to_str(integer_value)
print(f"so ban dau: {integer_value}, chuyen thanh str: {string_value}")