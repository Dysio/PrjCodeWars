def first_non_repeating_letter(string):
    #your code here
    for letter in string.lower():
        if string.lower().count(letter) == 1:
            return string[string.lower().index(letter)]
    return ''

if __name__ == '__main__':
    string = 'sTreSS'
    print(first_non_repeating_letter('stress'))
    print(first_non_repeating_letter('sTreSS'))
    print(first_non_repeating_letter('a'))
    # print(first_non_repeating_letter('aa'))
    # print(first_non_repeating_letter('aab'))
    # print(string[string.index('T')])


