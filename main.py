from data_generator import (
    gen_rand_bits,
    gen_bits_with_zeros,
    longest_palindrome
)

from line_coding import nrz_l
from line_coding import nrz_l, nrz_i
from line_coding import nrz_l, nrz_i, manchester, differential_manchester
from line_coding import nrz_l, nrz_i, manchester, differential_manchester, ami

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

if __name__ == "__main__":
    main()

