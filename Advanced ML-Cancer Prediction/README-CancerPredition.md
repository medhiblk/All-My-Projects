# Cancer Prediction Using Ensemble Methods

![Project Logo](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.vectorstock.com%2Froyalty-free-vector%2Fbig-data-healthcare-concept-vector-29662550&psig=AOvVaw0K9EoWypQh5WskxgTL40FN&ust=1723628945364000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKjUkKzY8YcDFQAAAAAdAAAAABAE)

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/user/repo/actions)
[![TBS Education](https://img.shields.io/badge/License-TBS%20Education-blue.svg)](https://www.tbs-education.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Medhi%20Balouka-blue)](https://www.linkedin.com/in/medhi-balouka-5a5342189/)

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Model Overview](#model-overview)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Overview

This project demonstrates cancer prediction using ensemble methods in Python. The script `cancer-prediction.py` loads data from `CancerPrediction.csv`, preprocesses it, and applies various ensemble techniques like Bagging with Random Forest, Boosting with AdaBoost, and Stacking to predict whether a patient has cancer. The objective is to enhance the accuracy of predictions by leveraging the strengths of different models.

---

## Features
- **Single Script Implementation:** All functionality is encapsulated in a single Python script (`cancer-prediction.py`).
- **Data Preprocessing:** Handles missing values, encodes categorical data, and scales features.
- **Multiple Models:** Includes Decision Tree, Random Forest, AdaBoost, and Stacking classifiers.
- **Evaluation Metrics:** Uses metrics such as accuracy, precision, recall, and F1-score to evaluate model performance.
- **Simple Setup:** Requires only one Python file and one dataset file to run the entire project.

---

## Installation

### Prerequisites
- Python 3.7+
- pip

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/user/repo.git
    cd repo
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
   
   *Note: If the `requirements.txt` file is not provided, install the necessary libraries manually:*
    ```bash
    pip install pandas scikit-learn
    ```

---

## Usage

1. Place the `CancerPrediction.csv` file in the same directory as `cancer-prediction.py`.
2. Run the script:
    ```bash
    python cancer-prediction.py
    ```
3. The script will preprocess the data, train the models, and display evaluation metrics.

---

## Screenshots

### Data Preprocessing
![Preprocessing](https://example.com/preprocessing.png)

### Model Training
![Training](https://example.com/training.png)

### Model Evaluation
![Evaluation](https://example.com/evaluation.png)

---

## Project Structure

```bash
├── cancer-prediction.py        # Main Python script
├── CancerPrediction.csv        # Dataset
├── README.md                   # Project README
└── requirements.txt            # Python dependencies

---

## Model Overview

### Decision Tree
A simple model that splits the dataset into different branches to make decisions. It serves as the baseline model.

### Random Forest
An ensemble method using multiple decision trees. It improves accuracy by averaging the predictions of several trees.

### AdaBoost
A boosting method that combines weak learners to create a strong classifier. Focuses on instances that previous models classified incorrectly.

### Stacking
An advanced ensemble method that combines the predictions of multiple models (Random Forest, AdaBoost, Decision Tree) using a meta-learner (Logistic Regression) to enhance prediction accuracy.

---

### Architecture
The project is built around a single Python script, cancer-prediction.py, which handles data loading, preprocessing, model training, and evaluation. The script is designed to be modular, allowing for easy adaptation to other datasets or model types.

---

##Contributing
At this time, this project is developed and maintained by me, Medhi Balouka.[![LinkedIn](https://img.shields.io/badge/LinkedIn-Medhi%20Balouka-blue)](https://www.linkedin.com/in/medhi-balouka-5a5342189/). Contributions are not being accepted, but feel free to reach out for any inquiries or collaboration ideas.

---

## License
This project is licensed under TBS Education. For more details, please visit TBS Education.

---
##Acknowledgements
*This project was developed as part of my coursework at TBS Education.
*Special thanks to the open-source community for providing the tools and libraries used in this project.


