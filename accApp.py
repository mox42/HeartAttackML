import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import GridSearchCV
import warnings
warnings.filterwarnings("ignore")
def Accapp_one():
    st.write("""
    # Explore different classifier and datasets
    Which one is the best?
    """)
    classifier_name = st.sidebar.selectbox(
        'Select classifier',
        ('Logistic Regression', 'Decision Tree', 'Random Forest', 'Gradient Boosting'))
    dataset_name = st.sidebar.selectbox(
        'Select dataset',
        ('heart', 'heart1025'))
     # Import data
    if dataset_name == 'heart':
        df = pd.read_csv('Model_datasets/heart.csv')
    elif dataset_name == 'heart1025':
        df = pd.read_csv('Model_datasets/heart1025.csv')
        
    df.drop_duplicates(keep='first', inplace=True)
    # Define X and Y
    x = df.drop(labels=['output'], axis=1) # features 
    y = df['output'] # target
    scaler = MinMaxScaler() # Feature Scaling
    x = scaler.fit_transform(x)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0) # Data splitting 
    def get_classifier(clf_name):
        if clf_name == 'Logistic Regression':
            clf = LogisticRegression(random_state=0)
        elif clf_name == 'Decision Tree':
            clf = DecisionTreeClassifier(random_state=24)
        elif clf_name == 'Random Forest':
            clf = RandomForestClassifier(random_state=24)
        elif clf_name == 'Gradient Boosting':
            clf = GradientBoostingClassifier(n_estimators=100, random_state=123)
        return clf
    clf = get_classifier(classifier_name)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    st.write(f"Classifier = {classifier_name}")
    st.write(f"Dataset = {dataset_name}")
    st.write(f"Accuracy = {accuracy}")
     # Plotting Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    class_label = ["High-risk", "Low-risk"]
    df_cm = pd.DataFrame(cm, index=class_label, columns=class_label)
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.heatmap(df_cm, annot=True, cmap='Reds', linewidths=2, fmt='d', ax=ax)
    ax.set_title("Confusion Matrix")
    ax.set_xlabel("Predicted Values")
    ax.set_ylabel("Actual Values")
    st.pyplot(fig)
    return fig