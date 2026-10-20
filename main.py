from data_generator import (
    gen_rand_bits,
    gen_bits_with_zeros,
    longest_palindrome
)

from line_coding import nrz_l, nrz_i, manchester, differential_manchester, ami
from scrambling import b8zs, hdb3
from line_coding_decoders import (
    decode_nrz_l,
    decode_nrz_i,
    decode_manchester,
    decode_differential_manchester,
    decode_ami
)
from descrambling import decode_b8zs, decode_hdb3
from delta_modulation import dm_encoder, dm_decoder

from plot_signals import plot_digital_signal, plot_delta_modulation
from delta_modulation import dm_encoder, dm_decoder

def main():
    length = 20

    bits = gen_rand_bits(length)
    print("\nRandom Binary Sequence:", bits)
    print("Longest Palindrome:", longest_palindrome(bits))

    bits_with_zeros = gen_bits_with_zeros(length, 4)
    print("\nSequence with 4 Consecutive Zeros:", bits_with_zeros)
    print("Longest Palindrome:", longest_palindrome(bits_with_zeros))


    print("\nNRZ-L Encoded Signal:", nrz_l(bits))
    print("NRZ-I Encoded Signal:", nrz_i(bits))
    
    print("Manchester Encoded Signal:", manchester(bits))
    print("Differential_Manchester Encoded Signal:", differential_manchester(bits))
    
    print("AMI Encoded Signal:", ami(bits))
    
    
    test_bits = "110000000010"
    print("Input Bits:", test_bits)
    print("B8ZS Signal:", b8zs(test_bits))
    
    tests = [
        "1",
        "0000",
        "10000",
        "100000000",
        "110000",
        "100000000000",
    ]

    for bits in tests:
        print("Input:", bits)
        print("HDB3:", hdb3(bits))
        print()
        
        bits = "10110010"

    print("\nOriginal Bits:", bits)
    print("NRZ-L Decoded:", decode_nrz_l(nrz_l(bits)))
    print("NRZ-I Decoded:", decode_nrz_i(nrz_i(bits)))
    print("Manchester Decoded:", decode_manchester(manchester(bits)))
    print("Differential Manchester Decoded:",
        decode_differential_manchester(differential_manchester(bits)))
    print("AMI Decoded:", decode_ami(ami(bits)))
    
        # B8ZS Descrambling Test

    original_bits = "110000000010"
    encoded_signal = b8zs(original_bits)
    decoded_bits = decode_b8zs(encoded_signal)

    print("\nB8ZS Original:", original_bits)
    print("B8ZS Encoded:", encoded_signal)
    print("B8ZS Decoded:", decoded_bits)
    print("B8ZS Correct:", original_bits == decoded_bits)


    # HDB3 Descrambling Test

    original_bits = "110000"
    encoded_signal = hdb3(original_bits)
    decoded_bits = decode_hdb3(encoded_signal)

    print("\nHDB3 Original:", original_bits)
    print("HDB3 Encoded:", encoded_signal)
    print("HDB3 Decoded:", decoded_bits)
    print("HDB3 Correct:", original_bits == decoded_bits)
    
    # HDB3 Descrambling Tests

    test_sequences = [
        "0000",
        "10000",
        "100000000",
        "110000",
        "100000000000",
        "110000000000"
    ]

    for original_bits in test_sequences:
        encoded_signal = hdb3(original_bits)
        decoded_bits = decode_hdb3(encoded_signal)

        print("Original:", original_bits)
        print("Encoded:", encoded_signal)
        print("Decoded:", decoded_bits)
        print("Correct:", original_bits == decoded_bits)
        print()
        
        # Delta Modulation Test

    samples = [0.5, 1.2, 2.0, 1.5, 0.5, -0.5, -1.5, -0.5, 0.8, 1.8]
    delta = 0.5

    dm_bits, reconstructed = dm_encoder(samples, delta)
    decoded_signal = dm_decoder(dm_bits, delta)

    print("\nOriginal Analog Samples:", samples)
    print("Delta Modulation Bits:", dm_bits)
    print("Encoder Reconstruction:", reconstructed)
    print("Decoder Reconstruction:", decoded_signal)

        
    # Digital Line Coding Waveforms

    bits = "10110010"

    signals = [
        nrz_l(bits),
        nrz_i(bits),
        manchester(bits),
        differential_manchester(bits),
        ami(bits)
    ]

    names = [
        "NRZ-L",
        "NRZ-I",
        "Manchester",
        "Differential Manchester",
        "AMI"
    ]

    plot_digital_signal(bits, signals, names)


    # Delta Modulation Waveform

    samples = [0.5, 1.2, 2.0, 1.5, 0.5, -0.5, -1.5, -0.5, 0.8, 1.8]
    delta = 0.5

    dm_bits, reconstructed = dm_encoder(samples, delta)

    decoded_signal = dm_decoder(dm_bits, delta)

    plot_delta_modulation(samples, decoded_signal)
    
    
if __name__ == "__main__":
    main()

