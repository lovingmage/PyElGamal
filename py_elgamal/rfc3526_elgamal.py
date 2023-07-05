"""
Author: Chenghong Wang
Email: cw374@duke.edu

This script implements the ElGamal encryption scheme using a 2048-bit prime modulus and generator defined in RFC 3526.
It provides functions for key generation, encryption, decryption, exponent encryption, exponent decryption, and homomorphic aggregation.

The script contains the following functions:

- generate_keypair: Generates a private key and corresponding public key using the RFC 3526 group parameters.
- encrypt: Encrypts a plaintext message using the public key.
- decrypt: Decrypts a ciphertext using the private key.
- encrypt_exponent: Encrypts an exponent using the public key.
- decrypt_exponent: Decrypts a ciphertext representing an exponent and recovers the original exponent.
- aggregate: Performs homomorphic aggregation of two ciphertexts.

Note: This implementation uses the gmpy2 library for efficient arbitrary-precision arithmetic.

This code is for educational and research purposes only. No warranty is provided or implied.

Always remember to use established, tested, and secure libraries for cryptographic applications in a production environment.
"""


import gmpy2
from gmpy2 import mpz

# Global group parameters
p = mpz("FFFFFFFF FFFFFFFF C90FDAA2 2168C234 C4C6628B 80DC1CD1"
         "29024E08 8A67CC74 020BBEA6 3B139B22 514A0879 8E3404DD"
         "EF9519B3 CD3A431B 302B0A6D F25F1437 4FE1356D 6D51C245"
         "E485B576 625E7EC6 F44C42E9 A637ED6B 0BFF5CB6 F406B7ED"
         "EE386BFB 5A899FA5 AE9F2411 7C4B1FE6 49286651 ECE45B3D"
         "C2007CB8 A163BF05 98DA4836 1C55D39A 69163FA8 FD24CF5F"
         "83655D23 DCA3AD96 1C62F356 208552BB 9ED52907 7096966D"
         "670C354E 4ABC9804 F1746C08 CA237327 FFFFFFFF FFFFFFFF",16)
g = mpz(2)  # Generator

def generate_keypair():
    # Generate a random value x as the private key
    x = gmpy2.mpz_random(gmpy2.random_state(), p-1) + 1

    # Calculate public key y
    y = gmpy2.powmod(g, x, p)
    
    return x, y

def encrypt(y, plaintext):
    # Generate a random value k
    k = gmpy2.mpz_random(gmpy2.random_state(), p-1) + 1

    # Calculate the shared secret S
    S = gmpy2.powmod(y, k, p)

    # Calculate the ciphertext (c1, c2)
    c1 = gmpy2.powmod(g, k, p)
    c2 = gmpy2.mul(plaintext, S) % p
    
    return [c1, c2]

def decrypt(x, c):
    # c1: ciphertext component 1
    # c2: ciphertext component 2
    c1 = c[0]
    c2 = c[1]

    # Calculate the shared secret S
    S = gmpy2.powmod(c1, x, p)

    # Calculate the inverse of S
    S_inverse = gmpy2.invert(S, p)

    # Calculate the plaintext
    plaintext = gmpy2.mul(c2, S_inverse) % p
    
    return plaintext

def encrypt_exponent(y, m):
    # Encrypt the message as g^m
    c1, c2 = encrypt(y, gmpy2.powmod(g, m, p))
    
    return [c1, c2]

def decrypt_exponent(x, c):
    # Decrypt the ciphertext
    decrypted_ciphertext = decrypt(x, c)

    # Compute the discrete logarithm to recover the exponent x
    recovered_exponent = gmpy2.mpz(gmpy2.log2(decrypted_ciphertext))

    return recovered_exponent

def aggregate(c1, c2):

    return [gmpy2.mul(c1[0], c2[0]), gmpy2.mul(c1[1], c2[1])]

