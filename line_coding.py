NRZ_L_MAP = {"0": 1, "1": -1}
MANCHESTER_MAP = {"0": [1, -1], "1": [-1, 1]}


def nrz_l(bits):
    return [NRZ_L_MAP[b] for b in bits]


def nrz_i(bits):
    signal = []
    level = 1

    for bit in bits:
        if bit == "1":
            level = -level
        signal.append(level)

    return signal


def manchester(bits):
    signal = []

    for bit in bits:
        signal.extend(MANCHESTER_MAP[bit])

    return signal


def differential_manchester(bits):
    signal = []
    level = 1

    for bit in bits:
        if bit == "0":
            level = -level

        signal.append(level)
        level = -level
        signal.append(level)

    return signal


def ami(bits):
    signal = []
    level = -1

    for bit in bits:
        if bit == "1":
            level = -level
            signal.append(level)
        else:
            signal.append(0)

    return signal
