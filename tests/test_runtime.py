import io
import sys
import os

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.tree import DecisionTreeClassifier

from fastapi.testclient import TestClient
from demo.demo_app import app, demo_process


def test_numpy_and_pandas_basic():
    arr = np.array([1, 2, 3, 4])
    assert arr.sum() == 10
    df = pd.DataFrame({"a": arr})
    assert df["a"].mean() == 2.5


def test_matplotlib_can_plot():
    plt.figure()
    plt.plot([0, 1, 2], [0, 1, 4])
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    assert buf.getbuffer().nbytes > 0


def test_scipy_stats():
    # normal cdf at 0 is 0.5
    val = stats.norm.cdf(0)
    assert abs(val - 0.5) < 1e-8


def test_sklearn_training_basic():
    X = [[0, 0], [1, 1]]
    y = [0, 1]
    clf = DecisionTreeClassifier(random_state=0)
    clf.fit(X, y)
    pred = clf.predict([[0.1, 0.1]])
    assert pred[0] in (0, 1)


def test_fastapi_demo_app():
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200 and r.json() == {"status": "ok"}
    r2 = client.get("/hello/Alice")
    assert r2.status_code == 200 and "Alice" in r2.json()["message"]


def test_demo_process_returns_dataframe():
    df = demo_process([1, 2, 3, 4])
    assert hasattr(df, 'to_dict')
    d = df.to_dict(orient="records")[0]
    assert d["sum"] == 10
