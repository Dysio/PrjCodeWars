def fibonacci(n):
    if n == 0:
        return 0
    elif n in (1,2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    print(fibonacci(1))
    for i in range(10):
        print(f'n={i}: {fibonacci(i)}')