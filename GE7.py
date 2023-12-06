# Write a function that accept two string and return indices if string1 present in string2. else -1 .

def indices():
    str1 = input("enter first string:")
    str2 = input("enter second string:")

    indices = []
    index = str1.find(str2)

    while index != -1:
        indices.append(index)
        index = str1.find(str2,index+1)

    if not indices:
        return -1
    else:
        return indices
print(indices())
    
