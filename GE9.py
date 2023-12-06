file_path = "C:\\Users\\brajesh kumar\\OneDrive\\Pictures\\New folder\\New folder\\myfile.txt"
f = open(file_path , 'r')
content = f.read()
def length():
    print("number of a character in a file is ",len(content))
    word = content.split()
    print("number of a word in a file is ",len(word))
    line = content.splitlines()
    print("number of a line in a file is ",len(line))
length()

def frequency():
    dict = {}
    for item in content:
        value = content.count(item)
        dict[item] = value
    print(dict)
frequency()

def reverse():
    word = content.split()
    words = word[::-1]
    print(' , '.join(words))
reverse()



#write even line in file 1 and odd line in file 2.
f = open(file_path , 'r')
content = f.readlines()
with open("file3.txt", 'w') as file1, open("file4.txt", 'w') as file2:
  for i ,line in enumerate(content):
       if i % 2 == 0:
        
            file1.writelines(line)
       else:
        
             file2.writelines(line)
    
f.close()
