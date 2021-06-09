def find_length(n):
    maxlength = 0
    while n > 0:
        maxlength += 1
        n &= (n << 1)
    return maxlength

n = 156
print(find_length(n))
