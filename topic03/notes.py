#!/bin/python3
'''
The functions below are also part of your lab for this week.
We will work through this file in lecture.
One useful tip is to use python's *interactive mode*.
You can enter interactive mode with the command
```
Get interactive mode with:
$ python3 -i topic03/notes.py
```
Run doctests with:
$ python3 -m doctest --verbose topic03/notes.py

Without --verbose only failing test cases get printed.
Test casees that pass print nothing.
If you add -- verbose then the passing test cases will also be printed.

'''

#1
def largest(xs):
    '''
    Return the largest element in a list.

    >>> largest([1,2,3])
    3
    >>> largest([99,-56,80,100,90])
    100
    >>> largest(list(range(0,100)))
    99
    >>> largest([10])
    10
    >>> largest([])
    '''
    if xs == []:
        return None
    accumulator = 0     #accumulator pattern
    for x in xs: #for singular in plural 
        if x > accumulator:
            accumulator = x     #updates accumulator to be the biggest thing we've seen so far
    return accumulator


#2
def largest3(xs):
    '''
    Return the largest 3 elements in a list in sorted order.

    >>> largest3([1,2,3])
    [1, 2, 3]
    >>> largest3([99,-56,80,100,90])
    [90, 99, 100]
    >>> largest3(list(range(0,100)))
    [97, 98, 99]
    >>> largest3([10])
    [10]
    >>> largest3([])
    []
    '''
    xs.sort()
    return xs[-3:]


#3
def filter_odd(xs):
    '''
    Return a list with all the odd elements removed.

    The right way to "remove" lines from a list is to create
    a new empty list and add elements you don't want removed to 
    the empty list.

    HINT:
    Use the accumulator pattern with a for loop.

    >>> filter_odd([2,4,6])
    [2, 4, 6]
    >>> filter_odd([1,3,5])
    []
    >>> filter_odd([4,5,6,7])
    [4, 6]
    >>> filter_odd([20,13,4,16,8,19,10])
    [20, 4, 16, 8, 10]
    '''
    accumulator = []
    for x in xs:
        if x%2 == 0:    #means it is EVEN
            accumulator.append(x)
    return accumulator


#4
def nested_filter_odd(xss):
    '''
    Convert a list of lists into a single list that contains only the even elements.

    >>> nested_filter_odd([[2, 4, 5], [1, 3, 6]])
    [2, 4, 6]
    >>> nested_filter_odd([[1, 3, 6]])
    [6]
    >>> nested_filter_odd([[4, 5], [6, 7]])
    [4, 6]
    >>> nested_filter_odd([[20],[13,4,16,8,19],[10], [15, 13, 1]])
    [20, 4, 16, 8, 10]
    '''
    accumulator = []
    for xs in xss:
        for x in xs:
            if x%2 == 0:    #means it is EVEN
                accumulator.append(x)
    return accumulator


# These dictionaries store the grades of famous people in their math, english, and economics classes.
# You shouldn't modify these dictionaries,
# they are used in the doctests for the functions below.
math_grades={
        'donald knuth':85,
        'hypatia':75,
        'emmy noether':86,
        'leonhard euler':92,
        'grigori perelman':95,
        'alexander grothendieck':95,
        'shelton cooper':72,
        'ada lovelace':96,
        }

english_grades={
        'emily dickenson':92,
        'edgar allan poe':88,
        'william shakespeare':84,
        'robert frost':83,
        'dorthy day':95,
        'douglas adams':42,
        'maya angelou':89,
        'emma goldman':85,
        }

economics_grades={
        'christine lagarde':85,
        'alan greenspan':92,
        'adam smith':88,
        'kristalina georgieva':79,
        'karl marx':90,
        'pierre-joseph proudhon':95,
        }


#5
def get_number_of_students_in_class(d):
    '''
    Return the total number of entries in the dictionary.

    >>> get_number_of_students_in_class(math_grades)
    8
    >>> get_number_of_students_in_class(english_grades)
    8
    >>> get_number_of_students_in_class(economics_grades)
    6
    '''
    #in interactive mode, type in >>> len(math_grades) to see that it returns 8
    return len(d)


#6
def highest_grade(d):
    '''
    Return the largest value.

    >>> highest_grade(math_grades)
    96
    >>> highest_grade(english_grades)
    95
    >>> highest_grade(economics_grades)
    95
    '''
    return max(d.values())