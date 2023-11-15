#!/usr/bin/env python3
# coding=utf-8

"""WORDCOUNT MAPPER

   Read all files from standard input
   Split and clean all words to map as list of key-values
   Ki, Vi => List(Ki, Vi)

   key = (word, doc_id)
   value = 1

   Input: stdin
   Output: ((word, doc_id), 1)
"""

import os
import re
import sys

stopwords = open("utils/stopwords_en.txt").read().split("\n")
current_filename = ""
doc_id = 0

for line in sys.stdin:
    # Set file ID as collection ID
    file_name = os.getenv("map_input_file")
    if current_filename != file_name:
        current_filename = file_name
        doc_id += 1

    # Set to lowercase, remove punctuations and tokenize
    line = line.lower().strip()
    line = re.sub(r"[^\w\s]", "", line)
    words = line.split()

    for word in words:
        any_digit = any(str.isdigit(c) for c in word)
        if len(word) > 3 and not any_digit and word not in stopwords:
            print('(("{}", {}), 1)'.format(word, doc_id))


# def transform(content):
#     content = content.lower()
#     content = re.sub(r'[^\w\s]', '', content)
#     return content

# def read_input(file):
#     file = file.read()
#     for line in file.split('\n'):
#         yield transform(line)

# def main(separator='\t', second_sep='@'):
#     data = read_input(sys.stdin)
#     file_url = os.getenv('mapreduce_map_input_file')
#     file_url = file_url if file_url else "random_filename"
#     if '/' in file_url:
#         file_url = file_url.split('/')[-1]

#     document_words = set()
#     for line in data:
#         document_words.update(line.split())

#     for word in document_words:
#         any_digit = any(str.isdigit(c) for c in word)
#         if len(word) > 3 and not any_digit and word not in stopwords:
#             print('{}{}'.format(word, file_url))

# if __name__ == "__main__":
#     main()
