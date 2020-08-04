def infected(s):
    list_of_countries = s.split_and_add('X')
    return list_of_countries

if __name__ == '__main__':
    map1 = "01000X000X011X0X"
    print(infected(map1))