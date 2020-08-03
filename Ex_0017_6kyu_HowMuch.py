def howmuch(m, n):
    # your code
    answer_list = []
    for M in range(min(m,n),max(m,n)+1):
        if (M - 1) % 9 == 0 and (M - 2) % 7 == 0:
            answer_list.append([f"M:{M}", f"B:{int((M-2)/7)}", f"C:{int((M - 1)/9)}"])
    # return answer_list

    # list comprehension
    # answer_list = [[f"M:{M}", f"B:{int((M-2)/7)}", f"C:{int((M - 1)/9)}"] for M in range(min(m,n),max(m,n)+1) if (M - 1) % 9 == 0 and (M - 2) % 7 == 0]
    return answer_list

if __name__ == '__main__':
    for m in range(3,10+1):
        print(m)

    result = 10 % 3
    print(result)

    print(howmuch(1, 100))