n = input("Enter Values Separated by Spaces:")
a = []
s = n.split()

max= s[0] #assume 1st number is max
ind = 0
for i in range(1, len(s)):
    if s[i] > max: 
        max = s[i]
        ind = i
print(f'Largest Value: {max}')
print(f'Index of Largest Value: {ind}')
      
#to find min, a[i] < max:
#if using >, max will be the first max found
#if using >=, max will be last max found 