#!/usr/bin/python3
import re
# $ python3 Project1/markdown_compiler.py --input_file=Project1/README.md --add_css
'''
This script converts markdown documents into HTML documents.

Each function has its own doctests (just like in lab),
and you should begin this assignment by solving the doctests (just like in lab).
This will let you focus on completing just one small piece of the assignment at a time and not get lost in the "big picture".
Then, once all of these small pieces are complete,
the entire assignment should just work "magically".

Dividing up a large project into smaller "doctestable" components is more of an art than a science.
As you get more experience programming,
you'll slowly learn how to divide up your code this way for yourself.
This is one of the main skills that separates senior programmers from junior programmers.

There's a handful of coding techniques in here that we haven't covered in class and you're not expected to understand.
This is intentional.
An important skill when learning a programming language is being able to work in an environment that you don't 100% understand.
(Again, this is similar to when learning a human language...
when we learn a new human languages,
we won't 100% understand everything in the new language,
but we still have to be able to work with the parts that we do understand.)

WARNING:
Recall that the technology policy places no restriction on your ability to use AI tools like ChatGPT or copilot.
Many of the simpler functions below can be solved directly with the tools.
But I strongly encourage you not to just copy/paste solutions from these tools into the homework.
The more complex functions below cannot be solved by current AI tools.
If you use AI as a crutch to solve the simple problems for you,
you will not be able to solve the more difficult problems.
'''

################################################################################
#
# The functions in this section operate on only a single line of text at a time.
#
################################################################################


# Problem 1
def compile_headers(line):
    '''
    Convert markdown headers into <h1>,<h2>,etc tags.

    HINT:
    This is the simplest function to implement in this assignment.
    Use a slices to extract the first part of the line,
    then use if statements to check if they match the appropriate header markdown commands.

    >>> compile_headers('# This is the main header')
    '<h1> This is the main header</h1>'
    >>> compile_headers('## This is a sub-header')
    '<h2> This is a sub-header</h2>'
    >>> compile_headers('### This is a sub-header')
    '<h3> This is a sub-header</h3>'
    >>> compile_headers('#### This is a sub-header')
    '<h4> This is a sub-header</h4>'
    >>> compile_headers('##### This is a sub-header')
    '<h5> This is a sub-header</h5>'
    >>> compile_headers('###### This is a sub-header')
    '<h6> This is a sub-header</h6>'
    >>> compile_headers('      # this is not a header')
    '      # this is not a header'
    '''
    if line[0:2] == '# ':
        line = '<h1> ' + line[2:] + '</h1>'
    if line[0:3] == '## ':
        line = '<h2> ' + line[3:] + '</h2>'
    if line[0:4] == '### ':
        line = '<h3> ' + line[4:] + '</h3>'
    if line[0:5] == '#### ':
        line = '<h4> ' + line[5:] + '</h4>'    
    if line[0:6] == '##### ':
        line = '<h5> ' + line[6:] + '</h5>'
    if line[0:7] == '###### ':
        line = '<h6> ' + line[7:] + '</h6>'    
    return line


# Problem 2
def compile_italic_star(line):
    '''
    Convert "*italic*" into "<i>italic</i>".

    HINT:
    Italics require carefully tracking the beginning and ending positions of the text to be replaced.
    This is similar to the `delete_HTML` function that we implemented in class.
    It's a tiny bit more complicated since we are not just deleting substrings from the text,
    but also adding replacement substrings.

    >>> compile_italic_star('*This is italic!* This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_star('*This is italic!*')
    '<i>This is italic!</i>'
    >>> compile_italic_star('This is *italic*!')
    'This is <i>italic</i>!'
    >>> compile_italic_star('This is not *italic!')
    'This is not *italic!'
    >>> compile_italic_star('*')
    '*'
    '''
    between_italics = False
    text = ''
    between_italics_string = ''

    for char in line:
        if char == '*' and not between_italics:  # Open italics
            between_italics = True
            between_italics_string = ''  # Reset collected text

        elif char == '*' and between_italics:  # Close italics
            text += f"<i>{between_italics_string}</i>"
            between_italics = False  # Reset flag

        elif between_italics:
            between_italics_string += char  # Collect text inside italics

        else:
            text += char  # Regular characters outside italics

    # If italics were never closed, restore the unmatched '*'
    if between_italics:
        text += '*' + between_italics_string

    return text


