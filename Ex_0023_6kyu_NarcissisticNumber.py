def narcissistic( value ):
    # val_sum = sum([int(num)**len(str(value)) for num in str(value)])
    return  value == sum([int(num)**len(str(value)) for num in str(value)])
    # return val_sum

if __name__ == '__main__':
    print(narcissistic(153))