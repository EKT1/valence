# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from optparse import OptionParser
from valence.valencecolor import *


def doit(filename, silent):
    """Standalone"""
    load()
    fi = codecs.open(filename, 'r', encoding='utf-8')
    text = fi.read()
    fi.close()
    t = mark(text)
    s = chart(t[1], t[2])

    if not silent:
        fo = codecs.open(filename + '.html', 'w', encoding='utf-8')
        fo.write(htmlStart)
        fo.write(t[0])
        # fo.write(t[0].replace('\r','<br>'))
        fo.write(chartStats(t[1], t[2], t[3]))
        fo.write(htmlEnd)
        fo.close()
    else:
        print("Dict:", s[0])
        print("Dict:", s[1])
        print("Bayes:", emotionBayes(t[3], t[1], t[2]), t[3])


def main():
    silent = None
    parser = OptionParser(usage='Usage: %prog file')
    parser.add_option('-s', '--silent', action="store_true", dest="silent", help='Silent: no html file')
    opts, args = parser.parse_args()
    if len(args) != 1:  # or not opts.segment:
        parser.print_help()
        sys.exit(1)
    if opts.silent:
        silent = opts.silent

    doit(args[0], silent)


if __name__ == '__main__':
    main()
