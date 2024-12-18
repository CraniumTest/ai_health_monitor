import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

class HealthPredictor:
    def __init__(self):
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(Dense(64, input_dim=10, activation='relu'))  # Assuming 10 input features
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))  # Binary classification
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train, epochs=10, batch_size=16, validation_data=(X_test, y_test))

    def predict(self, data):
        return self.model.predict(np.array(data))
