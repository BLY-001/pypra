movie = 'the Godfather'
print(movie[0:2])

#string variable [start:stop:step]

print(movie[2:5])
print(movie[:2])
print(movie[4:])
print(movie[-2:])

# movie[:i] + movie[i:] is equal to movie
print(movie[:4] + movie[4:])
print(movie[:42]) #NB: THIS WILL RUN AND WOULD N0t GIVE AN ERROR
print(movie[3:100])

print(movie[0:10:2])
print(movie[::]) # this will print the whole string
print(movie[::-1]) # this will print upside from the lastletter as in "rehtafdoG eht"
print(movie[::-3]) # this will print upside from the lastletter and with 3 steps i.e  "rtd t"


