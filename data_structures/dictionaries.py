# hash tables in Python
# http://www.bogotobogo.com/python/python_hash_tables_hashing_dictionary_associated_arrays.php - some
# see python book
# a python dictionary is a hash table

# empty dictionary
D = {}
# key value pairs
D['a'] = 1
D['b'] = 2
D['c'] = 3
print(D)
for k in D.keys():
    print(D[k])
for k,v in D.items():
    print(k,':',v)
#l = map(hash, [0, 1, 2, 3])
#print(l)
#import hashlib
#print(hashlib.md5('a'))
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)
# count words
#fname = input('Enter the file name: ')
#try:
#    fhand = open(fname)
#except:
#    print('File cannot be opened:', fname)
#    exit()
#counts = dict()
#for line in fhand:
#    words = line.split()
#    for word in words:
#        if word not in counts:
#            counts[word] = 1
#        else:
#            counts[word] += 1
#print(counts)

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])