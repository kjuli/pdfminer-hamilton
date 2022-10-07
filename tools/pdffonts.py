#!/usr/bin/env python
import sys
import getopt
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdffont import PDFCIDFont
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import FontConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter
from pdfminer.psparser import PSLiteral


def pdfconversion(
    fname, rsrcmgr, device, pagenos, maxpages, password, caching, rotation
):
    with open(fname, "rb") as fp:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(
            fp,
            pagenos,
            maxpages=maxpages,
            password=password,
            caching=caching,
            check_extractable=True,
        ):
            page.rotate = (page.rotate + rotation) % 360
            interpreter.process_page_font(page)
    return


def commandlineargumenthandler(argv, usage):
    try:
        (opts, args) = getopt.getopt(argv[1:], "dP:O:R:p:m:nAVM:W:L:F:")
    except getopt.GetoptError:
        return usage()
    if not args:
        return usage()

    # debug option
    debug = 0
    # input option
    password = b""
    pagenos = set()
    maxpages = 0
    imagewriter = None
    rotation = 0
    caching = True
    # showpageno = True
    laparams = LAParams()
    for (k, v) in opts:
        if k == "-d":
            debug += 1
        elif k == "-P":
            password = v.encode("ascii")
        elif k == "-O":
            imagewriter = ImageWriter(v)
        elif k == "-R":
            rotation = int(v)
        elif k == "-p":
            pagenos.update(int(x) - 1 for x in v.split(","))
        elif k == "-m":
            maxpages = int(v)
        elif k == "-n":
            laparams = None
        elif k == "-A":
            laparams.all_texts = True
        elif k == "-V":
            laparams.detect_vertical = True
        elif k == "-M":
            laparams.char_margin = float(v)
        elif k == "-W":
            laparams.word_margin = float(v)
        elif k == "-L":
            laparams.line_margin = float(v)
        elif k == "-F":
            laparams.boxes_flow = float(v)
    PDFDocument.debug = debug
    PDFParser.debug = debug
    CMapDB.debug = debug
    PDFPageInterpreter.debug = debug
    rsrcmgr = PDFResourceManager(caching=caching)
    rsrcmgr.get_font(None, {})
    outfp = sys.stdout

    fonttypelookuptable = {
        "PDFTrueTypeFont": "TrueType",
        "PDFType1Font": "Type 1",
        "PDFType3Font": "Type 3",
        "PDFCIDFont": "Type CID",
    }
    device = FontConverter(rsrcmgr, outfp, laparams=laparams, imagewriter=imagewriter)
    for fname in args:
        pdfconversion(
            fname,
            rsrcmgr=rsrcmgr,
            device=device,
            pagenos=pagenos,
            maxpages=maxpages,
            password=password,
            caching=caching,
            rotation=rotation,
        )
    # print results
    print("name".ljust(50) + "type".ljust(10) + "unicode".ljust(10) + "encoding")
    print(
        "------------------------------------------------------------------------------------------"
    )
    fontobject = {}
    for fontkey in rsrcmgr._cached_fonts:
        # Font = class (PDFType1Font etc)
        font = rsrcmgr._cached_fonts[fontkey]
        # Type = TrueType/Type 1/Type 3/Type CID
        fonttype = fonttypelookuptable[font.__class__.__name__]
        # Name = Helvetica etc
        fontname = font.basefont
        # Final object containing all fonts and their types
        fontobject[fontname] = fonttype
        unicode = "No"
        encoding = str(font.encoding)
        if font.unicode_map:
            unicode = "Yes"
        if type(font.encoding) != PSLiteral:
            encoding = "Custom"
        if type(font) == PDFCIDFont:
            encoding = str(font.cidcoding)
        encoding = encoding.replace("/", "")
        encoding = encoding.replace("'", "")
        print(fontname.ljust(50), end="")
        print(fonttype.ljust(10), end="")
        print(unicode.ljust(10), end="")
        print(encoding)

    # outfp.close()
    device.close()
    return fontobject


# main
def main(argv):
    def usage():
        print(
            f"usage: {argv[0]} [-P password]"
            " [-O output_dir] [-R rotation]"
            " [-p pagenos] [-m maxpages]"
            " [-n] [-A] [-V] [-M char_margin] [-L line_margin]"
            " [-W word_margin] [-F boxes_flow] [-d] input.pdf ..."
        )
        return 100

    commandlineargumenthandler(argv, usage)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
