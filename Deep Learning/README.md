<div align="center">
  <img src="https://cdn.svgator.com/images/2022/11/Chart-run-cycle.gif" alt="Banner GIF" width="100%" />
</div>

# 🎵 Acoustic Features Modeling

## 📝 About the Project
This project focuses on predicting the emotional class (e.g., sad, angry, happy, relaxed) of a person based on acoustic features using neural network models. The primary goal is to use various features from the dataset to determine the emotion, thus modeling the acoustic characteristics associated with different emotional states.

<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/1157/1157030.png" alt="Neural Network Icon" width="100" height="auto" />
  <h2>Acoustic Features Modeling Using Neural Networks</h2>
  <p>A Python project to model and predict emotions based on acoustic features using deep learning techniques.</p>
</div>

## 🚀 Project Objective
To create a neural network model that predicts the emotional state of an individual based on acoustic features. The project involves the following steps:

- **Data Preprocessing:** Handling missing values, encoding labels, and splitting the dataset into training and validation sets.
- **Model Development:** Building and training multiple neural network models with different architectures.
- **Model Evaluation:** Comparing model performance in terms of accuracy and loss.

## 🛠️ Installation
To set up the project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/medhiblk/All-My-Projects.git
cd "All-My-Projects/Acoustic Features Modeling"
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## 🎨 Features
* Data Preprocessing: Includes handling of missing values, label encoding, and scaling.
* Neural Network Models: Multiple architectures with varying complexities, including models with single and multiple hidden layers.
* Performance Metrics: Training and validation accuracy, as well as loss comparison across models.


## 🧠 Model Overview
### Model 1: Single Hidden Layer
A basic neural network with a single hidden layer consisting of 4 neurons, using ReLU activation for the hidden layer and softmax for the output layer.

<div align="center">
  <img src="DeepLearning - Images/Model1-Accuracy.png" alt="Model 1 Accuracy" width="50%" height="auto" />
</div>

### Model 2: Two Hidden Layers with LeakyReLU and ReLU
A more complex model featuring two hidden layers. The first hidden layer uses LeakyReLU activation, and the second uses ReLU.

<div align="center">
  <img src="DeepLearning - Images/Model2-accuracy.png" alt="Model 2 Accuracy" width="50%" height="auto" />
</div>

### Model 3: Two Hidden Layers with Mixed Activation Functions
This model combines LeakyReLU in the first hidden layer with a sigmoid activation in the second, aiming to explore the effects of different activation functions on performance.

<div align="center">
  <img src="DeepLearning - Images/Model3-Accuracy.png" alt="Model 3 Accuracy" width="50%" height="auto" />
</div>

## 📊 Model Evaluation
Performance across models is evaluated using training and validation accuracy, as well as loss comparisons. Below are the results:

## Training & Validation Accuracy
* Model 1: Basic Accuracy
* Model 2: Improved Performance with Two Layers
* Model 3: Experimentation with Mixed Activations
<div align="center">
  <img src="DeepLearning - Images/Model-Accuracy-Comparaison.png" alt="Validation Accuracy Comparison" width="50%" height="auto" />
</div>

### Loss Analysis
The project analyzes both training and validation loss across the models to identify overfitting and underfitting scenarios.

<div align="center">
  <img src="DeepLearning - Images/training-loss-comparaison.png" alt="Loss Comparison" width="50%" height="auto" />
</div>
<div align="center">
  <img src="DeepLearning - Images/ValisationLoss-comparaison.png" alt="Validation Loss Comparison" width="50%" height="auto" />
</div>




## 🎯 Conclusion & Future Work
The models developed in this project currently show limited accuracy. Future work will involve refining these models by tuning hyperparameters, experimenting with different architectures, and possibly integrating additional features or techniques to improve performance.

---

# 📬 Contact
<p align="left">
  <img src="Images/372102050_LINKEDIN_ICON_TRANSPARENT_400.gif" alt="LinkedIn" width="40" style="vertical-align: middle;"/>
  <span style="font-size: 18px; vertical-align: middle;">
    <a href="https://www.linkedin.com/in/medhi-balouka-5a5342189/" style="text-decoration: none; color: black;">Follow me on LinkedIn</a>
  </span>
</p>
---

# 🔗 Learn More
For detailed insights and continued updates on this project, stay connected on GitHub.
