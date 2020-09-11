import itertools

def perm(c):
    print (set(itertools.permutations(c, 4)))
#print (set(itertools.permutations([1,2,3,4], 3)))
#print (set(list(itertools.permutations([1,2,3,4], 3))))
#print (list(itertools.permutations([1,2,3,4], 2)))
#print list(itertools.combinations('123', 2))
#print list(itertools.permutations([1,2,3,4], 2))

n=int(input("Input a four digit number : "))

#create an array from input n
perm(list(str(n)))
#b = str(n)
#create a character array to add the
#c = []
#for digit in b:
#    c.append (int(digit))
#perm(c)


