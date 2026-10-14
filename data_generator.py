import random


def gen_rand_bits(length):
    bits = ""

    for _ in range(length):
        bits += str(random.randint(0, 1))

    return bits


def gen_bits_with_zeros(length, z_cnt):
    if z_cnt not in (4, 8):
        raise ValueError("z_cnt must be 4 or 8")

    if length < z_cnt:
        raise ValueError("length must be >= z_cnt")

    bits = gen_rand_bits(length)

    z_seq = "0" * z_cnt
    pos = random.randint(0, length - z_cnt)

    bits = bits[:pos] + z_seq + bits[pos + z_cnt:]

    return bits


def longest_palindrome(bits):
    longest = ""

    for i in range(len(bits)):
        for j in range(i + 1, len(bits) + 1):
            substring = bits[i:j]

            if substring == substring[::-1]:
                if len(substring) > len(longest):
                    longest = substring

    return longest