# Problem 3
def compile_italic_underscore(line):
    '''
    Convert "_italic_" into "<i>italic</i>".

    HINT:
    This function is almost exactly the same as `compile_italic_star`.

    >>> compile_italic_underscore('_This is italic!_ This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_underscore('_This is italic!_')
    '<i>This is italic!</i>'
    >>> compile_italic_underscore('This is _italic_!')
    'This is <i>italic</i>!'
    >>> compile_italic_underscore('This is not _italic!')
    'This is not _italic!'
    >>> compile_italic_underscore('_')
    '_'
    '''
    between_italics = False
    text = ''
    between_italics_string = ''

    for char in line:
        if char == '_' and not between_italics:  # Open italics
            between_italics = True
            between_italics_string = ''  # Reset collected text

        elif char == '_' and between_italics:  # Close italics
            text += f"<i>{between_italics_string}</i>"
            between_italics = False  # Reset flag

        elif between_italics:
            between_italics_string += char  # Collect text inside italics

        else:
            text += char  # Regular characters outside italics

    # If italics were never closed, restore the unmatched '_'
    if between_italics:
        text += '_' + between_italics_string

    return text


# Problem 4
def compile_strikethrough(line):
    '''
    Convert "~~strikethrough~~" to "<ins>strikethrough</ins>".

    HINT:
    The strikethrough annotations are very similar to implement as the italic function.
    The difference is that there are two delimiting characters instead of one.
    This will require carefully thinking about the range of your for loop and all of your list indexing.

    >>> compile_strikethrough('~~This is strikethrough!~~ This is not strikethrough.')
    '<ins>This is strikethrough!</ins> This is not strikethrough.'
    >>> compile_strikethrough('~~This is strikethrough!~~')
    '<ins>This is strikethrough!</ins>'
    >>> compile_strikethrough('This is ~~strikethrough~~!')
    'This is <ins>strikethrough</ins>!'
    >>> compile_strikethrough('This is not ~~strikethrough!')
    'This is not ~~strikethrough!'
    >>> compile_strikethrough('~~')
    '~~'
    '''
    text = ''
    i = 0
    between_tildes = False
    between_tildes_string = ''

    while i < len(line):
        # Check for "~~" at current position
        if line[i:i+2] == '~~':
            if between_tildes:  # Closing strikethrough tag
                text += f"<ins>{between_tildes_string}</ins>"
                between_tildes_string = ''
                between_tildes = False
            else:  # Opening strikethrough tag
                between_tildes = True
            i += 1  # Skip the second '~' in the pair
        
        elif between_tildes:
            between_tildes_string += line[i]  # Collect text inside strikethrough
        
        else:
            text += line[i]  # Append normal text

        i += 1

    # If strikethrough was never closed, restore unmatched '~~'
    if between_tildes:
        text += '~~' + between_tildes_string

    return text 


