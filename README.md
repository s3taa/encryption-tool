# Encryption Tool

A command-line encryption tool built in Python implementing two classical ciphers.
Built as a learning project while teaching myself Python fundamentals.

## Features
- Caesar cipher, encrypt and decrypt with a numeric shift key
- Vigenère cipher,  keyword-based polyalphabetic encryption
- Brute force cracker,  tries all 25 Caesar shifts to crack unknown ciphertext
- Colour terminal output with animated header
- Handles uppercase, lowercase, spaces and punctuation correctly

## How to run
```bash
python encryption_tool.py
```

## What it taught me
- How ASCII values work (ord/chr)
- Modulo arithmetic for wrap-around logic
- String iteration and accumulation
- ANSI terminal colour codes
- Why Caesar cipher is weak (only 25 possible keys — brute-forceable instantly)
- Why Vigenère is stronger (keyword cycling defeats frequency analysis)

## Background
Caesar cipher shifts every letter by a fixed number.
Vigenère uses a keyword where each letter becomes a different shift,
applied in rotation — meaning the same letter encrypts differently
depending on its position, defeating simple brute force.
