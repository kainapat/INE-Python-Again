Columns = int(input("Enter the Columns: "))
count = 0
for i in range(1, 101):
    num_str = str(i)
    print(num_str.ljust(2), end=" ")
    count += 1
    if count % Columns == 0:
        print("\n")