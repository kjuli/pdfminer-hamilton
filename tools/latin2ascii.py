#!/usr/bin/env python

"""latin2ascii.py - converts latin1 characters into ascii."""


import sys

"""
Mappings from Latin-1 characters to ASCII.

This is an in-house mapping table for some Latin-1 characters
(acutes, umlauts, etc.) to ASCII strings.
"""

LATIN2ASCII = {
    # 0x00a0: '',
    # 0x00a7: '',
<<<<<<< HEAD

    # iso-8859-1
    0x00c0: 'A`',
    0x00c1: "A'",
    0x00c2: 'A^',
    0x00c3: 'A~',
    0x00c4: 'A:',
    0x00c5: 'A%',
    0x00c6: 'AE',
    0x00c7: 'C,',
    0x00c8: 'E`',
    0x00c9: "E'",
    0x00ca: 'E^',
    0x00cb: 'E:',
    0x00cc: 'I`',
    0x00cd: "I'",
    0x00ce: 'I^',
    0x00cf: 'I:',
    0x00d0: "D'",
    0x00d1: 'N~',
    0x00d2: 'O`',
    0x00d3: "O'",
    0x00d4: 'O^',
    0x00d5: 'O~',
    0x00d6: 'O:',
    0x00d8: 'O/',
    0x00d9: 'U`',
    0x00da: "U'",
    0x00db: 'U~',
    0x00dc: 'U:',
    0x00dd: "Y'",
    0x00df: 'ss',

    0x00e0: 'a`',
    0x00e1: "a'",
    0x00e2: 'a^',
    0x00e3: 'a~',
    0x00e4: 'a:',
    0x00e5: 'a%',
    0x00e6: 'ae',
    0x00e7: 'c,',
    0x00e8: 'e`',
    0x00e9: "e'",
    0x00ea: 'e^',
    0x00eb: 'e:',
    0x00ec: 'i`',
    0x00ed: "i'",
    0x00ee: 'i^',
    0x00ef: 'i:',
    0x00f0: "d'",
    0x00f1: 'n~',
    0x00f2: 'o`',
    0x00f3: "o'",
    0x00f4: 'o^',
    0x00f5: 'o~',
    0x00f6: 'o:',
    0x00f8: 'o/',
    0x00f9: 'o`',
    0x00fa: "u'",
    0x00fb: 'u~',
    0x00fc: 'u:',
    0x00fd: "y'",
    0x00ff: 'y:',

    # Ligatures
    0x0152: 'OE',
    0x0153: 'oe',
    0x0132: 'IJ',
    0x0133: 'ij',
    0x1d6b: 'ue',
    0xfb00: 'ff',
    0xfb01: 'fi',
    0xfb02: 'fl',
    0xfb03: 'ffi',
    0xfb04: 'ffl',
    0xfb05: 'ft',
    0xfb06: 'st',

    # Symbols
    # 0x2013: '',
    0x2014: '--',
    0x2015: '||',
    0x2018: '`',
    0x2019: "'",
    0x201c: '``',
    0x201d: "''",
    # 0x2022: '',
    # 0x2212: '',

=======
    # iso-8859-1
    0x00C0: "A`",
    0x00C1: "A'",
    0x00C2: "A^",
    0x00C3: "A~",
    0x00C4: "A:",
    0x00C5: "A%",
    0x00C6: "AE",
    0x00C7: "C,",
    0x00C8: "E`",
    0x00C9: "E'",
    0x00CA: "E^",
    0x00CB: "E:",
    0x00CC: "I`",
    0x00CD: "I'",
    0x00CE: "I^",
    0x00CF: "I:",
    0x00D0: "D'",
    0x00D1: "N~",
    0x00D2: "O`",
    0x00D3: "O'",
    0x00D4: "O^",
    0x00D5: "O~",
    0x00D6: "O:",
    0x00D8: "O/",
    0x00D9: "U`",
    0x00DA: "U'",
    0x00DB: "U~",
    0x00DC: "U:",
    0x00DD: "Y'",
    0x00DF: "ss",
    0x00E0: "a`",
    0x00E1: "a'",
    0x00E2: "a^",
    0x00E3: "a~",
    0x00E4: "a:",
    0x00E5: "a%",
    0x00E6: "ae",
    0x00E7: "c,",
    0x00E8: "e`",
    0x00E9: "e'",
    0x00EA: "e^",
    0x00EB: "e:",
    0x00EC: "i`",
    0x00ED: "i'",
    0x00EE: "i^",
    0x00EF: "i:",
    0x00F0: "d'",
    0x00F1: "n~",
    0x00F2: "o`",
    0x00F3: "o'",
    0x00F4: "o^",
    0x00F5: "o~",
    0x00F6: "o:",
    0x00F8: "o/",
    0x00F9: "o`",
    0x00FA: "u'",
    0x00FB: "u~",
    0x00FC: "u:",
    0x00FD: "y'",
    0x00FF: "y:",
    # Ligatures
    0x0152: "OE",
    0x0153: "oe",
    0x0132: "IJ",
    0x0133: "ij",
    0x1D6B: "ue",
    0xFB00: "ff",
    0xFB01: "fi",
    0xFB02: "fl",
    0xFB03: "ffi",
    0xFB04: "ffl",
    0xFB05: "ft",
    0xFB06: "st",
    # Symbols
    # 0x2013: '',
    0x2014: "--",
    0x2015: "||",
    0x2018: "`",
    0x2019: "'",
    0x201C: "``",
    0x201D: "''",
    # 0x2022: '',
    # 0x2212: '',
>>>>>>> master
}


def latin2ascii(s):
<<<<<<< HEAD
    """Convert latin1 string to ascii code."""
    return ''.join(LATIN2ASCII.get(ord(c), c) for c in s)


def main(argv):
    """Run main function."""
=======
    return "".join(LATIN2ASCII.get(ord(c), c) for c in s)


def main(argv):
>>>>>>> master
    import getopt
    import fileinput

    def usage():
        print("usage: %s [-c codec] file ..." % argv[0])
        return 100

    try:
        (opts, args) = getopt.getopt(argv[1:], "c")
    except getopt.GetoptError:
        return usage()
    if not args:
        return usage()
<<<<<<< HEAD
    codec = 'utf-8'
    for (k, v) in opts:
        if k == '-c':
            codec = v
    for line in fileinput.input(args):
        line = latin2ascii(str(line.encode(), codec, 'ignore'))
        sys.stdout.write(line.encode(
            codec, 'ignore').decode('ascii', 'replace'))
    return


if __name__ == '__main__':
=======
    codec = "utf-8"
    for (k, v) in opts:
        if k == "-c":
            codec = v
    for line in fileinput.input(args):
        line = latin2ascii(unicode(line, codec, "ignore"))  # noqa: F821 # we will look at this later
        sys.stdout.write(line.encode("ascii", "replace"))
    return


if __name__ == "__main__":
>>>>>>> master
    sys.exit(main(sys.argv))
