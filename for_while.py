lis = [6,8,"Stroka", False, 46.7, 234, 1]

i = 0
while i < len(lis):
    if i % 2 == 0:
        i += 1
        continue
    print("Value element index ", i, ": ", lis[i])
    i += 1
    
for item in lis:
    break
    print("Value element index ", item)
    
for word in "Hello World":
    if word == "l":
        print("letter l was indeficated")
        break