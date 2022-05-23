# Uses python3
import sys

def optimal_summands(n):
    W = n
    prizes = []
    if (n<1)|(n>10**9):
        return n
    if (n==1):
        return [1]
    for i in range(1, n):
        if W>2*i:
            prizes.append(i)
            W -= i
        else:
            prizes.append(W)
            break
    return prizes

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
