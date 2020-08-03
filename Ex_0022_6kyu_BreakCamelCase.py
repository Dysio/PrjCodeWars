def solution(s):
    # sentence = ''
    # for letter in s:
    #     if letter == letter.upper():
    #         sentence += ' '
    #     sentence += letter

    sentence = ''.join([letter if letter == letter.lower() else ' ' + letter for letter in s])

    return sentence

if __name__ == '__main__':
    sentence = 'camelCasingTestBigLetters'

    print(solution(sentence))

    # sentence1 = ''.join([letter for letter in s if letter == letter.lower() else ' '])
    sentence2 = ''.join([letter if letter == letter.lower() else ' ' + letter for letter in sentence])
    print(sentence2)