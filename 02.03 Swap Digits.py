n = int(input("Enter a number: "))
onesdigit = n%10
tensdigit = n//10
swappednumber = (onesdigit*10) + tensdigit
print("Swapped Number: " + str(swappednumber))