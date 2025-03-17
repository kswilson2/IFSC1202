#Example 1
a = [1, 2, 3, 4]
b = [5, 6]
c = [7, 8, 9]
d = [] #create empty list
d.append(a) #[1,2,3,4]
d.append(b) #[5,6]
d.append(c) #[7,8,9]
print (d) #list of lists [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
print(d[0]) #[1, 2, 3, 4] first list
print(d[1]) #[5, 6]
print(d[2]) #[7, 8, 9]
print(d[0][0]) #from 1st list, first element =1
print(d[0][1])
print(d[0][2])
print(d[0][3])
print(d[1][0]) #from 2nd list, first element =5
print(d[1][1])
print(d[2][0])
print(d[2][1])
print(d[2][2])
d[0][0] = 10 #change list 1
d[0][1] = 11
d[0][2] = 12
d[0][3] = 13
print(d[0][0])
print(d[0][1])
print(d[0][2])
print(d) #[[10, 11, 12, 13], [5, 6], [7, 8, 9]]
#lists do not have to be the same length = jagged list