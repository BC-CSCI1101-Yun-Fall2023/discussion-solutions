a = float(input("Side A Length: "))
b = float(input("Side B Length: "))
c = float(input("Side C Length: "))

if a == b == c:
    print("Equilateral Triangle")
elif a != b and a != c and b != c:
    print("Scalene Triangle")
else:
    print("Isosceles Triangle")

