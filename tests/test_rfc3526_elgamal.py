import unittest
from py_elgamal.rfc3526_elgamal import generate_keypair, encrypt, decrypt, encrypt_exponent, decrypt_exponent, aggregate

class TestRFC3526ElGamal(unittest.TestCase):
    def test_generate_keypair(self):
        for _ in range(100):
            x, y = generate_keypair()
            self.assertIsNotNone(x)
            self.assertIsNotNone(y)

    def test_encrypt_decrypt(self):
        for _ in range(100):
            x, y = generate_keypair()
            plaintext = 42
            ciphertext = encrypt(y, plaintext)
            decrypted_plaintext = decrypt(x, ciphertext)
            self.assertEqual(plaintext, decrypted_plaintext)

    def test_encrypt_decrypt_exponent(self):
        for _ in range(100):
            x, y = generate_keypair()
            exponent = 42
            ciphertext = encrypt_exponent(y, exponent)
            recovered_exponent = decrypt_exponent(x, ciphertext)
            self.assertEqual(exponent, recovered_exponent)

    def test_aggregate(self):
        for _ in range(100):
            x1, y1 = generate_keypair()
            x2, y2 = generate_keypair()
            c1 = encrypt_exponent(y1, 10)
            c2 = encrypt_exponent(y2, 20)
            aggregated_ciphertext = aggregate(c1, c2)
            self.assertIsNotNone(aggregated_ciphertext)

if __name__ == '__main__':
    unittest.main()
