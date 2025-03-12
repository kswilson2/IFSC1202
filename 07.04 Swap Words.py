s = 'Hello World'
split = s.split(' ') #create list of words
split[0], split[1] = split[1], split[0] #swap words using their indexes
result = ' '.join(split) #join list into new string of words
print (result)