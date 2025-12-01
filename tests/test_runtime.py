import io
import os

os.environ.setdefault("MPLBACKEND", "Agg")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats, linalg
from sklearn.linear_model import LogisticRegression
from fastapi import FastAPI
from fastapi.testclient import TestClient
import uvicorn


def test_numpy_basic_ops():
    arr = np.array([1, 2, 3, 4], dtype=np.float64)
    assert arr.sum() == 10
    assert np.isclose(arr.mean(), 2.5)
    assert arr.dtype == np.float64


def test_pandas_dataframe_roundtrip():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert list(df.columns) == ["a", "b"]
    assert df.shape == (3, 2)
    # Verify describe works and returns expected columns
    desc = df.describe()
    assert "a" in desc.columns and "b" in desc.columns


def test_scipy_stats_and_linalg():
    data = np.array([1.0, 2.0, 3.0, 4.0])
    z = stats.zscore(data)
    assert np.isclose(z.mean(), 0, atol=1e-7)
    # simple linear system solve
    A = np.array([[3, 2], [1, 2]], dtype=float)
    b = np.array([5, 5], dtype=float)
    x = linalg.solve(A, b)
    assert np.allclose(A.dot(x), b)


def test_sklearn_logistic_regression():
    X = np.array([[1], [2], [3], [4]])
    y = np.array([0, 0, 1, 1])
    model = LogisticRegression(random_state=0).fit(X, y)
    pred = model.predict([[2.5]])[0]
    assert pred in (0, 1)


def test_matplotlib_headless_plot():
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2], [0, 1, 0])
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    assert buf.tell() > 0


def test_fastapi_ping():
    app = FastAPI()

    @app.get("/ping")
    def ping():  # pragma: no cover - trivial
        return {"pong": True}

    client = TestClient(app)
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.json() == {"pong": True}


def test_uvicorn_config_instantiation():
    # Ensure uvicorn can create a Config; we don't actually run the server here.
    app = FastAPI()
    config = uvicorn.Config(app, host="127.0.0.1", port=8000, log_level="info")
    assert config.app is app
