s = str(input("Enter a string: "))
locone = s.find('h') 
loctwo = s.rfind('h')
midsection = s[loctwo:locone-1:-1]
sectionone = s[:locone]
sectiontwo = s[loctwo+1:]
print(sectionone + midsection + sectiontwo)