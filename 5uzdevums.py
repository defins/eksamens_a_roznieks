def split(word): 
    return [char for char in word]

print("ievadi 10 skaitlus atdalot tos ar atstarpi:")
word = input()
l = split(word)
c= len(l)
sum = 0
for i in range(c):
    if l[i]== " ":
        print()

    else: 
        sum+=int(l[i])
print ("so skaitlu summa ir:",sum)
