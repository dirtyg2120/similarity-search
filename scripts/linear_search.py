from datetime import datetime
import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize
from glob import glob

def jaccard(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = len(set1.intersection(set2))
    union = (len(set1) + len(set2)) - intersection
    similarity = float(intersection) / union
    return intersection, union, similarity

def linear_search(root_path, search_term):
    start_time = datetime.now()
    found_times = {}
    num_found = 0
    search_set = set(word_tokenize(search_term.lower()))
    
    print("JACCARD SIMILARITY WITH LINEAR SEARCH")
    print("Search term:", search_term, "\n")
    
    for filepath in glob(root_path + '/*.txt'):
        with open(filepath, 'r', encoding='utf-8') as f:
            file_set = set()
            for line_num, line in enumerate(f):
                line_set = set(word_tokenize(line.lower()))
                file_set.update(line_set)
            intersection, union, similarity = jaccard(search_set, file_set)
            if similarity > 0:
                num_found += 1
                now = datetime.now()
                found_times[num_found] = (now - start_time).total_seconds()
                print(f'({num_found})\t({intersection}\t{union}\t{similarity:.8f})\t{filepath}\t{(now - start_time).total_seconds():.2f}s')

# Example usage
root_path = 'input'
search_term = input("Enter the search term: ")
linear_search(root_path, search_term)
