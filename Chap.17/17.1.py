def find_unique(S):
    arr = [0] * 32
    for num in S:
        for i in range(32):
            bit = (num >> i) & 1
            arr[i] += bit
    result = 0
    for i, bit in enumerate(arr):
        if bit % 3 != 0:
            result += 2 ** i
    return result

S = list(map(int, input().split()))
print(find_unique(S))
