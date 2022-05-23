# Uses python3
import sys

def get_change(m):
    if (m <0)|(m>1000):
        return print("Wrong number")
    elif m == 0:
        return m
    else:
        coin_10 = m//10
        coin_5 = (m%10)//5
        coin_1 = (m%10%5)
        count = coin_10 + coin_5 + coin_1       
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
