height = int(input("Enter maximum height: "))
x=0
for x in range(1, height+1):
    for i in range(1, x+1):
        print("*", end="")
    print("")