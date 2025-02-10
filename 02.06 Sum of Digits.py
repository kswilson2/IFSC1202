n = int(input("Enter a 3 Digit Number: "))
onesdigit = n%10
tensdigit = (n//10) % 10 
hundredsdigit = n//100
sum = onesdigit + tensdigit + hundredsdigit
print(f"Sum of Digits: {sum}")