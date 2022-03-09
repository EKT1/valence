# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
from valence.bayes import get_classifier, space
from optparse import OptionParser


def doit(fi, fo):
    classifier = get_classifier()
    if classifier:
        for para in fi:
            words = space.split(para)
            feats = dict([(word, True) for word in words])
            print(classifier.classify(feats), file=fo)


def main():
    parser = OptionParser(usage='Usage: %prog file')
    parser.add_option('-s', '--set', action="store_true", default=False, dest="set", help='stdio has file list')
    opts, args = parser.parse_args()

    if not opts.set:
        doit(sys.stdin, sys.stdout)
    else:
        for filename in sys.stdin:
            f = filename.strip()
            print(f, file=sys.stderr)
            fi = open(f, "r")
            fo = open(f + ".e", "w")
            doit(fi, fo)
            fi.close()
            fo.close()


if __name__ == '__main__':
    main()
