# Uses python3
import sys

#def binary_search(a, x):
#    left, right = 0, len(a)
    # write your code here

#def linear_search(a, x):
#    for i in range(len(a)):
#        if a[i] == x:
#            return i
#    return -1

def binary_search(a, k):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (high+low)//2
        if a[mid] > k:
            high = mid - 1
        elif a[mid] < k:
            low = mid + 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
