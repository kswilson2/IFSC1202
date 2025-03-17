def myFunction():
	a = "A is a local variable"
	return a
	
b = myFunction()
#print(a)
#NameError: name 'a' is not defined
#To correct this problem, change print(a) to print(b)
print(b)