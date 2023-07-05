"""
Author: Chenghong Wang
Email: cw374@duke.edu

Copyright 2023 Chenghong Wang

This script extends the functionality of the Elliptic Curve ElGamal Cryptosystem using the secp256r1 curve. 
It provides functions for performing vectorized operations on multiple messages, ciphertexts, and keys.

The script contains the following functions:

- vector_ec_elgamal_encrypt: Encrypts a vector of messages with the public key.
- vector_ecc_elgamal_decrypt: Decrypts a vector of ciphertexts with the private key.
- vector_ecc_elgamal_add: Homomorphically adds two vectors of ciphertexts together.

This code is for educational and research purposes only. No warranty is provided or implied.

Always remember to use established, tested, and secure libraries for cryptographic applications in a production environment.
"""

import rubenesque.curves
from .ec_elgamal import generate_keys, ec_elgamal_encrypt, ecc_elgamal_decrypt, ecc_elgamal_add, msg_to_point
from .utils import get_random_value, get_generators
import concurrent.futures


secp256r1 = rubenesque.curves.find('secp256r1')


def vector_ec_elgamal_encrypt(g, h, vector):
    return [ec_elgamal_encrypt(g, h, m) for m in vector]

    # -------- concurrent enc ------------- 
    #with concurrent.futures.ThreadPoolExecutor() as executor:
    #    futures = [executor.submit(ec_elgamal_encrypt, g, h, m) for m in vector]
    #return [f.result() for f in futures]

def vector_ecc_elgamal_decrypt(ciphertexts, x):
    return [ecc_elgamal_decrypt(c[0], c[1], x) for c in ciphertexts ]
    # -------- concurrent dec ------------- 
    #with concurrent.futures.ThreadPoolExecutor() as executor:
    #    futures = [executor.submit(ecc_elgamal_decrypt, c[0], c[1], x) for c in ciphertexts]
    #return [f.result() for f in futures]

def vector_ecc_elgamal_add(ciphertexts1, ciphertexts2):
    if len(ciphertexts1) != len(ciphertexts2):
        raise ValueError("Both ciphertext vectors must be of the same length")
    
    return [ecc_elgamal_add(c1, c2) for c1, c2 in zip(ciphertexts1, ciphertexts2)]

    # -------- concurrent add ------------- 
    #with concurrent.futures.ThreadPoolExecutor() as executor:
    #    futures = [executor.submit(ecc_elgamal_add, c1, c2) for c1, c2 in zip(ciphertexts1, ciphertexts2)]
    
    #return [f.result() for f in futures]
