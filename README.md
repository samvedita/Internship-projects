# 💼 CodTech Data Science Internship – All Tasks

This repository contains solutions to all four tasks assigned as part of the **CodTech Data Science Internship**.

Each task demonstrates a different aspect of data science including data preprocessing, deep learning, deployment, and optimization.
## 📁 Project Structure

CodTech-DS-Internship/
├── Task1_ETL_Pipeline/
│   ├── etl_pipeline.py
│   └── titanic.csv
│
├── Task2_Image_Classification/
│   └── mnist_cnn_classifier.ipynb
│
├── Task3_HousePriceAPI/
│   ├── code.py
│   └── house_data.csv
│
├── Task4_Optimization/
│   └── optimization_lp.py
└── README.md


---

## ✅ Task 1: Data Preprocessing Pipeline (ETL)

**Goal:** Create a pipeline to clean, encode, scale, and transform data.

- Language: Python
- Libraries: `pandas`, `scikit-learn`
- Dataset: Titanic dataset
- Output: Cleaned CSV file `titanic_cleaned.csv`

📄 File: `Task1_ETL_Pipeline/etl_pipeline.py`

---

## ✅ Task 2: Deep Learning Model (Image Classification)

**Goal:** Train a Convolutional Neural Network (CNN) to classify handwritten digits using the MNIST dataset.

- Framework: TensorFlow + Keras
- Dataset: MNIST (loaded via Keras)
- Output: Model accuracy and evaluation

📄 File: `Task2_Image_Classification/mnist_cnn_classifier.ipynb`

---

## ✅ Task 3: End-to-End ML Project with Deployment

**Goal:** Build a complete machine learning workflow from training to deployment using Flask.

- Task: Predict house prices using linear regression
- Dataset: Manually created house dataset
- Deployment: Flask API with `/predict` endpoint
- Input: JSON with area, bedrooms, and age

📄 File: `Task3_HousePriceAPI/task3_house_price_api.py`

---

## ✅ Task 4: Business Optimization using PuLP

**Goal:** Maximize profit for a company using linear programming and constraints on labor and materials.

- Tool: PuLP (Linear Programming in Python)
- Problem: Decide how many units of Product A and B to make
- Output: Optimal production plan and maximum profit

📄 File: `Task4_Optimization/optimization_lp.py`
