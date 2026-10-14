from data_generator import (
    gen_rand_bits,
    gen_bits_with_zeros,
    longest_palindrome
)


def main():
    length = 20

    bits = gen_rand_bits(length)
    print("Random Binary Sequence:", bits)
    print("Longest Palindrome:", longest_palindrome(bits))

    bits_with_zeros = gen_bits_with_zeros(length, 4)
    print("\nSequence with 4 Consecutive Zeros:", bits_with_zeros)
    print("Longest Palindrome:", longest_palindrome(bits_with_zeros))


if __name__ == "__main__":
    main()