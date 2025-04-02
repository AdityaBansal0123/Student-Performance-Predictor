# 🧑‍🎓 Examination-Marks-Predictor 📊

This machine learning project predicts the **Math marks** of students based on various factors such as **Gender**, **Ethnicity**, **Parental Level of Education**, **Lunch Type**, **Test Preparation Course**, and individual **Reading** and **Writing Scores**. 

By using this model, we aim to understand how these factors impact students' academic performance in mathematics. 🎯

---

## 📋 Project Overview

This project aims to predict student performance in **Mathematics** based on key factors such as:

- **Gender** 👦👧
- **Race or Ethnicity** 🌍
- **Parental Level of Education** 🎓
- **Lunch Type** 🍽️
- **Test Preparation Course** 📚
- **Reading and Writing Scores** ✍️📖

By understanding how these variables affect a student's performance, we can provide insights for educational improvements.

---

## 🧑‍💻 Dataset Information

The dataset consists of the following columns:

- **gender**: The gender of the student (Male/Female) 👨‍🎓👩‍🎓
- **race/ethnicity**: The ethnicity group of the student (Group A, B, C, D, E) 🌎
- **parental level of education**: The highest level of education completed by the student’s parent (High School, Associate’s Degree, Bachelor’s Degree, Master’s Degree, Some College) 🎓
- **lunch**: Type of lunch the student received (Standard or Free/Reduced) 🍔🥗
- **test preparation course**: Whether the student completed the test preparation course (Completed or Not Completed) 📚
- **math_score**: The student's final score in Mathematics (target variable) ➗
- **reading_score**: The student's score in Reading 📖
- **writing_score**: The student's score in Writing ✍️

---


## 📊 Model Overview

The machine learning model is trained using various features that influence student performance. The key steps include:

- **Data Preprocessing:** Handle missing values, encode categorical variables, and scale numerical values.

- **Model Training:** Train a regression model (e.g., Random Forest Regressor) using the processed data.

- **Model Evaluation:** Evaluate the model's performance using metrics like Mean Squared Error (MSE), R² Score, etc.

- **Prediction:** Make predictions based on the input data and display the result to the user.

---

## ⚙️ Technologies Used

- **Python** 🐍
- **pandas** 📊
- **scikit-learn** 🔍
- **Matplotlib** 📈
- **Jupyter Notebook** 📝

---

## 🗂️ Repository File Tree

```bash
Examination-Marks-Predictor/
├── notebook                          # Jupyter notebooks for data exploration & model training
│   ├── 1. EDA_STUDENT_PERFORMANCE.ipynb  # Exploratory Data Analysis (EDA) notebook
│   ├── 2. MODEL_TRAINING.ipynb           # Model training and evaluation notebook
│   └── data                              # Directory for dataset storage
│       └── stud.csv                      # Student performance dataset
|── src                                   # Source code for the project
|   ├── __init__.py                       # Marks src as a package
|   ├── components                         # Core project modules
|   │   ├── __init__.py                    # Marks components as a package
|   │   ├── data_ingestion.py              # Script to load and preprocess data
|   │   ├── data_transformation.py         # Handles feature transformation & scaling
|   │   ├── model_trainer.py                # Model training script
|   ├── exception.py                        # Custom exception handling
|   ├── logger.py                           # Logging setup for debugging & tracking
|   ├── pipeline                            # Pipeline for model training & prediction
|   │   ├── __init__.py                     # Marks pipeline as a package
|   │   ├── predict_pipeline.py             # Prediction pipeline script
|   │   ├── train_pipeline.py               # Model training pipeline script
|   └── utils.py                            # Utility functions (e.g., data processing, evaluation)
├── .gitignore                              # Specifies files to ignore in version control
├── README.md                               # Project documentation
├── requirments.txt                         # List of required dependencies
└── setup.py                                # Script for installing the package
                     # Project documentation (this file)

```

---

## 🔧 Installation & Setup

**1.** Clone the repository to your local machine:

   ```bash
   git clone https://github.com/AdityaBansal0123/Examination-Marks-Predictor.git
   cd Examination-Marks-Predictor
   ```

**2.** Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

**3.** Run the notebook or Python script to train and predict the student's performance.

---

## 🚀 How to Use

**1. Data Input:** The user can select or input values for the following features:

- **Gender** (Male/Female)
- **Race/Ethnicity** (Group A, B, C, D, E)
- **Parental Level of Education** (High School, Associate’s, Bachelor’s, Master’s, Some College)
- **Lunch Type** (Standard or Free/Reduced)
- **Test Preparation Course** (Completed or Not Completed)
- **Reading Score** (Enter score out of 100)
- **Writing Score** (Enter score out of 100)

**2. Prediction:** Based on the input, the model will predict the Math  Score of the student.

**3. Output:** The model will display the predicted math score (out of 100) as a result.

---

## 📞 Contact

- Email: [utsavraj911@outlook.com](utsavraj911@outlook.com)
