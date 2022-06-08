from main import beautifulZeros 

test1 = [3,1,[1,1,1]]
test2 = [14, 2,[1,2,2,2,2,2,2,2,2,2,2,2,2,2]]
test3 = [3,1,[1,2,1]]
test4 = [13, 4, [88, 123, 132, 39, 180, 30, 188, 131, 165, 155, 71, 31, 22]]
test5 = [10, 2, [19, 5, 4, 2, 10, 12, 8, 17, 17, 15]]
test6 = [7,2,[1,2,3,4,5,6,7]]
test7 = [3,4,[1,1,1]]
test8 = [41, 10, [2, 0, 2, 1, 0, 2, 2, 2, 2, 1, 0, 0, 0, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 0, 1, 2, 0, 2, 1, 1, 1, 0, 0, 1, 1, 0, 1, 2, 1, 1, 0]]
test9 = [46, 5, [8, 5, 6, 0, 20, 19, 8, 8, 10, 10, 14, 6, 10, 4, 7, 1, 8, 20, 20, 16, 1, 
16, 19, 1, 15, 1, 5, 12, 15, 11, 13, 12, 11, 18, 2, 19, 2, 5, 13, 14, 15, 12, 15, 6, 16, 9]]
test10 = [90, 16, [46, 110, 37, 186, 121, 140, 124, 22, 81, 135, 11, 193, 68, 
43, 167, 190, 157, 62, 187, 157, 161, 193, 44, 142, 121, 1, 175, 16, 117, 144, 
103, 174, 114, 66, 191, 117, 65, 143, 160, 72, 2, 158, 149, 99, 161, 191, 187, 
106, 129, 11, 144, 194, 78, 199, 182, 183, 115, 59, 83, 55, 6, 136, 11, 198, 
198, 108, 102, 163, 79, 6, 48, 8, 60, 143, 11, 157, 84, 129, 14, 103, 162, 94, 
158, 141, 106, 109, 175, 190, 35, 189]]

testArray = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10]
i = 1
for test in testArray:
    n,k,cost = test
    result, sol_idx = beautifulZeros(n,k,cost)
    print(f"Test{i} => min cost: {result}, solution: {list(range(sol_idx, n, 2*k+1))}")
    i = i + 1


