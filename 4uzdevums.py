def split(word): 
    return [char for char in word]
def listToString(s):  
    str1 = "" 
    c =len(s)
    for num in range(c,0,-1) : 
        str1 += l[num-1] 
    return str1

    
print("Ievadi Vārdu:")
word = input()
l = split(word)


rinda= listToString(l)
print(rinda)
