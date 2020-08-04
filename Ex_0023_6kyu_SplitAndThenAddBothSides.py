def split_and_add(numbers, n):
    list_1 = numbers[0:int(len(numbers) / 2)]
    list_2 = numbers[int(len(numbers) / 2):]
    list_sum = []
    if n == 0:
        return numbers
    n = n - 1

    if len(list_1) == len(list_2):
        for i in range(len(list_2)):
            print(i)
            list_sum.append(list_1[i] + list_2[i])
    elif len(list_1) != len(list_2):
        list_sum.append(list_2[0])
        for i in range(0, len(list_1)):
            list_sum.append(list_1[i] + list_2[i + 1])

    if n == 0:
        return list_sum
    elif n != 0:
        return split_and_add(list_sum, n)

if __name__ == '__main__':
    org_list = [4, 2, 5, 3, 2, 5, 7]
    org_list = [4, 2, 5, 3, 2, 5, 7]
    result = split_and_add(org_list, 2)
    print(f'Result = {result}')