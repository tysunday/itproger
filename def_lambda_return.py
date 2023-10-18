#-*- coding: cp1251 -*-


def func(words):
    # print("Peremenaya: ", words)
    pass
    
d = "hi"

def summ(a,b,x = 4):
    res = a + b + x
    return res

d = summ(5,2)
# print(d)

def printAll(*params):
    for i in params:
        print(i * 2)
    
# printAll(6,"Word", True, 9.23, 44)

def printDictionary(**args):
       for key, value in args.items():
        print("Key: ", key, "Value: ", value)
    
printDictionary(long = "Georgiy", short = "Gosha", x = 8, some=True)


# ************ anon function************

mult = lambda a, x: a * x

print(mult(22, 22))
print(mult(3,4))

mult = lambda *args: print(args)

mult(22, 22)