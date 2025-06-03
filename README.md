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



### 3. **Product Title Quality Estimation – CIKM AnalytiCup 2017**
- **Description**: This project is based on the CIKM AnalytiCup 2017 paper titled *"Product Title Classification versus Text Classification – Bagging Model for Product Title Quality with Noise"*.
-  The objective is to predict two attributes of e-commerce product titles: **clarity** and **conciseness**.
- Character-level n-gram features are extracted from product titles and descriptions.
- A bagged ensemble of **LightGBM regressors** is used for prediction.
- The model is evaluated using **Root Mean Squared Error (RMSE)**.
  
- **Technologies Used**: Python, Jupyter Notebook, Pandas, NumPy, Scikit-learn, LightGBM, BeautifulSoup, Regex

- **Key Features**:
  - Text preprocessing with HTML tag removal, lowercasing, and normalization.
  - Character n-gram vectorization (`CountVectorizer` with n-grams from 2 to 6).
  - Bagged ensemble training across multiple folds for robustness.

- **Results**:

  | Metric        | Paper RMSE (XGBoost) | Our RMSE (LightGBM) |
  |---------------|----------------------|----------------------|
  | *Conciseness* | 0.31553              | 0.35273              |
  | *Clarity*     | 0.20745              | 0.52931              |

  While our model does not fully replicate the original paper’s performance due to computational constraints, it closely follows the published methodology and achieves reasonable results.

- **Folder Structure**:
  ```
  Product-Title-Quality-Estimation-CIKMAnalyticup2017/
  ├── data/
  ├── code/
  └── README.md
  ```
