import unittest
import io

from tools.dumppdf import dumpoutline


class TestDumppdf(unittest.TestCase):
    def compare_outlines(self, sample, expected):
        with io.StringIO() as dump_output:
            dumpoutline(dump_output, sample, [], set())
            dump_output.seek(0)
            dump_output_lines = dump_output.readlines()

            with open(expected) as expect_file:
                expected_lines = expect_file.readlines()

                self.assertEqual(dump_output_lines, expected_lines)

    def test_simple1(self):
        self.compare_outlines("samples/simple1.pdf", "samples/test_samples/simple1_outline.txt")

    def test_cryptography_intro(self):
        self.compare_outlines(
            "samples/test_samples/Introduction_To_Modern_Cryptography.pdf",
            "samples/test_samples/Introduction_To_Modern_Cryptography_outline.txt"
        )


if __name__ == "__main__":
    unittest.main()
