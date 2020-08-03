def beggars(values, n):
    suma = []
    for iter in range(n):
        suma.append(sum(values[i] for i in range(iter,len(values),n)))
    return suma

if __name__ == '__main__':
    print(beggars([1,2,3,4,5], 2))
    print(beggars([1,2,3,4,5], 3))