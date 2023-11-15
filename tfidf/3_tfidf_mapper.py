#!/usr/bin/python2
# coding=utf-8

"""TF_IDF MAPPER

   Key: word
   Value: Previous output

   Input: ((word, doc_ID), (wordcount, wordperdoc))
   Output: word, ((word, doc_ID), (wordcount, wordperdoc))
"""

import glob
import os
import re
import string
import sys

lines = []
wordperdoc = {}

for line in sys.stdin:
    (word, doc_ID), (count, wordperdoc) = eval(line.strip())
    print('"{}", {}'.format(word, line.strip()))
