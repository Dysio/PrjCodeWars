def create_phone_number(n):
    #your code here
    return "(" + ''.join(str(n[i]) for i in range(0,3)) + ") " + ''.join(str(n[i]) for i in range(3,6)) + "-" + ''.join(str(n[i]) for i in range(6,10))


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
