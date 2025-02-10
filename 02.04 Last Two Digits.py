n = int(input("Enter a number: "))
lasttwodigits = n%100
format = f"{lasttwodigits:02}"
print(f"Last Two Digits: {format}")