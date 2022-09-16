import unittest
import io

from tools.dumppdf import dumpoutline


class TestDumppdf(unittest.TestCase):
    sample_outline_pairs = [(
        "samples/simple1.pdf",
        "samples/test_samples/simple1_outline.txt"
    ), (
        "samples/test_samples/Introduction_To_Modern_Cryptography.pdf",
        "samples/test_samples/Introduction_To_Modern_Cryptography_outline.txt"
    )]

    def compare_outlines(self, sample, expected):
        with io.StringIO() as dump_output:
            dumpoutline(dump_output, sample, [], set())
            dump_output.seek(0)
            dump_output_lines = dump_output.readlines()

            with open(expected) as expect_file:
                expected_lines = expect_file.readlines()

                self.assertEqual(dump_output_lines, expected_lines)

    def test_sample_outline_pairs(self):
        for (sample, expected) in self.sample_outline_pairs:
            self.compare_outlines(sample, expected)


if __name__ == "__main__":
    unittest.main()
