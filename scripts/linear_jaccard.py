from nltk.tokenize import word_tokenize
import os
import time
from datetime import datetime
import re

def transform(content):
    content = content.lower()
    content = re.sub(r"[^\w\s]", "", content)
    return set(word_tokenize(content))

def jaccard(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = len(set1.intersection(set2))
    union = (len(set1) + len(set2)) - intersection
    similarity = float(intersection) / union
    return intersection, union, similarity


def linear_search_files_jaccard(root_path, search_term):
    num_found = 0
    search_set = transform(search_term)
    print("Search term:", search_term, "\n")

    for subdir, dirs, files in os.walk(root_path):
        for file in files:
            start_file = time.time()
            if file.endswith(".txt"):
                filepath = os.path.join(subdir, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    file_set = set()
                    for line_num, line in enumerate(f):
                        line_set = transform(line.lower())
                        file_set.update(line_set)
                    intersection, union, similarity = jaccard(search_set, file_set)
                if similarity > 0:
                    num_found += 1
                    print(
                        f"({num_found})\t({similarity:.8f})\t{filepath}\t{time.time()-start_file}"
                    )


    if num_found == 0:
        print("Search term not found.\n")
    else:
        print(f"Total number of times found: {num_found}")


if __name__ == "__main__":
    root_path = "."
    search_term = input("Enter the search term: ")
    start = time.time()
    linear_search_files_jaccard(root_path, search_term)
    print(time.time() - start)
