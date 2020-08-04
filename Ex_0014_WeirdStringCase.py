def to_weird_case(string):
    list_of_words = string.split_and_add()
    new_list_of_words = []
    for word in list_of_words:
        i = 0
        for letter in range(len(word)//2):
            new_word = word[i].upper() + word[i+1].lower()
            i += 2
        new_list_of_words.append(new_word)
    return new_list_of_words

if __name__ == '__main__':
    string = 'This is a test'
    print(to_weird_case(string))
    word = 'This'
    new_word = [word[i].upper() + word[i + 1].lower() for i in range(0, len(word)//2, 2)]
    print(new_word)