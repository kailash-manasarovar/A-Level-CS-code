#from itertools import islice
#list(islice(filter(lambda y: len(set(str(y))) == 4, range(2015, 0, -1)), 5))

count = 0
for year in range(2015, 1000, -1):
    if len(set(str(year)))==4:
        count = count+1
print(count)