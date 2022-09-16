import unittest
import io

from tools.dumppdf import dumpoutline


class TestDumppdf(unittest.TestCase):
    def test_simple1(self):
        sample_path = "samples/simple1.pdf"

        with io.StringIO() as dump_output:
            dumpoutline(dump_output, sample_path, [], set())
            dump_output.seek(0)
            dump_output_lines = dump_output.readlines()

            with open("samples/test_samples/simple1_outline.txt") as expect_file:
                expected_lines = expect_file.readlines()

                self.assertEqual(dump_output_lines, expected_lines)


if __name__ == "__main__":
    unittest.main()
