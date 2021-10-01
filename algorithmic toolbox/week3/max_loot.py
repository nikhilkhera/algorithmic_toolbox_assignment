# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    V=0
    W=capacity
    vpu=[]
    for i in range(len(weights)):
        vpu.append(values[i]/weights[i])
    for i in range(len(weights)):
        if W==0:
            return V
        i=vpu.index(max(vpu))
        a=min(W,weights[i])
        W=W-a
        V=V+(values[i]*a)/weights[i]
        vpu.pop(i)
        weights.pop(i)
        values.pop(i)

    return V


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
