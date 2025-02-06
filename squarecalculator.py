def calculate_square_area(side_length):
    return side_length ** 2

if __name__ == "__main__":
    side_length = float(input("Nhap canh cua hinh vuong: "))
    area = calculate_square_area(side_length)
    print(f"Dien tich hinh vuong la: {area} m^2")