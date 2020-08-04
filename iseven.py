def iseven(num):
    if num % 2 == 0:
        return True
    return False

if __name__ == '__main__':
    print(iseven(6))
    for num in range(11):
        print(f'{num} is even {iseven(num)}')

    print(4%1)