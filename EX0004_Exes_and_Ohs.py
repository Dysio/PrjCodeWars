def xo(s):
    """Check to see if a string has the same amount of 'x's and 'o's.
    The method must return a boolean and be case insensitive. The string can contain any char."""
    dictionary = {'x': 0, 'o': 0}
    for i in s:
        if i.lower() == 'x':
            dictionary['x'] += 1
        elif i.lower() == 'o':
            dictionary['o'] += 1

    return dictionary['x'] == dictionary['o']

def xo_2(s):
    s = s.lower()
    return s.count('x') == s.count('o')

if __name__ == '__main__':
    print(xo("ooxx"))
    print(xo("ooxxxsafdab"))
    print(xo("abcgfda"))
    print(xo("ooxX"))
    print(xo_2("ooxX"))
