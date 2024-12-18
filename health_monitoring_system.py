import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import joblib

class HealthMonitoringSystem:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.data = None
        self.model = None

    def load_data(self):
        self.data = pd.read_csv(self.dataset_path)
        print("Data loaded successfully.")
    
    def preprocess_data(self):
        self.data.fillna(method='ffill', inplace=True)
        self.data['timestamp'] = pd.to_datetime(self.data['timestamp'])
        self.data['hour'] = self.data['timestamp'].dt.hour

        scaler = StandardScaler()
        self.data[['heart_rate', 'blood_pressure', 'glucose_level']] = scaler.fit_transform(
            self.data[['heart_rate', 'blood_pressure', 'glucose_level']]
        )

    def train_model(self):
        X = self.data[['hour', 'heart_rate', 'blood_pressure', 'glucose_level']]
        y = self.data['health_status']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))

    def generate_health_report(self):
        if self.model:
            print("Generating health report...")
            feature_importances = self.model.feature_importances_
            features = ['hour', 'heart_rate', 'blood_pressure', 'glucose_level']
            
            sns.barplot(x=feature_importances, y=features)
            plt.title("Feature Importance for Health Prediction")
            plt.xlabel("Importance")
            plt.ylabel("Features")
            plt.show()

    def save_model(self, filename='model.pkl'):
        joblib.dump(self.model, filename)
        print(f"Model saved as {filename}")

dataset_path = "health_data.csv"  # Dummy dataset path
health_monitor = HealthMonitoringSystem(dataset_path)
health_monitor.load_data()
health_monitor.preprocess_data()
health_monitor.train_model()
health_monitor.generate_health_report()
health_monitor.save_model()
