#list all multiples of 5 to 25 plus some repeating

fives = [1, 5, 10, 15, 5, 10, 15, 20, 25, 5, 0, 15, 25, 5, 10, 15, 5, 10, 25]

#indexing = position in an array / list

print(fives.index(int("5"), 2))
#changed string to integer, also indexes after 3rd number

print(fives.index(int("5"), 7))
#indexes after 8th number

print(fives.index(int("5"), 10, 15))
#indexes between 11 and 12th number

print(fives.count(fives[1]))
#shows how many 5's are in the list

