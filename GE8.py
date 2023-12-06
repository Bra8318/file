#Wap to creat a list of the cubes of only the even integers appearing in the input list.
list = [1,2,3,4,5,6,7,8,9,10,'first','second']
newlist = []
for n in list:
    if type(n) == int:
      if n % 2 == 0:
        cube = n ** 3
        newlist.append(cube)
print(newlist)

     

