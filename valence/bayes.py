# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import codecs
import re
import pkg_resources
from nltk.classify import NaiveBayesClassifier

space = re.compile('[\'".,!?\\s\\(\\)]+')
cats = ('positiivne', 'negatiivne', 'neutraalne', 'vastuoluline')
classifier = None
corpus_name = pkg_resources.resource_filename("valence", "korpus.csv")


def load_corpus(corpus_name=corpus_name):
    print("Load corpus:", corpus_name, file=sys.stderr)
    features = []
    with codecs.open(corpus_name, 'r', encoding='utf-8') as f:
        # for line in f: print line
        for line in f:
            row = line.split(',', 1)
            words = space.split(row[1])
            feats = dict([(word, True) for word in words])
            features.append((feats, row[0]))
    return features


def get_classifier():
    global classifier
    if not classifier:
        corpus = load_corpus()
        if corpus:
            print("Train", file=sys.stderr)
            classifier = NaiveBayesClassifier.train(corpus)
            # print >> sys.stderr,  classifier.labels()
            print(classifier.show_most_informative_features(100), file=sys.stderr)
        else:
            print("No corpus!", file=sys.stderr)


def classify(words):
    get_classifier()
    feats = dict([(word, True) for word in words])
    return classifier.classify(feats)


def prob_classify(words):
    get_classifier()
    feats = dict([(word, True) for word in words])
    return classifier.prob_classify(feats)
