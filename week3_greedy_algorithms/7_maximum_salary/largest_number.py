#Uses python3

import sys

def IsGreaterOrEqual(digit, max_digit):
    return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))

def largest_number(lst):
    answer = []
    
    while lst!=[]:
        max_digit = 0
        for digit in lst:
            if IsGreaterOrEqual(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        lst.remove(max_digit)

    return int(''.join([str(i) for i in answer]))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
