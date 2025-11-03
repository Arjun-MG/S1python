set1_input = input("Enter elements of the first set separated by spaces: ")
set1 = set(map(int, set1_input.split()))  # Convert input to integers and make a set

set2_input = input("Enter elements of the second set separated by spaces: ")
set2 = set(map(int, set2_input.split()))

diff1 = set1.difference(set2)
diff2 = set2.difference(set1)

print("Elements in first set but not in second set:", diff1)
print("Elements in second set but not in first set:", diff2)
