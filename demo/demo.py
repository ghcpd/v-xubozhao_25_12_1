"""
Minimal demo used by tests to validate runtime usage of key libraries:
- Uses numpy + pandas for data building
- Uses scikit-learn to fit a small logistic regression model on a toy dataset
- Returns a prediction array
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def build_sample_dataset(n_samples: int = 100) -> pd.DataFrame:
    """Create a simple two-class toy dataset."""
    rng = np.random.default_rng(seed=42)
    X = rng.normal(size=(n_samples, 3))
    y = (X[:, 0] + X[:, 1] * 0.5 > 0).astype(int)
    df = pd.DataFrame(X, columns=["f1", "f2", "f3"])
    df["target"] = y
    return df


def train_simple_model(df: pd.DataFrame):
    X = df[["f1", "f2", "f3"]].values
    y = df["target"].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    model = LogisticRegression(solver="liblinear", random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    return preds


def predict_sample(n_samples: int = 20) -> np.ndarray:
    df = build_sample_dataset(n_samples)
    return train_simple_model(df)


if __name__ == "__main__":
    print(predict_sample(10))
