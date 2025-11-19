class Rectangle:
    def __init__(self, l, w):
        self.__length = l
        self.__width = w

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()


l1 = int(input("Enter the length: "))
w1 = int(input("Enter the width: "))
r1 = Rectangle(l1, w1)

l2 = int(input("Enter the length: "))
w2 = int(input("Enter the width: "))
r2 = Rectangle(l2, w2)

if r1 < r2:
    print(f"Area of rectangle 2 is greater: {r2.area()}")
else:
    print(f"Area of rectangle 1 is greater: {r1.area()}")
