class Some:
    name = "John"
    number = 20    

    def __add__(self, str):
        print("Some " + str)

    def __init__(self):
        print("Init started")
        
    # def __new__(self):
    #     self.__add__(self, "New")
    #     self.__init__(self)

    def __str__(self):
        return "Name: " + self.name
    
    def __ge__(self, x):
        if(self.number >= x):
            return True
        else:
            return False   
        
    def __eq__(self, x):
        if(self.number == x):
            return True
        else:
            return False    
        
    def __ne__(self, x):
        if(self.number != x):
            return True
        else:
            return False 
        
    def __del__(self):
        print("HE SUICIDE")

obj = Some()
obj + "new"
print(obj >= 25)
print(dir(obj))
