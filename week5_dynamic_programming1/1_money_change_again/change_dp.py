# Uses python3
import sys

def min_coin_change(value):
    list_coin = [1,3,4]
    min_coins = [0]*(value+1) ## Create value range
    for coin in range(value+1):
        count = coin
        for i in [c for c in list_coin if c <= coin]:
            if min_coins[coin - i] + 1 < count:
                count = min_coins[coin - i] + 1
        min_coins[coin] = count
    return min_coins[value]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(min_coin_change(m))
