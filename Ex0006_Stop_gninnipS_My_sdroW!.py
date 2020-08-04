def spin_words(sentence):
    # Your code goes here
    # list_of_words = sentence.split(' ')
    return ' '.join([i if len(i) < 5 else i[::-1] for i in sentence.split_and_add(' ')])

print(spin_words('string for words'))