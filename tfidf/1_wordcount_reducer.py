#!/usr/bin/env python3
# coding=utf-8

"""WORDCOUNT REDUCER

   Retreive the mapper results from the standard input
   Reduce = Group by key

   OUTPUT ((word, doc_id), wordcount)
"""

import os
import re
import string
import sys

last_key = None
current_count = 0
current_key = None

for line in sys.stdin:

    line = line.strip()
    if line != "":
        # ((word, doc_id), 1)
        current_key, count = eval(line)
        current_key = '("{}",{})'.format(current_key[0], current_key[1])
        count = int(count)

        if last_key == current_key:
            current_count += count
        else:
            if last_key:
                print("({},{})".format(last_key, current_count))
            current_count = count
            last_key = current_key

if last_key == current_key:
    print("({},{})".format(last_key, current_count))
