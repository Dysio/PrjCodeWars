class DefaultList:

    def __init__(self, input_list, default_value):
        self.input_list = input_list
        self.default_value = default_value



if __name__ == '__main__':
    lst = DefaultList([1, 3, 4, 7, 2, 34], 'def')

    print(lst[2])