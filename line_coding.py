def nrz_l(bits):
    signal = []
    
    for bit in bits:        # convert binary -> signal level { 0 -> +1 and 1 -> =1 }
        if bit == "0":
            signal.append(1)
        if bit == "1":
            signal.append(-1)
    return signal

def nrz_i(bits):
    signal = []
    level = 1

    for bit in bits:        
        if bit == "1":
            level = -level  # 1 -> level= -1 and 0 -> level = 1

        signal.append(level)

    return signal