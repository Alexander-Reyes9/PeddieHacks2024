#New Idea
# What if score both the lyrics of a song and melody of a song to get emotion
# Might be better though to use lyrics as a prime factor???
# Maybe for songs w no lyrics, judge based on sound??
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
import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset

#Remember to change this...
with open('link.txt', 'r') as file:
    # Read the entire contents of the file as a string
    CSVfile = file.read() 
data = pd.read_csv(CSVfile, sep=';', header=0, encoding = 'utf-16',on_bad_lines = 'skip')
#print(data.head(20))  # Display the first few rows
#print(data.info())  # Get information about data types and missing values
#print(data.describe())  # Statistical summary of numerical columns
def extract_features(file_name):
    # Load the audio file
    y, sr = librosa.load(file_name)

    # Extract features
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    mel = librosa.feature.melspectrogram(y=y, sr=sr)
    contrast = librosa.feature.spectral_contrast(y=y, sr=sr)

    # Combine the features into a single array
    features = np.hstack([np.mean(mfccs, axis=1),                                                                                                                             np.mean(chroma, axis=1),
                          np.mean(mel, axis=1),
                          np.mean(contrast, axis=1)])
    return features
features = []
for file_name in data['Filename']:
    print(file_name)
    features.append(extract_features('Audio/' + str(file_name)))
print(features)
# Convert the features and labels to a DataFrame
X = np.array(features[:630])
output=pd.read_csv('categories.txt')
y = output.values[:630]
y = y.ravel()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize the model
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
#print(classification_report(y_test, y_pred, zero_division = 0))