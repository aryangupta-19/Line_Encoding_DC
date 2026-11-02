B8ZS_PATTERNS = {
    (0, 0, 0, 1, -1, 0, -1, 1): "00000000",
    (0, 0, 0, -1, 1, 0, 1, -1): "00000000",
}

HDB3_PATTERNS = {
    (1, 0, 0, 1): "0000",
    (-1, 0, 0, -1): "0000",
    (0, 0, 0, 1): "0000",
    (0, 0, 0, -1): "0000",
}


def decode_b8zs(signal):
    bits = []
    i = 0
    n = len(signal)

    while i < n:
        chunk = tuple(signal[i : i + 8])
        if chunk in B8ZS_PATTERNS:
            bits.append(B8ZS_PATTERNS[chunk])
            i += 8
        else:
            bits.append("0" if signal[i] == 0 else "1")
            i += 1

    return "".join(bits)


def decode_hdb3(signal):
    bits = []
    i = 0
    n = len(signal)

    while i < n:
        chunk = tuple(signal[i : i + 4])
        if chunk in HDB3_PATTERNS:
            bits.append(HDB3_PATTERNS[chunk])
            i += 4
        else:
            bits.append("0" if signal[i] == 0 else "1")
            i += 1

    return "".join(bits)