# graph as adjacency list
# graph = {'1': set(['2', '3']),
#          '2': set(['1', '3', '4']),
#          '3': set(['1', '2', '5']),
#          '4': set(['2']),
#          '5': set(['3'])}

# graph as adjacency matrix in 2D array form
# where 0 index = 1
m = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

# cat algo
# NoOfCats  5
# Cat[1]  1
# FOR A2 TO NoOfCats
#  B1
#  C1
#  WHILE B < A DO
#   IF M[A, B] = 1
#    THEN
#     IF Cat[B] = C
#      THEN
#       B1
#       CC + 1
#     ELSE BB + 1
#     ENDIF
#    ELSE BB + 1
#   ENDIF
#  ENDWHILE
#  Cat[A]  C
# ENDFOR
no_of_cats = 5
print(no_of_cats)
for a in range(2, no_of_cats):
    print(a)
    b = 1
    print(b)
    c = 1
    print(c)
while b < a:
    if m[a, b] == 1:
        if m[b] == c:
            b = 1
            c = c + 1
        else:
            b = b + 1
    else:
        b = b + 1
m[a] = c