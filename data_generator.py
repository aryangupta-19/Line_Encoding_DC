import random


def gen_rand_bits(length):
    return "".join(random.choices(("0", "1"), k=length))


def gen_bits_with_zeros(length, z_cnt):
    if z_cnt not in (4, 8):
        raise ValueError("z_cnt must be 4 or 8")

    if length < z_cnt:
        raise ValueError("length must be >= z_cnt")

    bits = gen_rand_bits(length)
    z_seq = "0" * z_cnt
    pos = random.randint(0, length - z_cnt)

    return bits[:pos] + z_seq + bits[pos + z_cnt:]


def longest_palindrome(bits):
    if not bits:
        return ""

    transformed = "^#" + "#".join(bits) + "#$"
    n = len(transformed)
    p = [0] * n
    center = right = 0
    max_len = 0
    center_idx = 0

    for i in range(1, n - 1):
        i_mirror = 2 * center - i
        if right > i:
            p[i] = min(right - i, p[i_mirror])

        while transformed[i + 1 + p[i]] == transformed[i - 1 - p[i]]:
            p[i] += 1

        if i + p[i] > right:
            center = i
            right = i + p[i]

        if p[i] > max_len:
            max_len = p[i]
            center_idx = i

    start = (center_idx - max_len) // 2
    return bits[start : start + max_len]