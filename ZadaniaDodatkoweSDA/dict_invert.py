def dict_invert(d):
    """
    :param d: dict
    :return: an inverted dictionary according to the instructions above
    """
    dic = {}
    for key, value in d.items():
        if value not in dic.keys():
            dic[value] = [key]
        elif value in dic.keys():
            dic[value].append(key)
            dic[value].sort()


    return dic

if __name__ == '__main__':
    e = [
        {'given': {1: 10, 2: 20, 3: 30}, 'expected': {10: [1], 20: [2], 30: [3]}},
        {'given': {1: 10, 2: 20, 3: 30, 4: 30}, 'expected': {10: [1], 20: [2], 30: [3, 4]}},
        {'given': {4: True, 2: True, 0: True}, 'expected': {True: [0, 2, 4]}},
    ]
    for element in e:
        result = dict_invert(element['given'])
        print(result, element['expected'])
        assert result == element['expected']

    # dic = dict_invert({1: 10, 2: 20, 3: 30})
    # dic = dict_invert({1: 10, 2: 20, 3: 30, 4: 30})
    # dic = {1: 10, 2: 20, 3: 30}
    # dic[1] = []
    # dic[1].append(10)
    # dic[1].append(12)
    # dic[1].append(13)
    # print(dic[1])
    # print(dic)