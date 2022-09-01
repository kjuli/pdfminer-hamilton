import unittest
from pdfminer.lzw import lzwdecode
#  Simplistic Test cases
#


class TestLzw(unittest.TestCase):

    TESTDATA = '800b6050220c0c8501'
    TESTRESULT = b'-----A---B'

    def test_1(self):
        decoded = lzwdecode(bytes.fromhex(self.TESTDATA))
        self.assertEqual(decoded, self.TESTRESULT)
        return


if __name__ == "__main__":
    unittest.main()
