"""
Author: Chenghong Wang
Email: cw374@duke.edu

Copyright 2023 Chenghong Wang

This script implements the Elliptic Curve ElGamal Cryptosystem using the secp256r1 curve. 
It allows for the generation of private and public keys, encryption and decryption of messages, 
and homomorphic addition of ciphertexts.

The script contains the following functions:

- generate_keys: Generates a private key and a corresponding public key.
- ec_elgamal_encrypt: Encrypts a message with the public key.
- ecc_elgamal_decrypt: Decrypts a ciphertext with the private key.
- ecc_elgamal_add: Homomorphically adds two ciphertexts together.
- msg_to_point: Converts a message to a point on the elliptic curve.
- test_ec_elgamal: Tests the above functions with randomly generated messages.

This code is for educational and research purposes only. No warranty is provided or implied.

Always remember to use established, tested, and secure libraries for cryptographic applications in a production environment.
"""


import rubenesque.curves

secp256r1 = rubenesque.curves.find('secp256r1')

from .utils import *

def generate_keys():
    g, = get_generators(1)

    # Generate a private key
    x = get_random_value()

    # Generate the corresponding public key h=g^x
    h = g * x

    return g, x, h

def ec_elgamal_encrypt(g, h, m):

    #choose encryption randomness
    r = get_random_value()

    # ciphertext = (g^r, m*h^r)
    return [g * r, m + h*r]

def ecc_elgamal_decrypt(c1, c2, x):

    # decryption cipher c=[c1, c2]
    return c2 - c1 * x

def ecc_elgamal_add(ctx_l, ctx_r):

    return [ctx_l[0]+ctx_r[0], ctx_l[1]+ctx_r[1]]

def msg_to_point(g, m):
    return g * m

