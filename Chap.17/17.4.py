def nth_sevenish_number(n):
    answer, bit_place = 0, 0
    while n > 0:
        if n & 1 == 1:
            answer += 7 ** bit_place
        n >>= 1
        bit_place += 1
    return answer

# n = 1
# print(nth_sevenish_number(n))

for n in range(1, 10):
    print(nth_sevenish_number(n))
