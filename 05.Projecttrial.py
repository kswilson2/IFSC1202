x = int(input("Enter Start of Range:"))
y = int(input("Enter End of Range: "))

for i in range(x, y+1):
    numofdigits = 0
    original = i
    while i > 0:
        onesdigit = i % 10
        numofdigits += 1
        tensdigit = (i//10) % 10
        hundredsdigit = (i//100) % 10
        thousandsdigit = (i//1000) % 10
        tenthousandsdigit = (i/10000) % 10
        sum = (onesdigit ** numofdigits) + (tensdigit **numofdigits) + (hundredsdigit **numofdigits) + (thousandsdigit **numofdigits) + (tenthousandsdigit **numofdigits)
    if sum == original:
        print(original)
