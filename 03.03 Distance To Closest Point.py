a = int(input("Enter Point A: "))
b = int(input("Enter Point B: "))
c = int(input("Enter Point C: "))
atob = b - a
atoc = c - a
if atob <= atoc:
    smallest = atob
else:
    smallest = atoc
print(smallest)