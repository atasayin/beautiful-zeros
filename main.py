
n, k = [int(x) for x in input().split()]

Cost = [int(x) for x in input().split()]

first_idx = (n - k -1) % (2*k + 1)

result = None

for i in range(first_idx, k+1):
    cost_i = 0
    for j in range(i, n, 2*k+1):
        cost_i = cost_i + Cost[j]
    if result is None:
        result = cost_i
    else:
        result = min(result, cost_i) 

print(result)