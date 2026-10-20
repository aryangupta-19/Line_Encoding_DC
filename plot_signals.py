import matplotlib.pyplot as plt


def plot_digital_signal(bits, signals, names):
    fig, axes = plt.subplots(len(signals), 1, figsize=(12, 10))

    if len(signals) == 1:
        axes = [axes]

    for i in range(len(signals)):
        signal = signals[i]

        if len(signal) == 0:
            continue

        if len(signal) == 2 * len(bits):
            samples_per_bit = 2
        else:
            samples_per_bit = 1

        time = []

        for j in range(len(signal) + 1):
            time.append(j / samples_per_bit)

        values = list(signal)
        values.append(signal[-1])

        axes[i].step(time, values, where="post")
        axes[i].set_title(names[i])
        axes[i].set_ylabel("Voltage")
        axes[i].set_xlabel("Bit Period")
        axes[i].set_xlim(0, len(bits))
        axes[i].grid(True)

    plt.tight_layout()
    plt.show()


def plot_delta_modulation(samples, reconstructed):
    time = list(range(len(samples)))

    plt.figure(figsize=(10, 5))

    plt.plot(
        time,
        samples,
        marker="o",
        label="Original Analog Signal"
    )

    plt.step(
        time,
        reconstructed,
        where="mid",
        label="Reconstructed Signal"
    )

    plt.title("Delta Modulation")
    plt.xlabel("Sample Number")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()