# -*- coding: utf-8 -*-
import sys
import os
import operator
import array
import codecs
import re
import random
import pickle
from collections import defaultdict
from optparse import OptionParser
from nltk.classify import NaiveBayesClassifier

space = re.compile('[\'".,!?\\s\\(\\)]+')
cats = ('positiivne','negatiivne','neutraalne','vastuoluline')
classifier = None
corpus_name = 'korpus.csv'

def load_corpus():
  print >> sys.stderr, "Load corpus:", corpus_name
  features = []
  with codecs.open(corpus_name, 'r', encoding='utf-8') as f:
    #for line in f: print line
    for line in f:
        row = line.split(',',1)
        words = space.split(row[1])
        feats = dict([(word, True) for word in words])
        features.append((feats,row[0]))
  return features

def get_classifier():
    global classifier
    if not classifier:
        corpus = load_corpus()
        if corpus:
            print >> sys.stderr,  "Train"
            classifier = NaiveBayesClassifier.train(corpus)
            #print >> sys.stderr,  classifier.labels()
            #print >> sys.stderr,  classifier.most_informative_features(n=10)
        else:
            print >> sys.stderr, "No corpus!"

def classify(words):
    get_classifier()
    feats = dict([(word, True) for word in words])
    return classifier.classify(feats)

def doit():

    get_classifier()
    if classifier:
        for para in sys.stdin:
            words = space.split(para)
            feats = dict([(word, True) for word in words])
            print classifier.classify(feats)

def main():
    global classifier_name
    global corpus_name
    parser = OptionParser(usage='Usage: %prog')
    parser.add_option('-f', '--file', dest="filename", help='Corpus file')
    opts, args = parser.parse_args()

    #if len(args)!=1: # or not opts.segment:
    #    parser.print_help()
    #    sys.exit(1)

    if opts.filename:
        corpus_name = opts.filename

    doit()

if __name__ == '__main__':
    main()

