from data_generator import (
    gen_rand_bits,
    gen_bits_with_zeros,
    longest_palindrome
)

from line_coding import nrz_l, nrz_i, manchester, differential_manchester, ami
from scrambling import b8zs, hdb3

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

if __name__ == "__main__":
    main()

