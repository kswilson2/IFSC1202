max= a[0] #assume 1st number is max
ind = 0
for i in range(1, len(a)):
    if a[i] > max: 
        max = a[i]
        ind = i
#to find min, a[i] < max:
#if using >, max will be the first max found
#if using >=, max will be last max found 