# Digital Signal Encoder and Decoder
ITT 036 - Programming Assignment 1, Autumn 2026  
Author: Aryan Gupta (2024BITE030)

## Overview
This program encodes digital and analog signals into standard line coding formats. It accepts digital bitstreams directly or digitizes analog inputs via Delta Modulation, computes the longest palindromic substring, and applies line coding with optional AMI scrambling (B8ZS or HDB3). All generated signal waveforms and staircase approximations are plotted using Matplotlib.

## Features
- Digital input: manual bit entry, random 20-bit generation, or random bits with 4 or 8 consecutive zeros.
- Longest palindromic substring detection on the input bitstream.
- Analog input: sine wave generation (user-defined amplitude) or custom space-separated samples, digitized via Delta Modulation with user-defined step size and staircase visualization.
- Line coding schemes: NRZ-L, NRZ-I, Manchester, Differential Manchester, and AMI.
- Scrambling: B8ZS and HDB3 available when AMI is selected.
- Graphical waveform plotting using Matplotlib (plots both AMI and scrambled signals when scrambling is chosen).

## Project Structure
```text
.
|-- main.py              Entry point and menu flow orchestration
|-- data_generator.py    Random bit generation and Manacher's algorithm
|-- delta_modulation.py  Delta modulation encoding and decoding
|-- line_coding.py       NRZ-L, NRZ-I, Manchester, Differential Manchester, AMI
|-- scrambling.py        B8ZS and HDB3 scrambling for AMI
|-- plot_signals.py      Matplotlib plotting for digital waveforms and DM
|-- requirements.txt     Third-party library dependencies
`-- README.md            Documentation and instructions
```

## Requirements
Python 3 and Matplotlib. Install dependencies using:
```bash
pip install -r requirements.txt
```

## How to Run
Run the program with:
```bash
python3 main.py
```
Menu flow:
1. Select input type: `1` for Digital Input or `2` for Analog Input.
2. Select data source: For digital, pick manual entry, random bits, or random bits with 4/8 zeros. For analog, pick sine wave (enter amplitude) or custom samples, then enter delta step size.
3. The program displays the bitstream and its longest palindromic substring (and displays the DM staircase plot if analog was chosen).
4. Select a line coding scheme (`1` to `5`).
5. If AMI (`5`) is chosen, choose whether to scramble (`y`/`n`), then pick B8ZS (`1`) or HDB3 (`2`).
6. Matplotlib displays the signal waveform plot.

## Example Session
```text
1. Digital Input
2. Analog Input
Choice: 1

1. Enter bits
2. Random bits
3. Random with 4 zeros
4. Random with 8 zeros
Choice: 1
Enter bits: 10110010

Bits: 10110010
Longest Palindrome: 0110

Line Coding:
1. NRZ-L
2. NRZ-I
3. Manchester
4. Differential Manchester
5. AMI
Choice: 3
```

## Assumptions
| Scheme / Component | Level for 0 | Level for 1 | Initial Level | Samples / Bit | Key Parameters |
| :--- | :--- | :--- | :--- | :---: | :--- |
| NRZ-L | +1 | -1 | N/A | 1 | Memoryless mapping |
| NRZ-I | No inversion | Invert | +1 | 1 | Inverts on bit 1 |
| Manchester | [1, -1] | [-1, 1] | N/A | 2 | High-to-low for 0, low-to-high for 1 |
| Diff. Manchester | Invert at start | No invert at start | +1 | 2 | Always inverts mid-bit |
| AMI | 0 | Alternating +1 / -1 | -1 | 1 | First 1 becomes +1 |
| B8ZS | N/A | N/A | -1 | 1 | Replaces 8 zeros with 000VB0VB |
| HDB3 | N/A | N/A | -1 | 1 | Pulse count starts at 0; 000V (odd), B00V (even) |
| Delta Modulation | Emits 0 | Emits 1 | 0 | 1 | Step size delta; rule is `sample >= previous` |

## Algorithms and Complexity
- Longest Palindrome: Manacher's algorithm operating in linear time O(n) and linear space O(n).
- Scrambling: B8ZS and HDB3 operate in a single linear forward pass in O(n) time and O(n) space.
- Menu Dispatch: Menu options are dispatched via dictionary lookup rather than chained if/elif statements.

## Not Implemented
- PCM (Pulse Code Modulation) is not implemented; Delta Modulation is used for analog conversion.
- Line coding decoders and descramblers (optional extra credit) are not implemented.

## AI Assistance
Claude (Anthropic) and Antigravity (AI coding assistant) were used for explanations, test cases and help implementing parts of the code. All code was checked and tested by the author.
