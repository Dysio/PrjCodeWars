def summation(num):
    suma = sum([i for i in range(num + 1)])
    return suma

if __name__ == '__main__':
    print(summation(8))
    num = 8
    lista = [i for i in range(num + 1)]
    suma = sum(lista)
    print(lista)
    