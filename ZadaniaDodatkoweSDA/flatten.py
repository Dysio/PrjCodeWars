def flatten(aList):
    """
    :param aList:
    :return: Returns a copy of aList, which is a flattened version of aList
    """
    output = []
    def flatten_nested(aList):
        for elem in aList:
            if type(elem) is list:
                flatten_nested(elem)
            else:
                output.append(elem)
        return output

    flatten_nested(aList)

    return output

def flatten2(aList):
    if not isinstance(aList, list):
        return aList

    result = []
    for i in aList:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result

if __name__ == '__main__':
    print(flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]))
    assert flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]) == [1, 'a', 'cat', 2, 3, 'dog', 4, 5]

