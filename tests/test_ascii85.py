import unittest
from pdfminer.ascii85 import *
#  Simplistic Test cases


class TestAscii85(unittest.TestCase):

    def test_ascii85decode(self):
        self.assertEqual(ascii85decode(
            b'9jqo^BlbD-BleB1DJ+*+F(f,q'), b'Man is distinguished')
        self.assertEqual(ascii85decode(b'E,9)oF*2M7/c~>'), b'pleasure.')
        return

    def test_asciihexdecode(self):
        self.assertEqual(asciihexdecode(b'61 62 2e6364   65'), b'ab.cde')
        self.assertEqual(asciihexdecode(b'61 62 2e6364   657>'), b'ab.cdep')
        self.assertEqual(asciihexdecode(b'7>'), b'p')
        return


if __name__ == "__main__":
    unittest.main()
