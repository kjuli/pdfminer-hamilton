#!/usr/bin/env python
#
# RunLength decoder (Adobe version) implementation based on PDF Reference
# version 1.4 section 3.3.4.
#
#  * public domain *
#


def rldecode(data):
    r"""
    RunLength decoder (Adobe version) implementation based on PDF Reference
    version 1.4 section 3.3.4:
        The RunLengthDecode filter decodes data that has been encoded in a
        simple byte-oriented format based on run length. The encoded data
        is a sequence of runs, where each run consists of a length byte
        followed by 1 to 128 bytes of data. If the length byte is in the
        range 0 to 127, the following length + 1 (1 to 128) bytes are
        copied literally during decompression. If length is in the range
        129 to 255, the following single byte is to be copied 257 - length
        (2 to 128) times during decompression. A length value of 128
        denotes EOD.
    """
    decoded = b""
    i = 0
    while i < len(data):
        # print('data[%d]=:%d:' % (i,ord(data[i])))
        length = data[i]
        if length == 128:
            break
        if length >= 0 and length < 128:
            run = data[i + 1 : (i + 1) + (length + 1)]
            # print('length=%d, run=%s' % (length+1,run))
            decoded += run
            i = (i + 1) + (length + 1)
        if length > 128:
            run = data[i + 1 : i + 2] * (257 - length)
            # print('length=%d, run=%s' % (257-length,run))
            decoded += run
            i = (i + 1) + 1
    return decoded
