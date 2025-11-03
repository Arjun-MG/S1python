user_input = input("Enter list elements separated by spaces: ")

my_list = user_input.split()

my_list = [int(item) for item in my_list]

if len(my_list) == 0:
    print("The list is empty.")
else:
    first_item = my_list[0]
    last_item = my_list[-1]

    print("First item:", first_item)
    print("Last item:", last_item)
