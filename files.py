# str = input("Input value:")
# str += '\n'

# file = open('text.txt', 'a')
# file.write(str)
# file.close()

# file = open('text.txt', 'rt')
# print(file.read(10))
# for line in file:
#     print(line)
# file.close()

# ************************ EXCEPTION ***********************

user_input_a = False
user_input_b = False

while user_input_a == False:
    try:
        a = int(input("Input value 1: "))
        user_input_a = True
    except ValueError:
        print("INPUT NUMBER MOTHERFUCKER!")

while user_input_b == False:
    try:
        b = int(input("Input value 2: "))
        user_input_b = True
    except ValueError:
        print("INPUT NUMBER MOTHERFUCKER!")
        


print("Result: ", a + b)