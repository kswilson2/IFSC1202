hourone = int(input("Enter First Timestamp Hours: "))
minuteone = int(input("Enter First Timestamp Minutes: "))
secondone = int(input("Enter First Timestamp Seconds: "))
hourtwo = int(input("Enter Second Timestamp Hours: "))
minutetwo = int(input("Enter Second Timestamp Minutes: "))
secondtwo = int(input("Enter Second Timestamp Seconds: "))
differenceone = (hourone*3600) + (minuteone*60) + (secondone)
differencetwo = (hourtwo*3600) + (minutetwo*60) + (secondtwo)
print(differencetwo - differenceone)