# Problem 5
def compile_bold_stars(line):
    '''
    Convert "**bold**" to "<b>bold</b>".

    HINT:
    This function is similar to the strikethrough function.

    >>> compile_bold_stars('**This is bold!** This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_stars('**This is bold!**')
    '<b>This is bold!</b>'
    >>> compile_bold_stars('This is **bold**!')
    'This is <b>bold</b>!'
    >>> compile_bold_stars('This is not **bold!')
    'This is not **bold!'
    >>> compile_bold_stars('**')
    '**'
    '''
    text = ''
    i = 0
    between_stars = False
    between_stars_string = ''

    while i < len(line):
        # Check for "**" at current position
        if line[i:i+2] == '**':
            if between_stars:  # Closing bold tag
                text += f"<b>{between_stars_string}</b>"
                between_stars_string = ''
                between_stars = False
            else:  # Opening bold tag
                between_stars = True
            i += 1  # Skip the second '*' in the pair
        
        elif between_stars:
            between_stars_string += line[i]  # Collect text inside bold
        
        else:
            text += line[i]  # Append normal text

        i += 1

    # If strikethrough was never closed, restore unmatched '**'
    if between_stars:
        text += '**' + between_stars_string

    return text 
    

# Problem 6 
def compile_bold_underscore(line):
    '''
    Convert "__bold__" to "<b>bold</b>".

    HINT:
    This function is similar to the strikethrough function.

    >>> compile_bold_underscore('__This is bold!__ This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_underscore('__This is bold!__')
    '<b>This is bold!</b>'
    >>> compile_bold_underscore('This is __bold__!')
    'This is <b>bold</b>!'
    >>> compile_bold_underscore('This is not __bold!')
    'This is not __bold!'
    >>> compile_bold_underscore('__')
    '__'
    '''
    text = ''
    i = 0
    between_underscore = False
    between_underscore_string = ''

    while i < len(line):
        # Check for "**" at current position
        if line[i:i+2] == '__':
            if between_underscore:  # Closing bold tag
                text += f"<b>{between_underscore_string}</b>"
                between_underscore_string = ''
                between_underscore = False
            else:  # Opening bold tag
                between_underscore = True
            i += 1  # Skip the second '_' in the pair
        
        elif between_underscore:
            between_underscore_string += line[i]  # Collect text inside bold
        
        else:
            text += line[i]  # Append normal text

        i += 1

    # If bold was never closed, restore unmatched '__'
    if between_underscore:
        text += '__' + between_underscore_string

    return text 


# Problem 7 
def compile_code_inline(line):
    '''
    Add <code> tags.

    HINT:
    This function is like the italics functions because inline code uses only a single character as a delimiter.
    It is more complex, however, because inline code blocks can contain valid HTML inside of them,
    but we do not want that HTML to get rendered as HTML.
    Therefore, we must convert the `<` and `>` signs into `&lt;` and `&gt;` respectively.

    >>> compile_code_inline('You can use backticks like this (`1+2`) to include code in the middle of text.')
    'You can use backticks like this (<code>1+2</code>) to include code in the middle of text.'
    >>> compile_code_inline('This is inline code: `1+2`')
    'This is inline code: <code>1+2</code>'
    >>> compile_code_inline('`1+2`')
    '<code>1+2</code>'
    >>> compile_code_inline('This example has html within the code: `<b>bold!</b>`')
    'This example has html within the code: <code>&lt;b&gt;bold!&lt;/b&gt;</code>'
    >>> compile_code_inline('this example has a math formula in the  code: `1 + 2 < 4`')
    'this example has a math formula in the  code: <code>1 + 2 &lt; 4</code>'
    >>> compile_code_inline('this example has a <b>math formula</b> in the  code: `1 + 2 < 4`')
    'this example has a <b>math formula</b> in the  code: <code>1 + 2 &lt; 4</code>'
    >>> compile_code_inline('```')
    '```'
    >>> compile_code_inline('```python3')
    '```python3'
    '''
    if line.count('`') < 2:  # If there's no pair of backticks, return as is
        return line

    if line.count('`') > 2:  # If there's no pair of backticks, return as is
        return line
    
    #if '```' in line:  # Ignore triple backticks, return original string (TAKING THIS OUT BECAUSE I DON'T WANT HARDCODED FOR SPECIFIC CASE OF TRIPLE BACKTICK)
    #    return line  

    parts = line.split('`')  # Split by backticks
    if len(parts) % 2 == 0:  # Odd number of backticks means a mismatch, return original
        return line  

    for i in range(1, len(parts), 2):  # Process only code parts (odd indices)
        parts[i] = f'<code>{parts[i].replace("<", "&lt;").replace(">", "&gt;")}</code>'
    
    return ''.join(parts)  # Reconstruct the string


