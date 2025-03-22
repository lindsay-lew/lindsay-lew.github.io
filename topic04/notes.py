# $ python3 -i topic04/notes.py
'''
#Problem 1
s = 'hello world'
print(s[:-6])



#Problem 2
s = '12345'
xs = [1, 2, 3, 4, 5]
# s[-1] = '5'
# xs[-1] = 5
b = s[-1] == xs[-1]
# b = '5' == 5
print('b=',b)


#Problem 3
s = 'hello'
xs = ['h', 'e', '1', '1', 'o']
b = s[-2:] == xs[-2:]
# s[-2:] = 'lo'
# xs[-2:] is equal to ['l', 'o']
# slice will always have the same type as the original variable
# 'lo' != ['l', 'o']
print('b=',b)


#Problem 4
s = 'python is awesome'
if 'python' in s:
    print('True')
else:
    print('False')
# everything in python is case sensistive 


#Problem 5
s = 'python is awesome'
if 'Python' in s:
    print('True')
else:
    print('False')


#Problem 6
s = 'python is awesome'
t = s.replace('python', 'everything')
# replace is what's called a "side effect free" operation
# the variable s is "immutable -- can't be changed
# in general, strings can never be modified in python
# what s.replace does is it keeps s the same and gives a new string that has the replacement 
print('t=', t)


#Problem 7
s = 'Python is awesome'
s.replace('python', 'everything')
# what s.replace does is it keeps s the same and gives a new string that has the replacement 
print('s=', s)

# never in this class try to delete from a [] list
# only create a new list that has the elements deleted 
# xs.remove() is unsafe; don't do it
# s = s.replace() is mostly safe; okay to do


#Problem 8
s = 'python is awesome'
t = s.split()
# split() converts a string into a list where each "word" is an element of the list 
# word is in " " because a word is anything separated by spaces and has no relationship
# to an english word
u = t[-1]
# -1 gets us the last position of the split 
print('u=',u)


#Problem 9
s = 'python\nis\tawesome'
# an escape character is any sequence of letters in a string that start with a \ backslash
# two important escape sequences are: 
# \n is a new line
# \t is the "tab"
t = s.split()
# whitespace characters is the general name for any character that doesn't print 
u = ' '.join(t)
# join is the opposite of split; this pattern of splitting and joining is a way to replace whitespace characters with regular spaces
# join takes a list and converts it to a string
# puts whatever is to the left of . in between each of the entries in the list 
print('u=', u)


#Problem 10
s = 'python  is\tawesome'
t = s.split(' ')
u = t[1]
print('u', u)


#Problem 11
s = 'python is awesome'
t = s.split('o')
u = 'XXX'.join(t)
print('u', u)


#Problem 12
s = 'guido van rossum'
# we call Guido the BDFL: benevolent dictator for life 
i = s.find(' ')
# find returns the first index of the string
# if the string in the () is not in the string to the left of the dot, then -1 is returned
# indices start at 0 
t = s[:i]
print('t=',t)


#Problem 13
s = 'guido van rossum'
# we call Guido the BDFL: benevolent dictator for life 
i = s.find('G')
# find returns the first index of the string
# if the string in the () is not in the string to the left of the dot, then -1 is returned
# indices start at 0 
t = s[:i]
print('t=',t)


#Problem 14
b = 'G' > 'a'
# these comparisons happen "ASCIIbetically" not "alphabetically"
print('b=',b)


#Problem 15
b = "\"" > '\n'
print('b=', b)


#Problem 16
s = "Guido van Rossum"
xs = s.split()
xs.sort()
# the list operations do modify the list
# it is wrong to say: xs = xs.sort()
# for strings, you must always do: s = s.replace()
print('xs=',xs)


#Problem 18
print(0b1010)


#Problem 19
print(0o110)


#Problem 20
print(0x0010)
 
'''
"""
def delete_HTML(text):
    '''
    This function removes all HTML tags from the input text.

    >>> delete_HTML('This is <b>bold</b>!')
    'This is bold!'
    >>> delete_HTML('This is <i>italic</i>!')
    'This is italic!'
    >>> delete_HTML('This is <strong>italic</strong> and this is <ins>strikethrough</ins>!')
    'This is italic and this is strikethrough!'
    '''
    # this is *a* strategy, but it's not a *good* strategy
    # why?
    # I could pass the test cases by just "hard coding" solutions for the 3 examples above,
    # but then my code won't work for other html tags like <p>, <ol>, <li>, <table>...abs
    # >1000 html tags in use and more being created everyday
    '''
    text = text.replace('<b>','')
    text = text.replace('</b>','')
    '''
    # let's write a solution that works for all html tags
    # we need to delete all text that appears between < >

    accumulator = ''
    between_brackets = False
    for c in text:
        if c == '<':
            between_brackets = True
        if between_brackets == False:
            accumulator += c
        if c == '>':
            between_brackets = False
        #if c != '<' and c != '>':
        #    accumulator += c        
    return accumulator
"""
'''
#Problem 21
s = '\x48\x45\x4C\x4C\x4F'
print('s=', s)


#Problem 22
s = '\x57o\x72L\x44'
print('s=', s)


#Problem 23
x = '"'>"'"
print('x=', x)


#Problem 24
x = '">"'
print('x=', x)

#Problem 25
xs = ['there,',"isn't","[a','syntax]",']error']
print(xs[2])
'''

'''
#QUIZ 5 PYTHON REVIEW (Topic 02, 03, 04) --> I failed 

#2
s = 'what\tis t h e\n, answer?'
t = s.split()
u = len(t)
print('u=',u)
'''

#7
x = 10
def foo(x):
    total = 0 
    for i in range(x, 3):
        total += i
    return total
x += foo(1)
x += foo(2)
x += foo(3)
print("x=", x)

#8
xs = [-2, -1, 0, 1, 2]
accumulator = 0
for x in xs:
    accumulator += 1
    if x:
        accumulator += 1
print('accumulator=', accumulator)