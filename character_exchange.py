
text = input("Enter a string: ")

pos1 = int(input("Enter the first position to swap (starting from 0): "))
pos2 = int(input("Enter the second position to swap (starting from 0): "))

char_list = list(text)

char_list[pos1], char_list[pos2] = char_list[pos2], char_list[pos1]

swapped_text = ''.join(char_list)

print("String after character exchange:", swapped_text)
