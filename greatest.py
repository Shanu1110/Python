a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("a is the greatest:", a)
elif b >= a and b >= c:
    print("b is the greatest:", b)
else:
    print("c is the greatest:", c)