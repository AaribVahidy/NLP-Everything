# Vector Space Model (VSM) IR Search Engine

## Overview
This project implements an **Information Retrieval System** based on the **Vector Space Model (VSM)** using **TF-IDF weighting** and **Cosine Similarity** to rank documents by relevance to a user query.

The system is designed to work on a dataset of computer science abstracts and includes a **Streamlit-based GUI** for an interactive search experience.

---

## Key Features
- **TF-IDF Vectorization**: Converts documents and queries into weighted vectors.
- **Cosine Similarity**: Ranks documents by computing similarity between query and document vectors.
- **Interactive Frontend**: Streamlit GUI for querying and displaying top results.
- **Golden Query Evaluation**: Option to run predefined golden queries for evaluation.

---

## Folder Structure

Vector-Space-Model-IR-Search-Engine/
├── code/
│ ├── 4004Assignment2.ipynb # Core code to preprocess data, build indexes, and implement TF-IDF logic
│ └── frontend/
│ ├── app.py # Streamlit frontend (run this file from terminal)
│ └── vsm_engine.py # Backend logic used by the frontend to process queries
│
├── data/
│ ├── abstracts.rar # Raw text data (448 abstracts from CS journals)
│ ├── stopword-list.txt # List of stopwords used for preprocessing
│ └── Gold-Query-VSM.txt # File containing golden queries and relevant document IDs
│
├── indexes/
│ ├── inverted_index.pkl # Pickled inverted index
│ └── positional_index.pkl # Pickled positional index
│
└── README.md # Project documentation

## Instructions

### 1. Run the Notebook
Start by opening and running the notebook:
- `code/4004Assignment2.ipynb`  
This generates the inverted and positional indexes and saves them as `.pkl` files in the `indexes/` folder.

### 2. Launch the Frontend
Once the notebook is run and the index files are created, you can launch the Streamlit app:
```bash
cd code/frontend
streamlit run app.py

Make sure vsm_engine.py is in the same directory as app.py.

3. Using the App
Enter any search query in the input box to retrieve ranked documents.

Optionally, select a golden query from the dropdown to test system performance against a predefined set.


Notes
If Gold-Query-VSM.txt is not found, the golden query option will not be shown.

The abstract documents are stored in abstracts.rar and must be extracted before running the notebook.