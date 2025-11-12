import math

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

result = []

for num in range(start, end + 1):
    if all(int(digit) % 2 == 0 for digit in str(num)):
        root = int(math.sqrt(num))
        if root * root == num:
            result.append(num)

print("Four-digit numbers with all even digits and perfect squares:")
print(result)
