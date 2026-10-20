def decode_b8zs(signal):
    bits = ""
    i = 0

    while i < len(signal):

        if signal[i:i + 3] == [0, 0, 0]:
            pattern = signal[i:i + 8]

            if pattern == [0, 0, 0, 1, -1, 0, -1, 1]:
                bits += "00000000"
                i += 8

            elif pattern == [0, 0, 0, -1, 1, 0, 1, -1]:
                bits += "00000000"
                i += 8

            else:
                bits += "0"
                i += 1

        elif signal[i] == 0:
            bits += "0"
            i += 1

        else:
            bits += "1"
            i += 1

    return bits


def decode_hdb3(signal):
    bits = ""
    i = 0

    while i < len(signal):

        pattern = signal[i:i + 4]

        if pattern == [1, 0, 0, 1] or pattern == [-1, 0, 0, -1]:
            bits += "0000"
            i += 4

        elif signal[i:i + 4] == [0, 0, 0, 1] or signal[i:i + 4] == [0, 0, 0, -1]:
            bits += "0000"
            i += 4

        elif signal[i] == 0:
            bits += "0"
            i += 1

        else:
            bits += "1"
            i += 1

    return bits