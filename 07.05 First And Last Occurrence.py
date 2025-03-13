s = str(input("Enter a string: "))
index = s.find('f')
if index == -1:
    print("0")
else:
    index2 = s.find('f', index+1)
    if index2 == -1:
        print(index)
    else: 
        print(index, index2)