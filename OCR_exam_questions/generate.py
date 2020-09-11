# 2018 Paper 2 June Q4
def generate(num1):
    if num1 > 10:
        print(num1)
        return 10
    else:
        print(num1, "generate", "(",num1," + 1) DIV 2")
        return num1 + (generate(num1 + 1)//2)

print(generate(7))



#def ref_demo(x=10):
#    print(x)
#    x=42
#    print(x)


#x = 9
#ref_demo(x)
#print(x)

#ref_demo()