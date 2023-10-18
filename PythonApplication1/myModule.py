if __name__ == "__main__":
    print("HI")
    
some = 12

def printSome(str):
    print("Result ", str)
    
def summ(*args):
    summa = 0
    for i in args:
        summa += i
        
    return summa