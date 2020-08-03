import unittest

def find_odd_int(seq):
    dictionary = {key : 0 for key in set(seq)}
    for number in seq:
        dictionary[number] += 1
    for key, value in dictionary.items():
        if value % 2 != 0:
            return (key)


# class Tests(unittest.TestCase):
#
#     def test_almost_equal(self):
#         with self.assertAlmostEqual()

if __name__ == '__main__':
    testarray = [1,1,1,2,2,3,3,4,4,5,5,6,6]

    find_odd_int(testarray)
    print(find_odd_int(testarray))

    # dictionary = {key : 0 for key in set(testarray)}
    # print(dictionary)
    string = 'sdafdsfaEnglish'
    if 'English' in string:
        print('true')
