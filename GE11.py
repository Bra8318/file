# Consider a tuple t1=(1,2,5,7,9,2,4,6,8,10).Wap to perform the following.
#1.print half the value of t1 in one line and next half on other line.
t1=(1,2,5,7,9,2,4,6,8,10)
first_half = t1[0:len(t1)//2]
print('First Half',first_half)
next_half = t1[len(t1)//2: ]
print('Next Half',next_half)

#2.print another tuple whose values are even number.
even = tuple(filter(lambda x: x % 2 == 0,t1))
print(even)

#3.concatenate a t2 = (11,13,15)with t1.
t2 = (11,13,15)
t3 = t1 + t2
print("concatenated tuple is :",t3)

#4.Return max and min value of tuple.
max_value = max(t3)
print("maximum vale",max_value)

min_value = min(t3)
print("minimum value",min_value)
