def decode_nrz_l(signal):
    bits = ""

    for level in signal:
        if level == 1:
            bits += "0"
        else:
            bits += "1"

    return bits


def decode_nrz_i(signal):
    bits = ""
    previous_level = 1

    for level in signal:
        if level == previous_level:
            bits += "0"
        else:
            bits += "1"

        previous_level = level

    return bits


def decode_manchester(signal):
    bits = ""

    for i in range(0, len(signal), 2):
        if signal[i] == 1:
            bits += "0"
        else:
            bits += "1"

    return bits


def decode_differential_manchester(signal):
    bits = ""
    previous_level = 1

    for i in range(0, len(signal), 2):
        if signal[i] == previous_level:
            bits += "1"
        else:
            bits += "0"

        previous_level = signal[i + 1]

    return bits


def decode_ami(signal):
    bits = ""

    for level in signal:
        if level == 0:
            bits += "0"
        else:
            bits += "1"

    return bits