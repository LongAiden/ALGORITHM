# Uses python3
import sys

def fib_last_digit(n):
    if n == 1:
        return n
    else:
        f = list(range(0,n+1))
        f[0] = 0
        f[1] = 1
        for i in range(2,n+1):
            f[i] = f[i-1] + f[i-2]
            f[i] = f[i]%10
        return f[-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_last_digit(n))
