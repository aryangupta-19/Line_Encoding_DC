B8ZS_SUBSTITUTIONS = {
    1: [0, 0, 0, 1, -1, 0, -1, 1],
    -1: [0, 0, 0, -1, 1, 0, 1, -1],
}

HDB3_SUBSTITUTIONS = {
    (0, 1): [-1, 0, 0, -1],
    (0, -1): [1, 0, 0, 1],
    (1, 1): [0, 0, 0, 1],
    (1, -1): [0, 0, 0, -1],
}


def b8zs(bits):
    signal = []
    last_pulse = -1
    i = 0
    n = len(bits)

    while i < n:
        if bits.startswith("00000000", i):
            pattern = B8ZS_SUBSTITUTIONS[last_pulse]
            signal.extend(pattern)
            last_pulse = pattern[-1]
            i += 8
        elif bits[i] == "0":
            signal.append(0)
            i += 1
        else:
            last_pulse = -last_pulse
            signal.append(last_pulse)
            i += 1

    return signal


def hdb3(bits):
    signal = []
    last_pulse = -1
    pulse_count = 0
    i = 0
    n = len(bits)

    while i < n:
        if bits.startswith("0000", i):
            pattern = HDB3_SUBSTITUTIONS[(pulse_count % 2, last_pulse)]
            signal.extend(pattern)
            last_pulse = pattern[-1]
            pulse_count = 0
            i += 4
        elif bits[i] == "0":
            signal.append(0)
            i += 1
        else:
            last_pulse = -last_pulse
            signal.append(last_pulse)
            pulse_count += 1
            i += 1

    return signal