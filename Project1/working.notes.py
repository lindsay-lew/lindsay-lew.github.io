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


    #QCL ANSWER
"""
    length = len(line)
    between_italics = False

    text = ''
    between_italics_string = ''

    for i in range(length):
        if (between_italics == True) and (i == length - 1): #reached end of the string
            text += between_italics_string + line[i]

        elif (line[i] == '*') and (between_italics == False): #open italics
            between_italics_string += "*"
            between_italics = True

        elif (line[i] == '*') and (between_italics == True): #close italics and append
            text += "<i>" + between_italics_string[1:] + "</i>"
            between_italics_string = ''
            between_italics = False

        elif between_italics == True:
            between_italics_string += line[i]

        else:
            between_italics == False
            text += line[i]

    print(text)
    return text
"""


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

    """
    between_backticks = False
    text = ''
    between_backticks_string = ''

    for char in line:
        if char == '`' and not between_backticks:  # Open code
            between_backticks = True
            between_backticks_string = ''  # Reset collected text

        elif char == '`' and between_backticks:  # Close code
            text += f"<code>{between_backticks_string}</code>"
            between_backticks = False  # Reset flag

        elif between_backticks:
            between_backticks_string += char  # Collect text inside code

        else:
            text += char  # Regular characters outside code

    # If code was never closed, restore the unmatched '`'
    if between_backticks:
        text += '`' + between_backticks_string

    return text
    """
    
    """
    parts = line.split('`')  # Split by backticks
    for i in range(1, len(parts), 2):  # Process only code parts (odd indices)
        parts[i] = f'<code>{parts[i].replace("<", "&lt;").replace(">", "&gt;")}</code>'
    
    return ''.join(parts)  # Reconstruct the string
    """



# Problem 12
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

# QCL DRAFT ANSWER
'''
    length = len(html)
    
    in_white = False

    accumulator = ''

    for i in range(length):
        #c is our character
        c = html[i] 

        #start spaces
        if in_white == False:
            if c == " " or c == "\n":
                accumulator.append(" ")
                in_white = True
            else:
                accumulator.append(c)
                in_white = False
        if in_white == True:
            if c != " " and c != "\n":
                accumulator.append(c)
                in_white = False
        
# QCL ANSWER
    #return re.sub(r'\s+', ' ', html.strip()) commented out solution
    return accumulator

'''
