# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    proportion = [float(v) / float(w) for v, w in zip(values, weights)]

    a = list(range(0,len(weights)+1))
    for _ in range(0,len(weights)+1):
        if (capacity == 0)|(capacity<0)|(capacity>100):
            return value
            break
        max_w = max(proportion)
        index = proportion.index(max(proportion))
        proportion[index] = -1 # for each iteration, remove the max item 
        
        print(index)
        
        current = min(weights[index], capacity)
        value += current * max_w
        weights[index] = weights[index] - current
        capacity = capacity - current
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
