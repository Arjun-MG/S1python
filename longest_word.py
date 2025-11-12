words = input("Enter words separated by spaces: ").split()

longest_word = max(words, key=len)

print("The longest word is:", longest_word)
print("Length of the longest word:", len(longest_word))
