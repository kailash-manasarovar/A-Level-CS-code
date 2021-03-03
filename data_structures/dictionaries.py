# hash tables in Python
# http://www.bogotobogo.com/python/python_hash_tables_hashing_dictionary_associated_arrays.php - some
# see python book
# a python dictionary is a hash table

# empty dictionary
# D = {}
# # key value pairs
# D['a'] = 1
# D['b'] = 2
# D['c'] = 3
# print(D)
# for k in D.keys():
#     print(D[k])
# for k,v in D.items():
#     print(k,':',v)




# # using a built in hash function
# import hashlib
# hash = hashlib.md5("a".encode('utf-8'))
# print(hash)
# print(hash.hexdigest())


# # another way to create a dictionary
# # add each value and update the number in the bucket if there is more than one
# word = 'brontosaurus'
# d = dict()
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] = d[c] + 1
# print(d)


# # count words in a text file
# fname = input('Enter the file name: ')
# try:
#    fhand = open(fname)
# except:
#    print('File cannot be opened:', fname)
#    exit()
# counts = dict()
# for line in fhand:
#    words = line.split()
#    for word in words:
#        if word not in counts:
#            counts[word] = 1
#        else:
#            counts[word] += 1
# print(counts)

# sorting a dictionary
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])
