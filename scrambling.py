B8ZS_SUBSTITUTIONS = {
    1: [0, 0, 0, 1, -1, 0, -1, 1],   # if last is +ve ->  0 0 0 +ve -ve 0 -ve +ve
    -1: [0, 0, 0, -1, 1, 0, 1, -1],  # if last is -ve ->  0 0 0 -ve +ve 0 +ve -ve
}

HDB3_SUBSTITUTIONS = {
    (0, 1): [-1, 0, 0, -1],     # even & +ve ---> voov
    (0, -1): [1, 0, 0, 1],      # even & -ve ---> boob
    (1, 1): [0, 0, 0, 1],       # odd  & +ve ---> oooB
    (1, -1): [0, 0, 0, -1],     # odd  & -ve ---> oooV
}


def b8zs(bits):
    signal = []
    last_pulse = -1
    i = 0
    n = len(bits)

    while i < n:
        if bits.startswith("00000000", i):      # if 8 zeroes then take pattern according to last pulse 
            pattern = B8ZS_SUBSTITUTIONS[last_pulse]         # append pattern 
            signal.extend(pattern)      
            last_pulse = pattern[-1]                    # last pulse will be last bit of current pattern
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