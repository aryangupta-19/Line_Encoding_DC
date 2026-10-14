def nrz_l(bits):
    signal = []
    
    for bit in bits:        # convert binary -> signal level { 0 -> +1 and 1 -> =1 }
        if bit == "0":
            signal.append(1)
        else:
            signal.append(-1)
    return signal