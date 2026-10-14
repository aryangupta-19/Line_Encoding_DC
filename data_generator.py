import random


def gen_rand_bits(len):
    bits = ""
    
    for _ in range(len):
        bits += str(random.randint(0, 1))

    return bits


def gen_bits_with_zeros(len, z_cnt):
    bits = gen_rand_bits(len)

    z_seq = "0" * z_cnt

    pos = random.randint(0, len - z_cnt)

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