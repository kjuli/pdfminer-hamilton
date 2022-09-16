import unittest
import io
import sys

from tools.dumppdf import dumpoutline


class TestDumppdf(unittest.TestCase):
    def test_simple1(self):
        sample_path = "samples/simple1.pdf"

        with io.StringIO() as dump_output:
            dumpoutline(dump_output, sample_path, [], set())
            dump_output.seek(0)

            for line in dump_output:
                sys.stdout.write(line)

        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
