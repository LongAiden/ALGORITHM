# Uses python3
import sys

def dp_approach(n):
    dp = [0,0]
    array = [0,0]
    for i in range(2, n+1):
        count_3 = count_2 = count_1 = n
        if i % 3 == 0:
            count_3 = dp[int(i/3)]
        if i % 2 == 0:
            count_2 = dp[int(i/2)]
        if i - 1 >= 0:
            count_1 = dp[i-1]
        
        dp.append(min(count_3+1, count_2+1, count_1+1))
        
        if count_3 <= min(count_2, count_1):
            array.append(int(i/3))
        elif count_2 <= min(count_3, count_1):
            array.append(int(i/2))
        elif count_1 <= min(count_3, count_2):
            array.append(i-1)
#     print(dp)
#     print(array)
    array_2 = [n]
#     print(array_2)
    for i in range(dp[n]):
#         print(array[n])
        array_2.append(array[n])
        n = array[n]
    array_2.reverse()
    
    return array_2

input = sys.stdin.read()
n = int(input)
sequence = dp_approach(n)
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
