<!--
Thank you for checking out the Cancer Prediction Using Ensemble Methods project.
If you have any suggestions or feedback, feel free to reach out or open an issue.

Don't forget to connect with me on LinkedIn ;)
-->
<div align="center">

  <img src="https://cdn-icons-png.flaticon.com/512/919/919852.png" alt="Python Logo" width="80" height="auto" />
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7IJhNVZ2UNFUlsJoPlVH3I_xuPqBVTa1GRA&s" alt="Scikit-learn Logo" width="80" height="auto" />
  <img src="https://ih1.redbubble.net/image.5124540665.7259/st,small,507x507-pad,600x600,f8f8f8.u1.jpg" alt="Pandas Logo" width="80" height="auto" />
  <h1>Cancer Prediction Using Ensemble Methods</h1>
  
  <p>
    A Python project demonstrating cancer prediction using various ensemble machine learning methods.
  </p>
  
<!-- Badges -->
<p>
  <a href="https://github.com/medhiblk/All-My-Projects/graphs/contributors">
    <img src="https://img.shields.io/badge/contributors-1-brightgreen" alt="contributors" />
  </a>
  <a href="https://github.com/medhiblk/All-My-Projects/commits/main">
    <img src="https://img.shields.io/github/last-commit/medhiblk/All-My-Projects" alt="last update" />
  </a>
  <a href="https://www.linkedin.com/in/medhi-balouka-5a5342189/">
    <img src="https://img.shields.io/badge/LinkedIn-Medhi%20Balouka-blue" alt="LinkedIn" />
  </a>
</p>
   
<h4>
    <a href="https://github.com/medhiblk/All-My-Projects/tree/main/Advanced%20ML-Cancer%20Prediction">View Project</a>
  <span> · </span>
    <a href="https://github.com/medhiblk/All-My-Projects/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/medhiblk/All-My-Projects/issues/">Request Feature</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->
# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
  * [Screenshots](#camera-screenshots)
  * [Features](#dart-features)
- [Installation](#gear-installation)
- [Usage](#eyes-usage)
- [Model Overview](#chart_with_upwards_trend-model-overview)
- [Architecture](#house-architecture)
- [Contributing](#wave-contributing)
- [License](#warning-license)
- [Contact](#handshake-contact)
- [Acknowledgements](#gem-acknowledgements)

<!-- About the Project -->
## :star2: About the Project

This project uses various ensemble methods to predict whether a patient has cancer based on medical data. It leverages models like Random Forest, AdaBoost, and Stacking to improve the prediction accuracy.

<!-- Screenshots -->
### :camera: Screenshots

<div align="center"> 
  <img src="https://placehold.co/600x400?text=Your+Screenshot+here" alt="screenshot" />
</div>

<!-- Features -->
### :dart: Features

- Data preprocessing including handling missing values, encoding, and scaling.
- Implementation of multiple models: Decision Tree, Random Forest, AdaBoost, and Stacking.
- Evaluation metrics for model performance including accuracy, precision, recall, and F1-score.

## :gear: Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/medhiblk/All-My-Projects.git
    cd "All-My-Projects/Advanced ML-Cancer Prediction"
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

<!-- Usage -->
## :eyes: Usage

1. Place the `CancerPrediction.csv` file in the same directory as `Sklearn-CancerPrediction.py`.
2. Run the script:
    ```bash
    python Sklearn-CancerPrediction.py
    ```
3. The script will preprocess the data, train the models, and display evaluation metrics.

<!-- Model Overview -->
## :chart_with_upwards_trend: Model Overview

### Decision Tree
A simple model that splits the dataset into different branches to make decisions. It serves as the baseline model.

<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/5139/5139787.png" alt="Decision Tree Icon" width="100" height="auto" />
</div>

### Random Forest
An ensemble method using multiple decision trees. It improves accuracy by averaging the predictions of several trees.

<div align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXI9mwWSorpzKPxiF8o7nMiMfCvF8-1UtCHA&s" alt="Random Forest Icon" width="100" height="auto" />
</div>

### AdaBoost
A boosting method that combines weak learners to create a strong classifier. Focuses on instances that previous models classified incorrectly.

<div align="center">
  <img src="https://miro.medium.com/v2/resize:fit:1200/1*tLUhrb27BKMtXAXRfy15Vw.png" alt="AdaBoost Schema" width="100%" height="auto" />
</div>

### Stacking
An advanced ensemble method that combines the predictions of multiple models (Random Forest, AdaBoost, Decision Tree) using a meta-learner (Logistic Regression) to enhance prediction accuracy.

<div align="center">
  <img src="https://your-image-link-for-stacking.png" alt="Stacking Icon" width="100" height="auto" />
</div>

<!-- Architecture -->
## :house: Architecture
The project is built around a single Python script, `Sklearn-CancerPrediction.py`, which handles data loading, preprocessing, model training, and evaluation. The script is designed to be modular, allowing for easy adaptation to other datasets or model types.

<!-- Contributing -->
## :wave: Contributing
At this time, this project is developed and maintained solely by Medhi Balouka. Contributions are not being accepted, but feel free to reach out for any inquiries or collaboration ideas.

<!-- License -->
## :warning: License
This project is licensed under TBS Education. For more details, please visit TBS Education.

<!-- Contact -->
## :handshake: Contact
Medhi Balouka - [LinkedIn](https://www.linkedin.com/in/medhi-balouka-5a5342189/)

<!-- Acknowledgements -->
## :gem: Acknowledgements
This project was developed as part of my coursework at TBS Education.
Special thanks to the open-source community for providing the tools and libraries used in this project.
