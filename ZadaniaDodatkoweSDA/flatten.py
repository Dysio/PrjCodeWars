def flatten(aList):
    """
    :param aList:
    :return: Returns a copy of aList, which is a flattened version of aList
    """
    # flatten_list = []
    for item in aList:
        if type(item) is list:
            list_value = flatten(item)
            flatten_list.append(list_value)
        elif type(item) is not list:
            if 'flatten_list' in locals() or 'flatten_list' in globals():
                flatten_list.append(item)
            else:
                flatten_list = []
                flatten_list.append(item)
    return flatten_list

def flatten_2(aList):
    for item in aList:
        if type(item) is not list:
            return item
        elif type(item) is list:
            return flatten_2(item)
    # return flatten_list

if __name__ == '__main__':
    # print(flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]))
    # assert flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]) == [1, 'a', 'cat', 2, 3, 'dog', 4, 5]

    print(flatten_2([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]))
