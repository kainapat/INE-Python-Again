import os

def display_menu():
    print("\nHeroes Menu:")
    print("1. Display Heroes")
    print("2. Add Heroes")
    print("3. Insert Heroes")
    print("4. Remove Heroes")
    print("5. Display Sorted Heroes (Ascending / Descending)")
    print("6. Quit")

def display_heroes():
    with open('heroes.txt', 'r') as file:
        heroes = file.readlines()
        heroes = [hero.strip() for hero in heroes if hero.strip()]
        if heroes:
            print("\nCurrent Heroes:")
            print(heroes)
        else:
            print("\nNo heroes found.")



def add_hero():
    hero_name = input("\nEnter the name of the Hero: ")
    with open('heroes.txt', 'a') as file:
        file.write(hero_name +  '\n ')
    print(f"\n{hero_name} : has been added to the list of Heroes.")

def insert_hero():
    position = int(input("\nEnter the position to insert the hero: "))
    hero_name = input("Enter the name of the hero: ")
    with open('heroes.txt', 'r') as file:
        heroes = file.readlines()
    if 0 < position <= len(heroes) + 1:
        heroes.insert(position - 1, hero_name + '\n')
        with open('heroes.txt', 'w') as file:
            file.writelines(heroes)
        print(f"\n{hero_name} : has been inserted at position {position}.")
    else:
        print("\nInvalid position. Please try again.")

def remove_hero():
    hero_name = input("\nEnter the name of the hero to remove: ")
    with open('heroes.txt', 'r') as file:
        heroes = file.readlines()
    removed = [hero for hero in heroes if hero.strip() != hero_name]
    if len(heroes) != len(removed):
        with open('heroes.txt', 'w') as file:
            file.writelines(removed)
        print(f"\n{hero_name} : has been removed from the list of heroes.")
    else:
        print(f"\n{hero_name} not found in the list.")

def display_sorted_heroes(ascending=True):
    with open('heroes.txt', 'r') as file:
        heroes = file.readlines()
        heroes = [hero.strip() for hero in heroes if hero.strip()]
        heroes.sort(reverse=not ascending)
        if heroes:
            print(f"\nSorted Heroes ({'Ascending' if ascending else 'Descending'}):")
            print(heroes)
        else:
            print("\nNo heroes found.")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            display_heroes()
        elif choice == '2':
            add_hero()
        elif choice == '3':
            insert_hero()
        elif choice == '4':
            remove_hero()
        elif choice == '5':
            ascending = input("\nDo you want to sort in ascending order? (y/n): ")
            display_sorted_heroes(ascending.lower() == 'y')
        elif choice == '6':
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == '__main__':
    if not os.path.exists('heroes.txt'):
        with open('heroes.txt', 'w') as file:
            pass
    main()
    
        
    
    