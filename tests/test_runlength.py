import unittest
from pdfminer.runlength import rldecode


class TestRunlength(unittest.TestCase):
    def test_rldecode(self):
        TESTDATA = b"\x05123456\xfa7\x04abcde\x80junk"
        decoded = rldecode(TESTDATA)
        self.assertEqual(decoded, b"1234567777777abcde")
        return


if __name__ == "__main__":
    unittest.main()
