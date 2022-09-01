import unittest
import sys
import filecmp
from weakref import ref
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import TextConverter
from tools.pdf2txt import commandlineArgumentHandler, pdf_conversion


class TestPdf2text(unittest.TestCase):
    def test_pdf_conversion(self):

        # fname, rsrcmgr, device, pagenos, maxpages, password, caching, rotation

        rsrcmgr = PDFResourceManager(caching=False)
        imagewriter = None
        laparams = LAParams()

        outputfile = "tests/simple_test_result.txt"
        outfp = open(outputfile, "w", encoding="utf-8")

        device = TextConverter(
            rsrcmgr, outfp, laparams=laparams, imagewriter=imagewriter
        )

        pagenos = set()
        maxpages = 1
        password = b""
        caching = True
        rotation = 0
        pdf_conversion(
            "samples/simple1.pdf",
            rsrcmgr,
            device,
            pagenos,
            maxpages,
            password,
            caching,
            rotation,
        )
        outfp.close()
        result_file = open("tests/simple_test_result.txt", "r+", encoding="utf-8")
        ref_file = open("samples/simple1.txt.ref", "r", encoding="utf-8")

        self.assertTrue(ref_file.read() == result_file.read())
        ref_file.close()
        result_file.close()
        return

    def test_commandlineArgumentHandlerNoArgs(self):
        def usage():
            return 100

        self.assertEqual(commandlineArgumentHandler([], usage=usage), 100)
        return

    def test_commandlineArgumentHandlerInvalidOuttype(self):
        def usage():
            return 100

        self.assertEqual(
            commandlineArgumentHandler(["null", "samples/simple1.pdf"], usage=usage),
            None,
        )
        return


if __name__ == "__main__":
    unittest.main()
