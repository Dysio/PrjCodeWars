def perimeter(n):

    if n in (1,2):
        return 1
    elif n > 2:
        return perimeter(n-2) + perimeter(n-1)
    
    # return 4*sum(perimeter(number) for number in range(0, n))

if __name__ == '__main__':
    print(perimeter(7))