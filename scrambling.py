def b8zs(bits):
    signal = []
    last_pulse = -1
    i = 0

    while i < len(bits):
        if bits[i:i + 8] == "00000000":
            if last_pulse == 1:
                pattern = [0, 0, 0, 1, -1, 0, -1, 1]
            else:
                pattern = [0, 0, 0, -1, 1, 0, 1, -1]

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

    while i < len(bits):
        if bits[i:i + 4] == "0000":

            if pulse_count % 2 == 0:
                # Even number of nonzero pulses: B00V
                b_pulse = -last_pulse
                pattern = [b_pulse, 0, 0, b_pulse]
                last_pulse = b_pulse

            else:
                # Odd number of nonzero pulses: 000V
                v_pulse = last_pulse
                pattern = [0, 0, 0, v_pulse]

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