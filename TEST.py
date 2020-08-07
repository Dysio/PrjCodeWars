def closest_power(base, num):
    exp = 0
    exp_result = 0
    while base ** exp < num:
        if num - base ** exp < base ** (exp+1) - num:
            exp_result = exp
        if num - base ** exp > base ** (exp + 1) - num:
            exp_result = exp + 1
        exp += 1

    return exp_result


if __name__ == '__main__':
    assert closest_power(4, 12) == 2
    assert closest_power(3, 12) == 2
    assert closest_power(4, 1) == 0

