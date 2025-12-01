import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pytest


def test_numpy_basic():
    arr = np.array([1, 2, 3])
    assert arr.sum() == 6


def test_pandas_basic():
    df = pd.DataFrame({'a': [1, 2, 2], 'b': [3, 4, 4]})
    grp = df.groupby('a').sum()
    assert 'b' in grp.columns


def test_scipy_stats():
    # basic use of stats
    rv = stats.norm(loc=0, scale=1)
    p = rv.pdf(0.0)
    assert p > 0


def test_matplotlib_plot(tmp_path):
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2], [0, 1, 4])
    out = tmp_path / "plot.png"
    fig.savefig(out)
    assert out.exists()


def test_sklearn_training():
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, random_state=0)
    model = DecisionTreeClassifier(random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    assert len(preds) == len(X_test)


def test_fastapi_endpoint():
    from fastapi import FastAPI
    from fastapi.testclient import TestClient

    app = FastAPI()

    @app.get('/ping')
    def ping():
        return {'ping': 'pong'}

    client = TestClient(app)
    r = client.get('/ping')
    assert r.status_code == 200
    assert r.json() == {'ping': 'pong'}


if __name__ == '__main__':
    # allow running as script for quick local checks
    pytest.main([__file__])
