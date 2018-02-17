# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    eff = sorted([(w,v) for w,v in zip(weights,values)], key = lambda t:t[1]/t[0], reverse = True)
    for item in eff:
        if capacity == 0:
            return value
        elif capacity >= item[0]:
            value += item[1]
            capacity -= item[0]
        else:
            value += capacity * item[1] / item[0]
            capacity = 0
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
