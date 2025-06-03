# 🛍️ Product Title Quality Estimation – CIKM AnalytiCup 2017

This repository contains a simplified and partial reproduction of the paper:

**“Product Title Classification versus Text Classification – Bagging Model for Product Title Quality with Noise”**  
*CIKM AnalytiCup 2017*  

---

## 🎯 Objective

Predict the **clarity** and **conciseness** of product titles from e-commerce listings.  
These quality scores help in understanding how readable and informative a product title is for customers.

---

## 🗂️ Dataset

The dataset includes:
- Product titles, descriptions, and category hierarchy
- Numeric and categorical attributes (price, delivery type)
- Target labels for:
  - `clarity`
  - `conciseness`

**Files used** (available from CIKM 2017 AnalytiCup data):
- `data_train.csv`, `data_valid.csv`
- `clarity_train.labels`, `conciseness_train.labels`
- `clarity_valid.predict`, `conciseness_valid.predict`

---

## ⚙️ Pipeline Overview

### 1. **Data Loading & Cleaning**
- Load training and validation product data
- Merge corresponding labels with input features
- Clean titles and descriptions:
  - Strip HTML and special characters
  - Convert to lowercase
  - Remove extra whitespace

### 2. **Feature Engineering**
- Concatenate cleaned title and description into a unified text field
- Extract character-level n-grams (range: 2–6)
- Vectorize using `CountVectorizer` with `max_features=5000`

### 3. **Model Training (LightGBM)**
- Bagging ensemble with `n_bags = 4`
- 10-fold cross-validation inside each bag (40 models per target)
- Separate regressors trained for `clarity` and `conciseness`

### 4. **Evaluation**
- Root Mean Squared Error (RMSE) computed on validation set

---

## 📉 Results

| Metric        | Paper (XGBoost) | This Implementation (LightGBM) |
|---------------|-----------------|-------------------------------|
| Conciseness   | **0.31553**     | 0.35273                       |
| Clarity       | **0.20745**     | 0.52931                       |

> 📌 *Note: This implementation only uses the LightGBM model with character n-grams. The full ensemble described in the paper (including Ridge and SVR) is not replicated here.*

---

## 🚀 Getting Started

### ✅ Prerequisites

Install required Python libraries:

```bash
pip install pandas numpy scikit-learn lightgbm beautifulsoup4


Ensure the following files are placed in their respective folders:

data/
├── training/
│   ├── data_train.csv
│   ├── clarity_train.labels
│   └── conciseness_train.labels
└── validation/
    ├── data_valid.csv
    ├── clarity_valid.predict
    └── conciseness_valid.predict

