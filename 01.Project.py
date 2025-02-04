second = int(input("Enter Length of Time in Seconds: "))
years = second // 31536000
print("Years: " + str(years))
remyrinsec = second % 31536000
days = remyrinsec // 86400
print("Days: " + str(days))
remdayinsec = second % 86400
hours = remdayinsec // 3600
print("Hours: " + str(hours))
remhrinsec = second % 3600
minutes = remhrinsec // 60
print("Minutes: " + str(minutes))
remsec = second % 60
seconds = remsec
print("Seconds: " + str(seconds))