#!/usr/bin/python2
# coding=utf-8

"""WORDPERDOC MAPPER

   Count total words per documents

   key = the document ID
   value = each word with the number of occurences

   Input: ((word, doc_id), wordcount)
   yield (doc_ID, (mot, wordcount))
"""

import sys

lines = []
wordperdoc = {}

for line in sys.stdin:
    line = line.strip()

    if line != "\n":
        word_docid, wordcount = eval(line)
        print('({}, ("{}", {}))'.format(word_docid[1], word_docid[0], wordcount))
