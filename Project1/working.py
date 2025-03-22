
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
    