# Problem 8
def compile_links(line):
    '''
    Add <a> tags.

    HINT:
    The links and images are potentially more complicated because they have many types of delimeters: `[]()`.
    These delimiters are not symmetric, however, so we can more easily find the start and stop locations using the strings find function.

    >>> compile_links('Click on the [course webpage](https://github.com/mikeizbicki/cmc-csci040)!')
    'Click on the <a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>!'
    >>> compile_links('[course webpage](https://github.com/mikeizbicki/cmc-csci040)')
    '<a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>'
    >>> compile_links('this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)')
    'this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)'
    >>> compile_links('this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040')
    'this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040'
    '''
    result = ''
    i = 0
    while i < len(line):
        # Check for the start of a Markdown link
        if line[i] == '[':
            start = i
            end_bracket = line.find(']', start)
            if end_bracket != -1:  # Found closing bracket
                url_start = line.find('(', end_bracket)
                url_end = line.find(')', url_start)
                if url_start != -1 and url_end != -1 and url_start == end_bracket + 1:
                    # Valid link found
                    link_text = line[start + 1:end_bracket]
                    url = line[url_start + 1:url_end]
                    result += f'<a href="{url}">{link_text}</a>'
                    i = url_end + 1  # Move past the closing parenthesis
                    continue
        result += line[i]  # If not a link, just add the character
        i += 1
    return result


# Problem 9
def compile_images(line):
    '''
    Add <img> tags.

    HINT:
    Images are formatted in markdown almost exactly the same as links,
    except that images have a leading `!`.
    So your code here should be based off of the <a> tag code.

    >>> compile_images('[Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    '[Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)'
    >>> compile_images('![Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    '<img src="https://avatars1.githubusercontent.com/u/1052630?v=2&s=460" alt="Mike Izbicki" />'
    >>> compile_images('This is an image of Mike Izbicki: ![Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    'This is an image of Mike Izbicki: <img src="https://avatars1.githubusercontent.com/u/1052630?v=2&s=460" alt="Mike Izbicki" />'
    '''
    result = ''
    i = 0
    while i < len(line):
        # Check for the start of a Markdown image
        if line[i:i+2] == '![':
            start = i + 2  # Move past the '!['
            end_bracket = line.find(']', start)
            if end_bracket != -1:  # Found closing bracket
                url_start = line.find('(', end_bracket)
                url_end = line.find(')', url_start)
                if url_start != -1 and url_end != -1 and url_start == end_bracket + 1:
                    # Valid image found
                    alt_text = line[start:end_bracket]
                    url = line[url_start + 1:url_end]
                    result += f'<img src="{url}" alt="{alt_text}" />'
                    i = url_end + 1  # Move past the closing parenthesis
                    continue
        result += line[i]  # If not an image, just add the character
        i += 1
    return result


################################################################################
#
# This next section contains only one function that calls the functions in the previous section.
# This is the "brains" of our application right here.
#
################################################################################


