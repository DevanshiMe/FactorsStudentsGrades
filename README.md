# Factors Affecting Students’ Grades

## Overview

This project investigates the **socio-economic, psychological, and lifestyle factors** that influence university students’ academic performance.
We use machine learning models to predict grades based on various attributes, and provide a simple **web-based UI** (Flask + HTML) for user interaction.


## 📊 Dataset

**Source:** `Factors_affecting_university_student_grades_dataset.csv`

### Features:

* **Numerical:** Age, Family Income, Attendance, Study Hours, Class Size, Sleep Patterns, Screen Time, Time Wasted on Social Media
* **Categorical:** Gender, Parental Education, Class Participation, Financial Status, Motivation, Stress Levels, Extracurricular Activities, Nutrition, Peer Group, etc.
* **Target:** Grades (final academic performance)

Preprocessing steps included:

* Handling duplicates and missing values
* Converting categorical variables
* Dropping irrelevant/redundant features


## 🤖 Models Implemented

* Logistic Regression
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)
* K-Nearest Neighbors (KNN)
* Naive Bayes (GaussianNB)
* Neural Networks (Keras Sequential Model)

Evaluation metrics: **Accuracy, Confusion Matrix, and Visualization (Plotly/Matplotlib).**


## 🌐 Web Application

The project includes a simple **Flask-based web UI**:

* `app.py` → Backend API for model inference
* `index.html` → Frontend form for inputting student details

Users can input relevant features and get a **predicted grade**.


## 📈 Results & Insights

* Random Forest and Neural Networks provided the most accurate results.
* Socio-economic and psychological factors (like **Parental Education, Motivation, Stress Levels**) had a strong correlation with student performance.
* Lifestyle attributes (e.g., **Sleep Patterns, Social Media Usage**) also influenced outcomes significantly.


