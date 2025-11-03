def get_list_input(prompt):
    """Function to get a list of integers from user input."""
    while True:
            user_input = input(prompt)
            user_list = list(map(int, user_input.split()))
            return user_list
        

def compare_lists(list1, list2):
    """Function to compare two lists and print their similarities and differences."""
    if list1 == list2:
        print("The lists are identical.")
    else:
        print("The lists are not identical.")
        common_elements = list(set(list1) & set(list2))
        print(f"Common elements: {common_elements}")
        unique_to_list1 = list(set(list1) - set(list2))
        print(f"Elements unique to list1: {unique_to_list1}")
        unique_to_list2 = list(set(list2) - set(list1))
        print(f"Elements unique to list2: {unique_to_list2}")

def main():
    """Main function to execute the program."""
    print("Please enter two lists of integers.")
    list1 = get_list_input("Enter the first list: ")
    list2 = get_list_input("Enter the second list: ")
    compare_lists(list1, list2)

if __name__ == "__main__":
    main()
