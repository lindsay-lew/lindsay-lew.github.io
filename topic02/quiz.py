"""
#Problem 1
x = 2 ** 3      # = 8
print('x=', x)
y = x * 4       # 32
print('y=', y)
z = y % 5       #2
print('z=', z)

#Problem 2
if 'False':
    result = 0 
else:
    result = 1
print('result=', result)
#result = 0, because 'False' is a truthy string

#Problem 3
i = 0 
total = 0 
while i < 5: #this condition is never going to evaluate to true because we will never run line 25
    total = total + i 
    # 0 is the only falsey number
    # any non-zero number is truthy
    if i % 2    #relying on the truthy/falseyness of integers
    i += 1
print('total=', total)
#this is an infinite while loop, everyone gets full credit on this problem 
#disadvantage of while loops is that if you make a mistake, then the code can run forever (won't terminate)
#anything you can do with a while loop, you can do with a for loop, and vis versa...in general, we prefer 
#for loops, because you won't get infinite loops on accident

#Problem 4
total = 42
for i in range(10,15,2): #10,12,14
    total %= i 
    print('total=', total)
#total = 2
"""