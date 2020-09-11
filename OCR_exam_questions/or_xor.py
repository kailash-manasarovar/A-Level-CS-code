a=42
b=41
c=42

d = 5
if ((a>b) or (b>=c)):
    if ((c<a) ^ (c<b)):
        d = 15
    else:
        d = 16
else:
    d=14

print(d)