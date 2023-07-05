import unittest
from py_elgamal.ec_elgamal import generate_keys, ec_elgamal_encrypt, ecc_elgamal_decrypt, ecc_elgamal_add, msg_to_point
from py_elgamal.utils import get_random_value

class TestECElGamal(unittest.TestCase):
    def test_generate_keys(self, num_tests=100):
        for _ in range(num_tests):
            g, x, h = generate_keys()
            self.assertTrue(g is not None)
            self.assertTrue(x is not None)
            self.assertTrue(h is not None)

    def test_ec_elgamal_encrypt_decrypt(self, num_tests=100):
        for _ in range(num_tests):
            g, x, h = generate_keys()
            m = [get_random_value() for _ in range(5)]
            ciphertexts = []
            decrypted_m_points = []
            for mi in m:
                m_point = msg_to_point(g, mi)
                ciphertext = ec_elgamal_encrypt(g, h, m_point)
                decrypted_m_point = ecc_elgamal_decrypt(ciphertext[0], ciphertext[1], x)
                ciphertexts.append(ciphertext)
                decrypted_m_points.append(decrypted_m_point)
                self.assertEqual(m_point, decrypted_m_point)
            self.assertEqual(len(m), len(ciphertexts))
            self.assertEqual(len(m), len(decrypted_m_points))

    def test_ecc_elgamal_addition(self, num_tests=100):
        for _ in range(num_tests):
            g, x, h = generate_keys()
            m1 = [get_random_value() for _ in range(5)]
            m2 = [get_random_value() for _ in range(5)]
            ciphertexts1 = []
            ciphertexts2 = []
            decrypted_sums = []
            for m1i, m2i in zip(m1, m2):
                m1_point = msg_to_point(g, m1i)
                m2_point = msg_to_point(g, m2i)
                sum_m_point = m1_point + m2_point
                ciphertext1 = ec_elgamal_encrypt(g, h, m1_point)
                ciphertext2 = ec_elgamal_encrypt(g, h, m2_point)
                sum_ciphertext = ecc_elgamal_add(ciphertext1, ciphertext2)
                decrypted_sum = ecc_elgamal_decrypt(sum_ciphertext[0], sum_ciphertext[1], x)
                ciphertexts1.append(ciphertext1)
                ciphertexts2.append(ciphertext2)
                decrypted_sums.append(decrypted_sum)
                self.assertEqual(sum_m_point, decrypted_sum)
            self.assertEqual(len(m1), len(ciphertexts1))
            self.assertEqual(len(m2), len(ciphertexts2))
            self.assertEqual(len(m1), len(decrypted_sums))

if __name__ == '__main__':
    unittest.main()
