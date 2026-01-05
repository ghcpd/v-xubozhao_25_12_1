"""
Minimal demo to exercise key dependencies.
Run with an active virtual environment: `python demo.py`.
"""
from __future__ import annotations

import io
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from scipy import stats
from sklearn.linear_model import LogisticRegression
from fastapi import FastAPI
from fastapi.testclient import TestClient


def demo_numeric_stack():
    arr = np.array([1, 2, 3, 4], dtype=np.float64)
    mean = arr.mean()

    df = pd.DataFrame({"value": arr})
    df["zscore"] = stats.zscore(df["value"])

    # simple sklearn fit
    X = arr.reshape(-1, 1)
    y = np.array([0, 0, 1, 1])
    model = LogisticRegression(random_state=0).fit(X, y)
    pred = model.predict([[2.5]])[0]

    # matplotlib plot to buffer
    fig, ax = plt.subplots()
    ax.plot(df.index, df["value"], marker="o")
    ax.set_title("Demo Plot")
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)

    return {
        "mean": mean,
        "pred": int(pred),
        "plot_bytes": len(buf.getvalue()),
        "df_shape": df.shape,
    }


def demo_fastapi_stack():
    app = FastAPI()

    @app.get("/ping")
    def ping():
        return {"pong": True}

    client = TestClient(app)
    resp = client.get("/ping")
    resp.raise_for_status()
    data = resp.json()
    assert data == {"pong": True}
    return data


def main():
    results = demo_numeric_stack()
    api = demo_fastapi_stack()
    print("Numeric stack:", results)
    print("FastAPI stack:", api)


if __name__ == "__main__":
    main()
