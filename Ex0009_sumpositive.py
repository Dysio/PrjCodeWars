def positive_sum(arr):
    # Your code here
    return sum(list(filter(lambda x: x > 0, arr)))

if __name__ == '__main__':
    # suma = sum(map(lambda x: x if x > 0, [1,-2,3]))
    lista = map(lambda x: x > 0, [1,-2,3])
    print(list(lista))
    nowa_lista = list(filter(lambda x: x > 0, [1,-2,3]))
    print(nowa_lista)
    suma = sum(list(filter(lambda x: x > 0, [1,-2,3])))
    print(suma)
    print(positive_sum([1,-4,7,12]))