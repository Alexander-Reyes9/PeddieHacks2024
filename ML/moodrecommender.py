#Possible approach
#Randomly compare user song to a song in the Dataset
#If sound similar, compare to other songs to make sure it fits the right mood. 
#Then find closest match
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# Load the dataset

#Remember to change this...
data = pd.read_csv('/fs/student/alexander_reyes/Desktop/ML/music_dataset.csv')
print(data.head())  # Display the first few rows
print(data.info())  # Get information about data types and missing values
print(data.describe())  # Statistical summary of numerical columns


