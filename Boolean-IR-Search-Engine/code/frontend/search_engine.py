import json
import nltk
from nltk.stem import PorterStemmer

# Initialize the stemmer
stemmer = PorterStemmer()

# Load the saved inverted index
with open("inverted_index.json", "r", encoding="utf-8") as f:
    posting_list = json.load(f)

# Load the saved positional index
with open("positional_index.json", "r", encoding="utf-8") as f:
    positional_index = json.load(f)


def boolean_query(term1, operator1=None, term2=None, operator2=None, term3=None):
    """Processes Boolean queries with up to three terms using the posting list.
    Stems terms to match the indexed format.
    Supports AND, OR, and NOT operations.
    """

    # Stemming the terms
    term1 = stemmer.stem(term1)
    term2 = stemmer.stem(term2) if term2 else None
    term3 = stemmer.stem(term3) if term3 else None  

    # Universal Set of all document IDs
    all_docs = set(doc for docs in posting_list.values() for doc in docs)

    # Fetching posting lists
    docs_term1 = set(posting_list.get(term1, []))
    docs_term2 = set(posting_list.get(term2, [])) if term2 else set()
    docs_term3 = set(posting_list.get(term3, [])) if term3 else set()

    # Single-term query
    if not operator1:
        return sorted([int(doc.replace('.txt', '')) for doc in docs_term1])

    # First operation (term1 and term2)
    if operator1 == "AND":
        result1 = docs_term1 & docs_term2
    elif operator1 == "OR":
        result1 = docs_term1 | docs_term2
    elif operator1 == "NOT":
        result1 = all_docs - docs_term1
    else:
        print("Invalid operator1. Use 'AND', 'OR', or 'NOT'.")
        return []

    # If only two terms were provided, return result1
    if not operator2:
        return sorted([int(doc.replace('.txt', '')) for doc in result1])

    # Second operation (result1 and term3)
    if operator2 == "AND":
        final_result = result1 & docs_term3
    elif operator2 == "OR":
        final_result = result1 | docs_term3
    elif operator2 == "NOT":
        final_result = result1 - docs_term3
    else:
        print("Invalid operator2. Use 'AND', 'OR', or 'NOT'.")
        return []

    return sorted([int(doc.replace('.txt', '')) for doc in final_result])


def proximity_query(term1, term2, k):
    """Finds documents where term1 and term2 appear within k positions of each other."""

    # Stemming terms
    term1 = stemmer.stem(term1)
    term2 = stemmer.stem(term2)

    # Check if terms exist in the positional index
    if term1 not in positional_index or term2 not in positional_index:
        return []

    docs_term1 = positional_index[term1]
    docs_term2 = positional_index[term2]

    matching_docs = []
    common_docs = set(docs_term1.keys()) & set(docs_term2.keys())

    for doc in common_docs:
        positions1 = docs_term1[doc]
        positions2 = docs_term2[doc]

        # Two-pointer technique for proximity search
        i, j = 0, 0
        while i < len(positions1) and j < len(positions2):
            if abs(positions1[i] - positions2[j]) <= k + 1:
                matching_docs.append(int(doc.replace('.txt', '')))
                break
            elif positions1[i] < positions2[j]:
                i += 1
            else:
                j += 1

    return sorted(matching_docs)
