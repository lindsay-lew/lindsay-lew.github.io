#Problem 1
def compile_italic_star(line):
    result = ''
    i = 0
    while i < len(line):
        if line[i] == '*':
            if i + 1 < len(line) and '*' in line[i+1:]:
                end = line.find('*', i+1)
                result += '<i>' + line[i+1:end] + '</i>'
                i = end + 1
            else:
                result += '*'
                i += 1
        else:
            result += line[i]
            i += 1

    return result
result = compile_italic_star('alpha *beta* gamma *delta')
print(result)


#Problem 2
def compile_italic_star(line):
    result = ''
    i = 0
    while i < len(line):
        if line[i] == '*':
            end = line.find('*', i+1)
            if end != -1:
                result += '<i>' + line[i+1:end] + '</i>'
                i = end + 1
            else:
                i = len(line)
        else:
            result += line[i]
            i += 1
    return result
result = compile_italic_star('alpha *beta* gamma *delta')
print(result)


#Problem 3
def compile_italic_star(line):
    result = ''
    i = 0
    while i < len(line):
        if line[i] == '*':
            end = line.find('*', i+1)
            if end != -1:
                result += '<i>' + line[i+1:end] + '</i>'
                i = end + 1
            else:
                i = len(line)
        else:
            result += line[i]
            i += 1
    return result
result = compile_italic_star('alpha *beta* gamma *delta*')
print(result)


#Problem 4
def compile_italic_star(line):
    result = ''
    i = 0
    while i < len(line):
        if line[i] == '*':
            end = line.find('*', i+1)
            if end != -1:
                result += '<i>' + line[i+1:end] + '</i>'
                i = end + 1
            else:
                i = len(line)
        else:
            result += line[i]
            i += 1
    return result
result = compile_italic_star('alpha *beta gamma delta')
print(result)


#Problem 5
def compile_italic_star(line):
    result = ''
    i = 0
    while i < len(line):
        if line[i] == '*':
            end = line.find('*', i+1)
            if end != -1:
                result += '<i>' + line[i+1:end] + '</i>'
                i = end + 1
            else:
                i += 1
        else:
            result += line[i]
            i += 1
    return result
result = compile_italic_star('alpha *beta* gamma *delta')
print(result)


#Problem 6
def compile_italic_star(line):
    result = ''
    i = 0
    while i < len(line):
        if line[i] == '*':
            end = line.find('*', i+1)
            if end != -1:
                result += '<i>' + line[i+1:end] + '</i>'
                i = end + 1
            else:
                i += 1
        else:
            result += line[i]
            i += 1
    return result
result = compile_italic_star('alpha *beta gamma delta')
print(result)


#Problem 7
def compile_italic_star(line):
    result = ''
    i = 0
    while i < len(line):
        if line[i] == '*':
            end = line.find('*', i+1)
            if end != -1:
                result += '<i>' + line[i+1:end] + '</i>'
                i = end + 1
            else:
                i += 1
        else:
            result += line[i]
            i += 1
    return result
result = compile_italic_star('alpha *beta gamma delta*')
print(result)


#Problem 8
def compile_bold_stars(line):
    start = line.find('**')
    if start == -1 or len(line) < 4:
        return line
    end = line[start + 2:].find('**')
    if end == -1:
        return line
    end = end + start + 2
    return line[:start] + '<b>' + line[start + 2:end] + '</b>' + line[end + 2:]
result = compile_bold_stars('alpha **beta** gamma **delta**')
print(result)


#Problem 9
def compile_bold_stars(line):
    start = line.find('**')
    if start == -1 or len(line) < 4:
        return line
    end = line[start + 2:].find('**')
    if end == -1:
        return line
    end = end + start + 2
    return line[:start] + '<b>' + line[start + 2:end] + '</b>' + line[end + 2:]
result = compile_bold_stars('alpha **beta** gamma **delta')
print(result)


#Problem 10
def compile_bold_stars(line):
    start = line.find('**')
    if start == -1 or len(line) < 4:
        return line
    end = line[start + 2:].find('**')
    if end == -1:
        return line
    end = end + start + 2
    return line[:start] + '<b>' + line[start + 2:end] + '</b>' + line[end + 2:]
result = compile_bold_stars('alpha beta gamma **delta')
print(result)

line = ('alpha')
print(len(line))