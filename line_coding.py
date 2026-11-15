NRZ_L_MAP = {"0": 1, "1": -1}
MANCHESTER_MAP = {"0": [1, -1], "1": [-1, 1]}


def nrz_l(bits):        # zero -> hero , one -> zero 
    return [NRZ_L_MAP[b] for b in bits]


def nrz_i(bits):        # prev 0 -> no inversion
    signal = []
    level = 1

    for bit in bits:
        if bit == "1":
            level = -level
        signal.append(level)

    return signal


def manchester(bits):   # Z formation 
    signal = []

    for bit in bits:
        signal.extend(MANCHESTER_MAP[bit])

    return signal


def differential_manchester(bits):  # at bit = 0 transition in next Z otherwise folowup 
    signal = []
    level = 1

    for bit in bits:
        if bit == "0":
            level = -level

        signal.append(level)
        level = -level
        signal.append(level)

    return signal


def ami(bits):  # be on 0 at 0 and if 1 alternate the position 
    signal = []
    level = -1

    for bit in bits:
        if bit == "1":
            level = -level
            signal.append(level)
        else:
            signal.append(0)

    return signal