# Problem 10
def compile_lines(text):
    r'''
    Apply all markdown transformations to the input text.

    NOTE:
    This function calls all of the functions you created above to convert the full markdown file into HTML.
    This function also handles multiline markdown like <p> tags and <pre> tags;
    because these are multiline commands, they cannot work with the line-by-line style of commands above.

    NOTE:
    The doctests are divided into two sets.
    The first set of doctests below show how this function adds <p> tags and calls the functions above.
    Once you implement the functions above correctly,
    then this first set of doctests will pass.

    NOTE:
    For your assignment, the most important thing to take away from these test cases is how multiline tests can be formatted.

    >>> compile_lines('This is a **bold** _italic_ `code` test.\nAnd *another line*!\n')
    '<p>\nThis is a <b>bold</b> <i>italic</i> <code>code</code> test.\nAnd <i>another line</i>!\n</p>'

    >>> compile_lines("""
    ... This is a **bold** _italic_ `code` test.
    ... And *another line*!
    ... """)
    '\n<p>\nThis is a <b>bold</b> <i>italic</i> <code>code</code> test.\nAnd <i>another line</i>!\n</p>'

    >>> print(compile_lines("""
    ... This is a **bold** _italic_ `code` test.
    ... And *another line*!
    ... """))
    <BLANKLINE>
    <p>
    This is a <b>bold</b> <i>italic</i> <code>code</code> test.
    And <i>another line</i>!
    </p>

    >>> print(compile_lines("""
    ... *paragraph1*
    ...
    ... **paragraph2**
    ...
    ... `paragraph3`
    ... """))
    <BLANKLINE>
    <p>
    <i>paragraph1</i>
    </p>
    <p>
    <b>paragraph2</b>
    </p>
    <p>
    <code>paragraph3</code>
    </p>

    NOTE:
    This second set of test cases tests multiline code blocks.

    HINT:
    In order to get some of these test cases to pass,
    you will have to both add new code and remove some of the existing code that I provide you.

    >>> print(compile_lines("""
    ... ```
    ... x = 1*2 + 3*4
    ... ```
    ... """))
    <BLANKLINE>
    <pre>
    x = 1*2 + 3*4
    </pre>
    <BLANKLINE>

    >>> print(compile_lines("""
    ... Consider the following code block:
    ... ```
    ... x = 1*2 + 3*4
    ... ```
    ... """))
    <BLANKLINE>
    <p>
    Consider the following code block:
    <pre>
    x = 1*2 + 3*4
    </pre>
    </p>

    >>> print(compile_lines("""
    ... Consider the following code block:
    ... ```
    ... x = 1*2 + 3*4
    ... print('x=', x)
    ... ```
    ... And here's another code block:
    ... ```
    ... print(this_is_a_variable)
    ... ```
    ... """))
    <BLANKLINE>
    <p>
    Consider the following code block:
    <pre>
    x = 1*2 + 3*4
    print('x=', x)
    </pre>
    And here's another code block:
    <pre>
    print(this_is_a_variable)
    </pre>
    </p>

    >>> print(compile_lines("""
    ... ```
    ... for i in range(10):
    ...     print('i=',i)
    ... ```
    ... """))
    <BLANKLINE>
    <pre>
    for i in range(10):
        print('i=',i)
    </pre>
    <BLANKLINE>
    '''
    #convert all lines into a list, every newline 
    lines = text.split('\n')
    new_lines = []
    
    #variable discerning whether or not you're in the paragraph
    in_paragraph = False
    in_pre = False

    #for every line in our list of lines (that are broken up by newlines)
    for line in lines:
        raw = line          #we want to keep the source formatting for our pre tag        
        line = line.strip() #strips white spaces

        #in pre
        if line=='```':
            if in_pre: #if in pre when you see the new pre tag then close and update your variable accordingly
                new_lines.append("</pre>")
                in_pre = False
                continue
            else: #if not in pre when you see the new pre tag then close and updat eyour variable accordingly
                new_lines.append("<pre>")
                in_pre = True
                continue
        elif line != '```' and in_pre:
            new_lines.append(raw)
            continue

        #in paragraph?
        if line=='':
            if in_paragraph:
                #if in paragraph when you see the new paragraph tag then close and update your variable accordingly
                line='</p>'
                in_paragraph = False
        else:
            if line[0] != '#' and not in_paragraph:
                in_paragraph = True
                line = '<p>\n'+line
        
        #running through all of our transformations
            line = compile_headers(line)
            line = compile_strikethrough(line)
            line = compile_bold_stars(line)
            line = compile_bold_underscore(line)
            line = compile_italic_star(line)
            line = compile_italic_underscore(line)
            line = compile_code_inline(line)
            line = compile_images(line)
            line = compile_links(line)

        new_lines.append(line)
    new_text = '\n'.join(new_lines)
    return new_text


