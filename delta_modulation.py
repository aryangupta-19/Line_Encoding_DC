def dm_encoder(samples, delta):
    bits = []
    reconstructed = []
    previous = 0

    for sample in samples:
        if sample >= previous:
            bits.append(1)
            previous += delta
        else:
            bits.append(0)
            previous -= delta

        reconstructed.append(previous)

    return bits, reconstructed


def dm_decoder(bits, delta):
    reconstructed = []
    previous = 0

    for bit in bits:
        if bit == 1:
            previous += delta
        else:
            previous -= delta

        reconstructed.append(previous)

    return reconstructed