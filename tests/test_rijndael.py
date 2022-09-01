import unittest

from pdfminer.rijndael import RijndaelEncryptor, RijndaelDecryptor


class TestRijndaelDecryptor(unittest.TestCase):

    key = bytes.fromhex('00010203050607080a0b0c0d0f101112')
    ciphertext = bytes.fromhex('d8f532538289ef7d06b506a4fd5be9c9')
    plaintext = '506812a45f08c889b97f5980038b8359'

    def test_encryption(self):
        decryptor = RijndaelDecryptor(self.key, 128)
        assert self.encrypted == decryptor.encrypt(self.plaintext).hex()
    

class TestRijndaelEncryptor(unittest.TestCase):

    key = bytes.fromhex('00010203050607080a0b0c0d0f101112')
    plaintext = bytes.fromhex('506812a45f08c889b97f5980038b8359')
    encrypted = 'd8f532538289ef7d06b506a4fd5be9c9'

    def test_encryption(self):
        encryptor = RijndaelEncryptor(self.key, 128)
        assert self.encrypted == encryptor.encrypt(self.plaintext).hex()


if __name__ == '__main__':
    unittest.main()
