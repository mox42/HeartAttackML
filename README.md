# Heart Attack Prediction System

## Project Overview

The Heart Attack Prediction System is an interactive web application that predicts the likelihood of a heart attack based on user input. The system is built using machine learning algorithms and provides accurate and efficient heart attack predictions to improve early detection and prevention.

It was developed to address the need for accurate and efficient heart attack prediction systems that can aid healthcare providers in making informed decisions about patient care. By leveraging machine learning techniques, the system offers an accessible and reliable solution for heart attack risk assessment.

This System employs several popular machine learning algorithms, including Gradient Boosting, Decision Trees, Random Forest, Support Vector Machines, Naïve Bayes, and Logistic Regression. By trying multiple algorithms and evaluating their performance, the system selects the most suitable one for the given problem.

**Features of the project**
- User-friendly interface for inputting personal and medical information.
- Utilizes machine learning models to predict the probability of a heart attack.
- Provides insights and statistics about heart diseases and heart attacks.
- Contact section for user feedback and support.



## Steps
Key Features of the Heart Attack Prediction System
- **Data Collection:** The Dataset collected from Kaggle 1025 records with 14 features
- **Data Pre-processing:** Before training the machine learning models, the collected data is cleaned and processed to ensure it is suitable for analysis.
- **Feature Selection:** The system identifies important features from the pre-processed data that are relevant for predicting heart attacks.
- **Model Training and Validation:** The machine learning model is trained on the collected and pre-processed data and validated using suitable evaluation metrics.
- **Model Extraction and Deployment:** The trained model was extract using pickle and deplyoed into streamlit cloud service
  
## Feature Selection
The project uses the Forward Feature Selection method to select the most relevant features for heart attack prediction. It has been found to achieve the best accuracy with Gradient Boosting, with accuracy of 98.54%.

To enhance the system's accuracy and performance, four feature selection methods were tested: ANOVA, Correlation-Based (CFS), Mutual Information (MI), and Forward selection. The Forward Feature Selection method was found to achieve the best accuracy scores with Gradient Boosting.

## Deployment

The project is deployed as a web application using Streamlit. The application can be accessed at https://heartml.streamlit.app

## Contributors
- Dalia AlJahmani - GitHub [here](https://github.com/Dalia2810)
- Rahaf AlQura’an - GitHub [here](https://github.com/Rahafrsq)


## Contact
If you have any questions, feedback, or need support with the Heart Attack Prediction System, please feel free to contact me at mohammedqasem442@gmail.com


