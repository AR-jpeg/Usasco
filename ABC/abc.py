ints = list(map(int, input().split()))
sortedInts = sorted(ints)

A = sortedInts[0]
B = sortedInts[1]
ABC = sortedInts[-1]

C = ABC - (B+A)

print(A, B, C)