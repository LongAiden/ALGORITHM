# Uses python3
# def calc_fib(n):
#     if (n <= 1):
#         return n

#     return calc_fib(n - 1) + calc_fib(n - 2)

# n = int(input())
# print(calc_fib(n))

def fib(n):
    if (n == 1) or (n==0):
        return n
    else:
        f = list(range(0,n+1))
        f[0] = 0
        f[1] = 1
        for i in range(2,n+1):
            f[i] = f[i-1] + f[i-2]
        return f[-1]

n = int(input())
print(fib(n))