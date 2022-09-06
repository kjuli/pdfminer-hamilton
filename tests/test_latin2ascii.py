import contextlib
import io
import unittest
from tools.latin2ascii import main


class TestLatin2ascii(unittest.TestCase):

    def test_main(self):
        """Test latin to ascii conversion"""
        expected = "Thi^s i^s a te^xt with spe:ci:al chara:cto:rs"
        with contextlib.redirect_stdout(io.StringIO()) as f:
            main(argv=["", "samples/test_samples/sample_latin2ascii.txt"])
        actual = f.getvalue()
        self.assertEqual(expected, actual)
        return


if __name__ == "__main__":
    unittest.main()
