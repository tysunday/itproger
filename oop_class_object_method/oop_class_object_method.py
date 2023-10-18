class User:
    name = ""
    surname = ""
    age = 0
    email = "" 
    
    def __init__(self, name, surname, age, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email

    def set(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    def printAll(self):
        print("User: ", self.name, "\n Age: ", self.age)

admin = User("Admin", "Marley", 21, "admin@itproger.com")
bob = User("Bob", "Marley", 18, "bobKrutoy@sfr.gov.ru")

admin.printAll()
bob.printAll()