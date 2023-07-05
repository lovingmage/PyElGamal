# PyElGamal

PyElGamal is a Python package that provides implementations of the ElGamal encryption scheme using the secp256r1 elliptic curve group and the RFC 3526 group.

**Notes:** This package is currently under development and is not ready for production use. It is intended for research and educational purposes only.


## Features

- Elliptic Curve ElGamal encryption implementation
- Support for the secp256r1 elliptic curve group and the RFC 3526 group
- Key generation, encryption, decryption, and homomorphic addition of ciphertexts

## Installation

You can install PyElGamal by cloning the GitHub repository and running the installation using `setup.py`:

1. Clone the GitHub repository:
   ```bash
   git clone https://github.com/your-username/PyElGamal.git
    ```
2. Navigate to the PyElGamal directory:
    ```bash
    cd PyElgamal
    ```
3. Install the package and its dependencies using setup.py:

    ```bash
    python setup.py install
    ```

## Usage

Here's an example of how to use PyElGamal:
```python
from py_elgamal.ec_elgamal import generate_keys, ec_elgamal_encrypt, ecc_elgamal_decrypt, ecc_elgamal_add

# Generate keys
g, x, h = generate_keys()

# Encrypt a message
m = 42
ciphertext = ec_elgamal_encrypt(g, h, m)

# Decrypt the ciphertext
decrypted_m = ecc_elgamal_decrypt(ciphertext[0], ciphertext[1], x)

# Homomorphically add ciphertexts
c1 = ec_elgamal_encrypt(g, h, 10)
c2 = ec_elgamal_encrypt(g, h, 20)
sum_ciphertext = ecc_elgamal_add(c1, c2)

print(f"Original message: {m}")
print(f"Decrypted message: {decrypted_m}")
print(f"Sum of ciphertexts: {sum_ciphertext}")
```
