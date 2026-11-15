import math
from data_generator import gen_rand_bits, gen_bits_with_zeros, longest_palindrome
from line_coding import nrz_l, nrz_i, manchester, differential_manchester, ami
from scrambling import b8zs, hdb3
from line_coding_decoders import (
    decode_nrz_l,
    decode_nrz_i,
    decode_manchester,
    decode_differential_manchester,
    decode_ami,
)
from descrambling import decode_b8zs, decode_hdb3
from delta_modulation import dm_encoder
from plot_signals import plot_digital_signal, plot_delta_modulation


def get_digital_bits():
    print("\n1. Enter bits\n2. Random bits\n3. Random with 4 zeros\n4. Random with 8 zeros")
    sources = {
        "1": lambda: input("Enter bits: ").strip(),
        "2": lambda: gen_rand_bits(20),
        "3": lambda: gen_bits_with_zeros(20, 4),
        "4": lambda: gen_bits_with_zeros(20, 8),
    }
    return sources.get(input("Choice: ").strip(), sources["2"])()


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid number. Try again.")


def get_sine_samples():
    amp = get_float_input("Amplitude: ")
    return [round(amp * math.sin(2 * math.pi * i / 20), 2) for i in range(20)]


def get_custom_samples():
    while True:
        raw = input("Enter samples separated by spaces: ").strip()
        if not raw:
            print("Cannot be empty. Try again.")
            continue
        try:
            return [float(x) for x in raw.split()]
        except ValueError:
            print("Invalid numbers. Try again.")


def get_analog_bits():
    print("\n1. Sine wave\n2. Type my own samples")
    sources = {"1": get_sine_samples, "2": get_custom_samples}
    samples = sources.get(input("Choice: ").strip(), sources["1"])()
    delta = get_float_input("Delta step size: ")
    dm_bits, reconstructed = dm_encoder(samples, delta)
    plot_delta_modulation(samples, reconstructed)
    return "".join(str(b) for b in dm_bits)


def main():
    print("1. Digital Input\n2. Analog Input")
    inputs = {"1": get_digital_bits, "2": get_analog_bits}
    bits = inputs.get(input("Choice: ").strip(), get_digital_bits)()

    print("\nBits:", bits)
    print("Longest Palindrome:", longest_palindrome(bits))

    schemes = {
        "1": ("NRZ-L", nrz_l, decode_nrz_l),
        "2": ("NRZ-I", nrz_i, decode_nrz_i),
        "3": ("Manchester", manchester, decode_manchester),
        "4": ("Differential Manchester", differential_manchester, decode_differential_manchester),
        "5": ("AMI", ami, decode_ami),
    }

    print("\nLine Coding:")
    for k in sorted(schemes):
        print(f"{k}. {schemes[k][0]}")

    name, encoder, decoder = schemes.get(input("Choice: ").strip(), schemes["1"])

    if name == "AMI":
        scramblers = {
            "1": ("B8ZS", b8zs, decode_b8zs),
            "2": ("HDB3", hdb3, decode_hdb3),
        }
        if input("Scrambling? (y/n): ").strip().lower() in ("y", "yes"):
            print("1. B8ZS\n2. HDB3")
            s_name, s_enc, s_dec = scramblers.get(input("Choice: ").strip(), scramblers["1"])
            signals = [ami(bits), s_enc(bits)]
            names = ["AMI", s_name]
            decoder = s_dec
        else:
            signals = [ami(bits)]
            names = ["AMI"]
    else:
        signals = [encoder(bits)]
        names = [name]

    plot_digital_signal(bits, signals, names)

    while True:
        ans = input("\nDecode the signal? (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            decoded = decoder(signals[-1])
            print("Decoded bits:", decoded)
            print("Match with original:", decoded == bits)
            break
        if ans in ("n", "no"):
            break
        print("Invalid choice. Enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
