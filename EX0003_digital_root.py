def digital_root(n):
    """A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n.
    If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
    This is only applicable to the natural numbers.
    digital_root(493193)
    => 4 + 9 + 3 + 1 + 9 + 3
    => 29 ...
    => 2 + 9
    => 11 ...
    => 1 + 1
    => 2"""
    sum = 0
    for digit in str(n):
        sum += int(digit)
    if sum < 10:
        return sum
    return digital_root(sum)


if __name__ == '__main__':
    print(digital_root(942))
    print(digital_root(132189))
    print(digital_root(493193))
