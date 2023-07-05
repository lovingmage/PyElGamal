import unittest
from py_elgamal.vector_ec_elgamal import generate_keys, vector_ec_elgamal_encrypt, vector_ecc_elgamal_decrypt, vector_ecc_elgamal_add, msg_to_point
from py_elgamal.utils import get_random_value

class TestVectorECElGamal(unittest.TestCase):
    def test_generate_keys(self):
        g, x, h = generate_keys()
        self.assertTrue(g is not None)
        self.assertTrue(x is not None)
        self.assertTrue(h is not None)

    def test_vector_ec_elgamal_encrypt_decrypt(self, num_tests=100):
        g, x, h = generate_keys()
        for _ in range(num_tests):
            vector = [get_random_value() for _ in range(5)]
            vector_points = [msg_to_point(g, m) for m in vector]
            ciphertexts = vector_ec_elgamal_encrypt(g, h, vector_points)
            decrypted_vector_points = vector_ecc_elgamal_decrypt(ciphertexts, x)
            self.assertEqual(vector_points, decrypted_vector_points)

    def test_vector_ecc_elgamal_addition(self, num_tests=100):
        g, x, h = generate_keys()
        for _ in range(num_tests):
            vector1 = [get_random_value() for _ in range(5)]
            vector2 = [get_random_value() for _ in range(5)]
            vector1_points = [msg_to_point(g, m) for m in vector1]
            vector2_points = [msg_to_point(g, m) for m in vector2]
            sum_vector_points = [p1 + p2 for p1, p2 in zip(vector1_points, vector2_points)]
            ciphertexts1 = vector_ec_elgamal_encrypt(g, h, vector1_points)
            ciphertexts2 = vector_ec_elgamal_encrypt(g, h, vector2_points)
            sum_ciphertexts = vector_ecc_elgamal_add(ciphertexts1, ciphertexts2)
            decrypted_sum_points = vector_ecc_elgamal_decrypt(sum_ciphertexts, x)
            self.assertEqual(sum_vector_points, decrypted_sum_points)

if __name__ == '__main__':
    unittest.main()
