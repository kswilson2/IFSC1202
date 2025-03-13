#pull out sections and put them together
s = str(input("Enter a string: "))
locone = s.find('h')
loctwo = s.rfind('h') + 1
print (s[:locone] + s[loctwo:])