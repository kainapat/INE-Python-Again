import math

def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

def rectangle_area(width, length):
    return width * length

def rectangle_perimeter(width, length):
    return 2 * (width + length)

def main():
    area_circle_choice = 1
    circumference_choice = 2
    area_rectangle_choice = 3
    perimeter_rectangle_choice = 4
    quit_choice = 5

    choice = 0
    while choice != quit_choice:
        display_menu()
        choice = int(input('Enter your choice: '))
        if choice == area_circle_choice:
            radius = float(input("Enter the circle's radius: "))
            print('The area is', circle_area(radius))
        elif choice == circumference_choice:
            radius = float(input("Enter the circle's radius: "))
            print('The circumference is', circle_circumference(radius))
        elif choice == area_rectangle_choice:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The area is', rectangle_area(width, length))
        elif choice == perimeter_rectangle_choice:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The perimeter is', rectangle_perimeter(width, length))
        elif choice == quit_choice:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')

def display_menu():
    print('------------------------')
    print(' MENU')
    print('------------------------')
    print('1) Area of a circle')
    print('2) Circumference of a circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Quit')
    print('------------------------')


main()
