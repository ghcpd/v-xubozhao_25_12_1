import importlib
import sys

import numpy as np
import pandas as pd
import pytest

from demo.demo import predict_sample


def test_numpy_basic():
    a = np.array([1, 2, 3])
    assert a.sum() == 6


def test_pandas_basic():
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert df["a"].mean() == pytest.approx(2.0)


def test_sklearn_model_runs():
    preds = predict_sample(50)
    assert hasattr(preds, "shape")
    assert len(preds) > 0


def test_fastapi_minimal():
    fastapi = importlib.import_module("fastapi")
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/ping")
    def ping():
        return {"ping": "pong"}

    # minimal behavior check: has routes
    assert any(r.path == "/ping" for r in app.routes)


def test_uvicorn_import():
    uvicorn = importlib.import_module("uvicorn")
    assert hasattr(uvicorn, "run")


def test_matplotlib_backend():
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([0, 1], [0, 1])
    # not saving; just ensure we can draw
    plt.close(fig)


def test_scipy_stats():
    scipy = importlib.import_module("scipy")
    from scipy import stats

    x = stats.norm.pdf(0.0, 0.0, 1.0)
    assert pytest.approx(0.398942, rel=1e-3) == x


# Ensure pytest itself is at least v8 for modern features
def test_pytest_version():
    import pkg_resources

    ver = pkg_resources.get_distribution("pytest").version
    major = int(ver.split(".")[0])
    assert major >= 8
