import sys
import unittest
from tools.pdffonts import commandlineargumenthandler


class TestPdffonts(unittest.TestCase):
    # Test calling commandlineArgumentHandler with no args
    def test_commandlineargumenthandlernoargs(self):
        def usage():
            return 100

        self.assertEqual(commandlineargumenthandler([], usage=usage), 100)
        return

    # Test correct behaviour of commandlineArgumentHandler given simple1.pdf
    def test_commandlineargumenthandler_simple1(self):
        def usage():
            return 100

        expectedFontObject = {"Helvetica": "Type 1"}
        sys.stdout = open("/dev/stdout", "w")
        self.assertEqual(
            commandlineargumenthandler(["null", "samples/simple1.pdf"], usage=usage),
            expectedFontObject,
        )
        return

    # Test correct behaviour of commandlineArgumentHandler given simple2.pdf
    def test_commandlineargumenthandler_simple2(self):
        def usage():
            return 100

        expectedFontObject = {}
        sys.stdout = open("/dev/stdout", "w")
        self.assertEqual(
            commandlineargumenthandler(["null", "samples/simple2.pdf"], usage=usage),
            expectedFontObject,
        )
        return

    # Test correct behaviour of commandlineArgumentHandler given simple3.pdf
    def test_commandlineargumenthandler_simple3(self):
        def usage():
            return 100

        expectedFontObject = {"Helvetica": "Type 1", "unknown": "Type CID"}
        sys.stdout = open("/dev/stdout", "w")
        self.assertEqual(
            commandlineargumenthandler(["null", "samples/simple3.pdf"], usage=usage),
            expectedFontObject,
        )
        return

    # Test correct behaviour of commandlineArgumentHandler given simple3.pdf with 90 degree rotation
    def test_commandlineargumenthandler_simple3withrotation90(self):
        def usage():
            return 100

        expectedFontObject = {"Helvetica": "Type 1", "unknown": "Type CID"}
        sys.stdout = open("/dev/stdout", "w")
        self.assertEqual(
            commandlineargumenthandler(
                ["null", "-R", "90", "samples/simple3.pdf"], usage=usage
            ),
            expectedFontObject,
        )
        return

    # Test correct behaviour of commandlineArgumentHandler given simple3.pdf with 180 degree rotation
    def test_commandlineargumenthandler_simple3withrotation180(self):
        def usage():
            return 100

        expectedFontObject = {"Helvetica": "Type 1", "unknown": "Type CID"}
        sys.stdout = open("/dev/stdout", "w")
        self.assertEqual(
            commandlineargumenthandler(
                ["null", "-R", "180", "samples/simple3.pdf"], usage=usage
            ),
            expectedFontObject,
        )
        return  # Test correct behaviour of commandlineArgumentHandler given simple3.pdf with 270 degree rotation

    def test_commandlineargumenthandler_simple3withrotation270(self):
        def usage():
            return 100

        expectedFontObject = {"Helvetica": "Type 1", "unknown": "Type CID"}
        sys.stdout = open("/dev/stdout", "w")
        self.assertEqual(
            commandlineargumenthandler(
                ["null", "-R", "270", "samples/simple3.pdf"], usage=usage
            ),
            expectedFontObject,
        )
        return

    # Test correct behaviour of commandlineArgumentHandler given an encrypted pdf
    def test_commandlineargumenthandler_encrypted(self):
        def usage():
            return 100

        expectedFontObject = {"BAAAAA+TimesNewRomanPSMT": "TrueType"}
        sys.stdout = open("/dev/stdout", "w")
        self.assertEqual(
            commandlineargumenthandler(
                ["tools/pdffonts.py", "-P", "foo", "samples/encryption/aes-128-m.pdf"],
                usage=usage,
            ),
            expectedFontObject,
        )
        return

    # Test correct behaviour of commandlineArgumentHandler with page number restriction
    def test_commandlineargumenthandler_pagenos(self):
        def usage():
            return 100

        expectedFontObject = {
            "PDDIPA+Helvetica": "Type 1",
            "PDDJAB+ZapfDingbats": "Type 1",
            "PDDJAC+Helvetica-Oblique": "Type 1",
            "PDDJAD+Helvetica-Bold": "Type 1",
            "PDDJCD+Helvetica-Condensed-Black": "Type 1",
            "PDDJCE+FranklinGothic-Demi": "Type 1",
            "PDDJDF+Symbol": "Type 1",
            "PDDJEF+Helvetica-Black": "Type 1",
        }
        sys.stdout = open("/dev/stdout", "w")
        self.assertEqual(
            commandlineargumenthandler(
                ["tools/pdffonts.py", "-p", "1", "samples/nonfree/i1040nr.pdf"],
                usage=usage,
            ),
            expectedFontObject,
        )
        return

    # Test correct behaviour of commandlineArgumentHandler with -n flag
    def test_commandlineargumenthandler_nflag(self):
        def usage():
            return 100

        expectedFontObject = {
            "PDDIPA+Helvetica": "Type 1",
            "PDDJAB+ZapfDingbats": "Type 1",
            "PDDJAC+Helvetica-Oblique": "Type 1",
            "PDDJAD+Helvetica-Bold": "Type 1",
            "PDDJCD+Helvetica-Condensed-Black": "Type 1",
            "PDDJCE+FranklinGothic-Demi": "Type 1",
            "PDDJDF+Symbol": "Type 1",
            "PDDJEF+Helvetica-Black": "Type 1",
        }
        sys.stdout = open("/dev/stdout", "w")
        self.assertEqual(
            commandlineargumenthandler(
                ["tools/pdffonts.py", "-p", "1", "-n", "samples/nonfree/i1040nr.pdf"],
                usage=usage,
            ),
            expectedFontObject,
        )
        return


if __name__ == "__main__":
    unittest.main()
