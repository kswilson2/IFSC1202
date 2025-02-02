N = int(input("Number of Students: "))
K = int(input("Number of Apples: "))
applesperstudent = K//N 
print(applesperstudent)
applesgone = N*int(applesperstudent) 
applesleft = K - int(applesgone)
print(applesleft)