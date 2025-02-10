n = int(input("Enter a 3 Digit Number: "))
onesdigit = n%10
tensdigit = (n//10) % 10 
hundredsdigit = n//100
reverse = (onesdigit*100) + (tensdigit*10) + hundredsdigit
print(f"Reverse of Digits: {reverse}")