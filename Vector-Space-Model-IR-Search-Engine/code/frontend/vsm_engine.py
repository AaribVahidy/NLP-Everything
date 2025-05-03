import os
import math
from collections import defaultdict, Counter
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
from nltk.tokenize import word_tokenize

# GLOBALS
my_stopwords = set([
    "a", "is", "the", "of", "all", "and", "to", "can", "be", "as", "once", 
    "for", "at", "am", "are", "has", "have", "had", "up", "his", "her", 
    "in", "on", "no", "we", "do"
])
lemmatizer = WordNetLemmatizer()

# ---------------------- PREPROCESSING ----------------------
def preprocess_text(text, for_query=False):
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens]
    filtered_tokens = [word for word in tokens if word not in my_stopwords]
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    return lemmatized_tokens

def preprocess_documents(folder_path):
    processed_docs = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="windows-1252") as file:
                text = file.read()
            tokens = preprocess_text(text)
            processed_docs[filename] = tokens
    return processed_docs

# ---------------------- TF-IDF ----------------------
def compute_tfidf_vector(tf, df_counter, N, vocab):
    vector = []
    for term in vocab:
        tf_val = tf.get(term, 0)
        df_val = df_counter.get(term, 1)
        tfidf = tf_val * math.log(N / df_val)
        vector.append(tfidf)
    return vector

# ---------------------- COSINE SIM ----------------------
def cosine_similarity(vec1, vec2):
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))
    return dot / (norm1 * norm2 + 1e-10)

# ---------------------- INDEX BUILDING ----------------------
def build_index_and_vectors(folder_path):
    processed_docs = preprocess_documents(folder_path)

    vocab = set()
    tf_dict = {}
    df_counter = Counter()

    for doc, tokens in processed_docs.items():
        tf = Counter(tokens)
        tf_dict[doc] = tf
        for term in tf:
            df_counter[term] += 1
        vocab.update(tokens)

    vocab = sorted(vocab)
    N = len(processed_docs)

    doc_vectors = {}
    for doc in processed_docs:
        doc_vectors[doc] = compute_tfidf_vector(tf_dict[doc], df_counter, N, vocab)

    inverted_index = defaultdict(set)
    for doc_id, tokens in processed_docs.items():
        for token in set(tokens):
            inverted_index[token].add(doc_id)

    for term in inverted_index:
        inverted_index[term] = sorted(list(inverted_index[term]))

    return df_counter, N, doc_vectors, vocab, inverted_index, processed_docs

# ---------------------- QUERY PROCESSING ----------------------
def process_query(query, alpha=0.005, top_k=25):
    query_tokens = preprocess_text(query, for_query=True)
    tf_q = Counter(query_tokens)
    query_vec = compute_tfidf_vector(tf_q, df_counter, N, vocab)

    similarities = []
    for doc, vec in doc_vectors.items():
        sim = cosine_similarity(query_vec, vec)
        if sim >= alpha:
            doc_num = int(doc.replace(".txt", "")) 
            similarities.append((doc_num, sim))

    return sorted(similarities, key=lambda x: x[1], reverse=True)[:top_k]

# ---------------------- BUILD INDEX (RUN ON IMPORT) ----------------------
df_counter, N, doc_vectors, vocab, inverted_index, processed_docs = build_index_and_vectors("Abstracts/")
