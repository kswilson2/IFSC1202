N = int(input("Enter N: "))
x=0
if(N<=9):
    for x in range (1, N+1):    
        for i in range (1, x+1): 
            print(i, end="")
        print("")