# -*- coding: utf-8 -*-
from __future__ import print_function
from valence.bayes import *
from optparse import OptionParser

corpus_name = None

def doit(fi, fo):
    get_classifier(corpus_name)
    if classifier:
        for para in fi:
            words = space.split(para)
            feats = dict([(word, True) for word in words])
            print(classifier.classify(feats), file=fo)


def main():
    global corpus_name
    parser = OptionParser(usage='Usage: %prog file')
    parser.add_option('-f', '--file', dest="filename", help='Corpus file')
    parser.add_option('-s', '--set', action="store_true", default=False, dest="set", help='stdio has file list')
    opts, args = parser.parse_args()

    # if len(args)!=1: # or not opts.segment:
    #    parser.print_help()
    #    sys.exit(1)

    if opts.filename:
        corpus_name = opts.filename

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
