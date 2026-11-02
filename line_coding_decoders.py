NRZ_L_DECODE = {1: "0", -1: "1"}
AMI_DECODE = {0: "0", 1: "1", -1: "1"}


def decode_nrz_l(signal):
    return "".join(NRZ_L_DECODE.get(level, "1") for level in signal)


def decode_nrz_i(signal):
    bits = []
    previous_level = 1

    for level in signal:
        bits.append("0" if level == previous_level else "1")
        previous_level = level

    return "".join(bits)


def decode_manchester(signal):
    bits = []

    for i in range(0, len(signal), 2):
        bits.append("0" if signal[i] == 1 else "1")

    return "".join(bits)


def decode_differential_manchester(signal):
    bits = []
    previous_level = 1

    for i in range(0, len(signal), 2):
        bits.append("1" if signal[i] == previous_level else "0")
        previous_level = signal[i + 1]

    return "".join(bits)


def decode_ami(signal):
    return "".join(AMI_DECODE.get(level, "1") for level in signal)