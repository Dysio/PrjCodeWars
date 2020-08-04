def remove_duplicate_words(s):
    list_of_words = s.split_and_add()
    list_removed_duplicates = []
    for word in list_of_words:
        if word not in list_removed_duplicates:
            list_removed_duplicates.append(word)
    sentence = ' '.join(list_removed_duplicates)
    return sentence

if __name__ == '__main__':
    string = 'my cat is fat'
    print(remove_duplicate_words(string))