def markdown_to_html(markdown, add_css):
    '''
    Convert the input markdown into valid HTML,
    optionally adding CSS formatting.

    NOTE:
    This function is separated out from the `compile_lines` function so that the doctests are much simpler.
    In particular, by splitting these functions in two,
    there's no need to add all of the HTML boilerplate code to the doctests in `compile_lines`.

    NOTE:
    The code for this function is simple enough that we don't even have a "real" doctest.
    The only purpose of this doctest is to run the function and ensure that there are no errors.
    The `assert` function prints no output whenever the input is "truthy".

    >>> assert(markdown_to_html('this *is* a _test_', False))
    >>> assert(markdown_to_html('this *is* a _test_', True))
    '''

    html = '''
<html>
<head>
    <style>
    ins { text-decoration: line-through; }
    </style>
    '''
    if add_css:
        html += '''
<link rel="stylesheet" href="https://izbicki.me/css/code.css" />
<link rel="stylesheet" href="https://izbicki.me/css/default.css" />
        '''
    html+='''
</head>
<body>
    '''+compile_lines(markdown)+'''
</body>
</html>
    '''
    return html


# Problem 11
def minify(html):
    r'''
    Remove redundant whitespace (spaces and newlines) from the input HTML,
    and convert all whitespace characters into spaces.

    NOTE:
    When we transfer HTML files over the internet,
    we'd like them to be as small as possible in order to save bandwidth and make the webpage load faster.
    Minifying html documents is an important step for webservers.
    It may not seem like much, but at the scale of Google/Facebook,
    it can reduce costs by millions of dollars annually.

    >>> minify('       ')
    ''
    >>> minify('   a    ')
    'a'
    >>> minify('   a    b        c    ')
    'a b c'
    >>> minify('a b c')
    'a b c'
    >>> minify('a\nb\nc')
    'a b c'
    >>> minify('a \nb\n c')
    'a b c'
    >>> minify('a\n\n\n\n\n\n\n\n\n\n\n\n\n\nb\n\n\n\n\n\n\n\n\n\n')
    'a b'
    '''
    result = []
    in_white = False  # Track if we are in a whitespace sequence

    for c in html:
        if c in (" ", "\n"):  
            if not in_white:  # Only add a single space for consecutive whitespace
                result.append(" ")
                in_white = True
        else:
            result.append(c)
            in_white = False

    return "".join(result).strip()  # Convert list back to string and remove leading/trailing spaces



def convert_file(input_file, add_css):
    '''
    Convert the input markdown file into an HTML file.
    If the input filename is `README.md`,
    then the output filename will be `README.html`.

    NOTE:
    It is difficult to write meaningful doctests for functions that deal with files.
    This is because we would have to create a bunch of different files to do so.
    Therefore, there are no tests for this function.
    But we can still be confident that this function will work because of the extensive tests on the "helper functions" that this function depends on.
    '''

    # validate that the input file is a markdown file
    if input_file[-3:] != '.md':
        raise ValueError('input_file does not end in .md')

    # load the input file
    with open(input_file, 'r') as f:
        markdown = f.read()

    # generate the HTML from the Markdown
    html = markdown_to_html(markdown, add_css)
    html = minify(html)

    # write the output file
    with open(input_file[:-2]+'html', 'w') as f:
        f.write(html)


################################################################################
#
# This final section does not need to be modified at all.
# It connects commands run in the terminal environment to the python functions above.
#
################################################################################

if __name__ == '__main__':

    # process command line arguments
    import argparse
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True)
    parser.add_argument('--add_css', action='store_true')
    args = parser.parse_args()

    # call the main function
    convert_file(args.input_file, args.add_css)