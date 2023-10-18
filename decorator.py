def auth(func):
    def wrapper():
         isAuth = False
         if(isAuth):
             func()
         else:
             print("You need to be auth")
             func()
    return wrapper        

def test(func):
    def wrapper():
        print("Text before function")
        func()
        print("Text after function")
    return wrapper


@test
@auth
def show():
    print("Show function")
    
@test
@auth
def index():
    print("Index function")

@test
@auth
def somebody():
    print("some say")
    
show()
# index()
# somebody()