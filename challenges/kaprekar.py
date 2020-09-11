def is_kaprekar(n):
	n2 = str(n**2)
	for i in range(len(n2)):
		a, b = int(n2[:i] or 0), int(n2[i:])
		if b and a + b == n:
			return True
			#return (n, (n2[:i], n2[i:]))


# Driver method
i = 1
while i < 10000:
    if (is_kaprekar(i)):
        print(i, " ")
    i = i + 1

