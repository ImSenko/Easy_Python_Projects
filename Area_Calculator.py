def start():
    print("=====================================\n   Welcome to the Area Calculator!\n=====================================")
    print("Please select a shape to calculate its area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")
    choice = input("Enter the number corresponding to your choice: ")
    if choice == '1':
        calculate_circle_area()
    elif choice == '2':
        calculate_rectangle_area()
    elif choice == '3':
        calculate_triangle_area()
    elif choice == '4':
        calculate_square_area()
    else:
        print("Invalid choice. Please try again.")
        start()

def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius ** 2
    print(f"The area of the circle is: {area:.2f}")

def calculate_rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area:.2f}")

def calculate_triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area:.2f}")

def calculate_square_area():
    side = float(input("Enter the side length of the square: "))
    area = side ** 2
    print(f"The area of the square is: {area:.2f}")

start()