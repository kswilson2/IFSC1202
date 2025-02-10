n = int(input("Enter First 2 Digit Number: "))
n2 = int(input("Enter Second 2 Digit Number: "))
tensdigit = (n//10) % 10 
tensdigit2 = (n2//10) % 10 
onesdigit = n%10
onesdigit2 = n2%10
merge = (tensdigit*1000) + (tensdigit2*100) + (onesdigit*10) + (onesdigit2)
print(f"Merged Number: {merge}")
