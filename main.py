def checkpair(array, n, x):
    for i in range(n-1):
        for j in range(i+1,n):
            if array[i] + array[j] == x:
                print(f"the given pairs are {array[i]},{array[j]}")
    return 0

A = [0, -1, 2, -3, 1]
x = -2
n=len(A)

checkpair(A, n, x)

