import nltk

nltk.download("punkt")
import os
import time
from datetime import datetime

from nltk.tokenize import word_tokenize


def jaccard(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = len(set1.intersection(set2))
    union = (len(set1) + len(set2)) - intersection
    similarity = float(intersection) / union
    return intersection, union, similarity


def linear_search_files_jaccard(root_path, search_term):
    start_time = datetime.now()
    num_found = 0

    found_times = {}
    search_set = set(word_tokenize(search_term.lower()))
    print("JACCARD SIMILARITY WITH LINEAR SEARCH")
    print("Search term:", search_term, "\n")
    for subdir, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith(".txt"):
                filepath = os.path.join(subdir, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    file_set = set()
                    for line_num, line in enumerate(f):
                        line_set = set(word_tokenize(line.lower()))
                        file_set.update(line_set)
                    intersection, union, similarity = jaccard(search_set, file_set)
                if similarity > 0:
                    num_found += 1
                    now = datetime.now()
                    found_times[num_found] = (now - start_time).total_seconds()
                    print(
                        f"({num_found})\t({intersection}\t{union}\t{similarity:.8f})\t{filepath}\t\t{(now - start_time).total_seconds():.2f}s"
                    )

    end_time = datetime.now()
    duration = end_time - start_time

    print(f"\nTotal time taken: {duration.total_seconds():.2f}s")

    if num_found == 0:
        print("Search term not found.\n")
    else:
        print(f"Total number of times found: {num_found}")


if __name__ == "__main__":
    root_path = "."
    search_term = """
        Hello it's me
    """
    start = time.time()
    linear_search_files_jaccard(root_path, search_term)
    print(time.time() - start)
