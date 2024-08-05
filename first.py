def dumplings(input1, input2):
    maximum =0
    for i in range(input1):
        maximum = max(maximum, input2[i])
    count = [0] * (maximum +1)
    for i in range(input1):
        count[input2[i]]+=1
    result =[0] *(maximum +1)
    result[0] =0
    for num in range (1, maximum +1):
        k=max(num-1-1, 0)
        result[num] = max(result[num-1], num*count[num] + result[k])
    return result[maximum]

input1=5
input2=[3,3,4,5,4]
print(dumplings(input1, input2))

