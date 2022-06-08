import sys

n, k = [int(x) for x in input().split()]

Cost = [int(x) for x in input().split()]

first_idx = (n - k -1) % (2*k + 1)

result = None
sol_idx = None

for i in range(first_idx, k+1):
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

print(result)

# check if there are arguments
if len(sys.argv) > 1:
    print(list(range(sol_idx, n, 2*k+1)))