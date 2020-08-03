def tribonacci(signature, n):
    #your code here
    output_list = signature[:n]
    for i in range(0, n - 3):
        output_list.append(sum(output_list[-3:]))
    return output_list


print(tribonacci([0,0,1],0))
print(tribonacci([0,0,1],3))
print(tribonacci([0,0,1],4))
print(tribonacci([0,0,1],10))
print(tribonacci([1,1,1],1))