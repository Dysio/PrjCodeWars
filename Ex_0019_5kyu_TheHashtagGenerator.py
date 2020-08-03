def generate_hashtag(s):
    if s == '':
        return False

    sentence = ''.join([word.capitalize() for word in s.split()])

    if len(sentence) > 140:
        return False
    return '#' + sentence

if __name__ == '__main__':
    s = 'Hello there thanks for trying my Kata'
    s_table = s.split()
    print(s_table)
    capitalize_table = [word.capitalize() for word in s_table]
    sentence = ''.join([word.capitalize() for word in s_table])
    print(sentence)
    print(len(sentence))

    print(generate_hashtag(s))
    print(generate_hashtag(''))
    print(generate_hashtag('sbfsd'*100))