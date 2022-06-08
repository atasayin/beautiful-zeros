import sys

def beautifulZeros(n, k, Cost):
    result = None
    sol_idx = None

    for i in range(0, k+1):
        if (n - i -1) % (2*k + 1) <= k:
            cost_i = 0
            for j in range(i, n, 2*k+1):
                cost_i = cost_i + Cost[j]
            if result is None:
                result = cost_i
                sol_idx = i
            else:
                result = min(result, cost_i)
                if result == cost_i:
                    sol_idx = i

    return result, sol_idx 

if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    Cost = [int(x) for x in input().split()]

    result, sol_idx = beautifulZeros(n, k, Cost)

    print(result)

    if len(sys.argv) > 1:
        print(list(range(sol_idx, n, 2*k+1)))