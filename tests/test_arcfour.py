import unittest
from pdfminer.arcfour import Arcfour
#  Simplistic Test cases


class TestArcfour(unittest.TestCase):

    def test_1(self):
        """Test arcfour encryption"""
        self.assertEqual(Arcfour(b'Key').process(
            b'Plaintext').hex(), 'bbf316e8d940af0ad3')
        self.assertEqual(Arcfour(b'Wiki').process(
            b'pedia').hex(), '1021bf0420')
        self.assertEqual(Arcfour(b'Secret').process(
            b'Attack at dawn').hex(), '45a01f645fc35b383552544b9bf5')
        return


if __name__ == "__main__":
    unittest.main()
