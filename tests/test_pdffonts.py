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
        expectedFontObject = {
            "Helvetica": "Type 1"
        }
        self.assertEqual(
            commandlineargumenthandler(["null", "samples/simple1.pdf"], usage=usage),
            expectedFontObject,
        )
        return

    # Test correct behaviour of commandlineArgumentHandler given simple2.pdf
    def test_commandlineargumenthandler_simple2(self):
        def usage():
            return 100
        expectedFontObject = {
        }
        self.assertEqual(
            commandlineargumenthandler(["null", "samples/simple2.pdf"], usage=usage),
            expectedFontObject,
        )
        return

    # Test correct behaviour of commandlineArgumentHandler given simple3.pdf
    def test_commandlineargumenthandler_simple3(self):
        def usage():
            return 100
        expectedFontObject = {
            "Helvetica": "Type 1",
            "unknown": "Type CID"
        }
        self.assertEqual(
            commandlineargumenthandler(["null", "samples/simple3.pdf"], usage=usage),
            expectedFontObject,
        )
        return

    

if __name__ == "__main__":
    unittest.main()
