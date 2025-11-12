n = int(input("Enter number of items: "))

numbers = []
for i in range(n):
    num = float(input(f"Enter item {i+1}: "))
    numbers.append(num)

total = sum(numbers)

print("Sum of list items:", total)
