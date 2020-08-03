def find_short(s):
    # your code here
    l = min([len(i) for i in string.split()])
    return l # l: shortest word length

if __name__ == '__main__':
    string = 'bitcoin take over the world maybe who knows perhaps'
    print(find_short(string))
