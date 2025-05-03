# NLP-Everything

This repository contains all the work I have done in the fields of **Information Retrieval (IR)** and **Natural Language Processing (NLP)** till now. It includes various projects, implementations, and experiments that I've worked on, showcasing the practical application of NLP and IR techniques. Below is an overview of the projects included in this repository.

---

## Projects

### 1. **Boolean IR Search Engine**
   - **Description**: This project implements a Boolean Information Retrieval Model, which includes the creation of **Inverted** and **Positional** indexes for a collection of computer science journal abstracts. The search engine supports Boolean queries (AND, OR, NOT) and proximity queries.
   - **Technologies Used**: Python, Jupyter Notebook
   - **Key Files**:
     - `4004IRAssignment1.ipynb`: Full implementation of the Boolean IR search engine.
     - `frontend/`: Contains the frontend code (`app.py`, `search_engine.py`) for interacting with the search engine.
     - `data/`: Contains datasets such as abstracts and stopword lists.
     - `index/`: Contains the generated inverted and positional indexes.
   - **Folder Structure**:
     ```
     Boolean-IR-Search-Engine/
     ├── data/
     ├── index/
     ├── code/
     └── README.md
     ```

### 2. **Vector Space Model (VSM) IR Search Engine**
   - **Description**: This project implements an Information Retrieval System using the Vector Space Model (VSM). It uses **TF-IDF weighting** and **Cosine Similarity** to rank documents based on their relevance to a user query. A Streamlit GUI is included for an interactive search experience. The system also supports evaluation using Golden Queries.

   - **Technologies Used**: Python, Jupyter Notebook, Streamlit

   - **Key Files**:
   - `4004Assignment2.ipynb`: Core implementation of the VSM system and index generation.
   - `frontend/`: Contains the Streamlit-based frontend (app.py) and backend logic (vsm_engine.py).
   - `data/`: Contains raw abstracts, stopword list, and golden queries.
   - `indexes/`: Stores the generated TF-IDF-based inverted and positional indexes.

- **Folder Structure**:
   ```
   Vector-Space-Model-IR-Search-Engine/
   ├── code/
   │   ├── 4004Assignment2.ipynb
   │   └── frontend/
   │       ├── app.py
   │       └── vsm_engine.py
   ├── data/
   ├── indexes/
   └── README.md
   ```
