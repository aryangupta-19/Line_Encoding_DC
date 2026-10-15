def nrz_l(bits):
    signal = []
    
    for bit in bits:        # convert binary -> signal level { 0 -> +1 and 1 -> =1 }  (zero -> hero and one -> zero)
        if bit == "0":
            signal.append(1)
        if bit == "1":
            signal.append(-1)
    return signal

def nrz_i(bits):        # Transition on 1 and no transition on zero (transition -> reflection in x-axis)
    signal = []
    level = 1

    for bit in bits:        
        if bit == "1":
            level = -level  # 1 -> level= -1 and 0 -> level = 1

        signal.append(level)

    return signal

def manchester(bits):   # manchester -> 1 == -ve to +ve z and 0 == +ve to -ve z
    signal = []

    for bit in bits:
        if bit == "0":
            signal.extend([1, -1])
        if bit == "1":
            signal.extend([-1, 1])

    return signal

def differential_manchester(bits):  # hrr bit ke middle mai transition necessary hai and one mai continue as it is and zero mai invert and then continue 
    signal = []
    level = 1

    for bit in bits:
        if bit == "0":  # zero pr invert krke append kro 
            level = -level

        signal.append(level)
        level = -level
        signal.append(level)

    return signal

def ami(bits):      # (First simple 0 -> on ref line and 1 -> alternates)  now how alternates on 1 -> see first one -> above then alternate on one 
    signal = []
    level = -1      # initally taken below 

    for bit in bits:
        if bit == "1":      # if bit is 1 then it will negate it and mark 
            level = -level  # alternates at each 1 but for initial 1 always above that's why initalized with -1 and negated before appending 
            signal.append(level)
        if bit == "0":      # at zero always be on ref line 
            signal.append(0)

    return signal

