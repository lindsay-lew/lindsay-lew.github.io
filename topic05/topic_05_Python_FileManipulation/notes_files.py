# this is on every machine except windows how to specify the path 
# on windows; you need to use two backslashes instead of a forward slash 
# on windows: 
# filename = 'topic_05_Python_FileManipulation\\example_file_1'

filename = 'topic_05_Python_FileManipulation/example_file_1'
# above is called a "relative path"
# a path is relative if on windows: it does not start with c:\\
# on non-windows: it does not start with /

# alternative is called an absolute path: starts with a / or a drive name 
filename = '/Users/Lindsay/Documents/GitHub/lindsay-lew.github.io/topic05/topic_05_Python_FileManipulation/example_file_1'

# first argument isn't actually the name of the file; it's the path to the file
# path is the directories/folders + filename 
'''
with open(filename, 'rb') as fin:
    # 'r' means read
    # 'b' means bytes
    contents = fin.read()
    contents = contents.decode('utf32')
print(contents)

First takeaway from this problem above is that you can't open a file if you don't know the encoding 
'''

'''
# you can do the problem above in less steps below
with open(filename, 'rt', encoding = 'utf32') as fin:   #specify what encoding to use 
    # 't' means text
    contents = fin.read()
print(contents)
'''

'''
#File 2
filename = '/Users/Lindsay/Documents/GitHub/lindsay-lew.github.io/topic05/topic_05_Python_FileManipulation/example_file_2'
with open(filename, 'rt', encoding ='utf16') as fin:
    contents = fin.read()
print(contents)
'''

'''
#File 4
filename = '/Users/Lindsay/Documents/GitHub/lindsay-lew.github.io/topic05/topic_05_Python_FileManipulation/example_file_4'
with open(filename, 'rt', encoding ='euc_jis_2004') as fin:
    contents = fin.read()
print(contents)
'''

#File 4
filename = '/Users/Lindsay/Documents/GitHub/lindsay-lew.github.io/topic05/topic_05_Python_FileManipulation/example_file_4'
try:
    with open(filename, 'rt', encoding ='utf8') as fin:
        contents = fin.read()
except UnicodeDecodeError:
    try:
        with open(filename, 'rt', encoding='utf16') as fin:
            contents = fin.read()
    except UnicodeError:
        with open(filename, 'rt', encoding='euc_jis_2004') as fin:
            contents = fin.read()
    print(contents)
