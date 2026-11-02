B8ZS_PATTERNS = {
    (0, 0, 0, 1, -1, 0, -1, 1): "00000000",
    (0, 0, 0, -1, 1, 0, 1, -1): "00000000",
}

HDB3_BOOV = {
    (1, 0, 0, 1): "0000",
    (-1, 0, 0, -1): "0000",
}

HDB3_OOOV = {
    (0, 0, 0, 1): 1,
    (0, 0, 0, -1): -1,
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
    last_pulse = -1
    i = 0
    n = len(signal)

    while i < n:
        chunk = tuple(signal[i : i + 4])
        if chunk in HDB3_BOOV:
            bits.append("0000")
            last_pulse = chunk[-1]
            i += 4
        elif HDB3_OOOV.get(chunk) == last_pulse:
            bits.append("0000")
            last_pulse = chunk[-1]
            i += 4
        elif signal[i] == 0:
            bits.append("0")
            i += 1
        else:
            bits.append("1")
            last_pulse = signal[i]
            i += 1

    return "".join(bits)