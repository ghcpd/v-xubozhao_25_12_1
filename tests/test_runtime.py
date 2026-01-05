#!/usr/bin/env python3
"""
Runtime Functionality Tests for Backend Analytics Service

Tests validate that all core dependencies are functional and compatible.
Uses pytest for automated testing.
"""

import sys
import pytest


class TestNumpyFunctionality:
    """Test numpy installation and core operations."""

    def test_numpy_import(self):
        """Verify numpy can be imported."""
        import numpy as np
        assert np.__version__
        assert hasattr(np, 'array')

    def test_numpy_array_operations(self):
        """Test basic numpy array operations."""
        import numpy as np
        
        arr = np.array([1, 2, 3, 4, 5])
        assert arr.shape == (5,)
        assert arr.sum() == 15
        assert arr.mean() == 3.0

    def test_numpy_linear_algebra(self):
        """Test numpy linear algebra operations."""
        import numpy as np
        
        matrix = np.array([[1, 2], [3, 4]])
        result = np.linalg.det(matrix)
        assert abs(result - (-2.0)) < 1e-10


class TestPandasFunctionality:
    """Test pandas installation and core operations."""

    def test_pandas_import(self):
        """Verify pandas can be imported."""
        import pandas as pd
        assert pd.__version__
        assert hasattr(pd, 'DataFrame')

    def test_pandas_dataframe_creation(self):
        """Test DataFrame creation and basic operations."""
        import pandas as pd
        
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        assert df.shape == (3, 2)
        assert list(df.columns) == ['A', 'B']

    def test_pandas_groupby(self):
        """Test pandas groupby operations."""
        import pandas as pd
        
        df = pd.DataFrame({
            'category': ['X', 'Y', 'X', 'Y'],
            'value': [10, 20, 30, 40]
        })
        grouped = df.groupby('category')['value'].sum()
        assert grouped['X'] == 40
        assert grouped['Y'] == 60


class TestScikitLearnFunctionality:
    """Test scikit-learn installation and core operations."""

    def test_sklearn_import(self):
        """Verify scikit-learn can be imported."""
        import sklearn
        assert sklearn.__version__
        from sklearn.datasets import load_iris
        assert callable(load_iris)

    def test_sklearn_model_training(self):
        """Test training a simple classifier."""
        from sklearn.datasets import load_iris
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LogisticRegression
        
        X, y = load_iris(return_X_y=True)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        model = LogisticRegression(max_iter=200)
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        
        assert score > 0.8, f"Model accuracy too low: {score}"

    def test_sklearn_preprocessing(self):
        """Test sklearn preprocessing."""
        from sklearn.preprocessing import StandardScaler
        import numpy as np
        
        data = np.array([[1, 2], [3, 4], [5, 6]])
        scaler = StandardScaler()
        scaled = scaler.fit_transform(data)
        
        assert scaled.shape == (3, 2)
        assert abs(scaled.mean()) < 1e-10  # Should be ~0


class TestScipyFunctionality:
    """Test scipy installation and core operations."""

    def test_scipy_import(self):
        """Verify scipy can be imported."""
        import scipy
        assert scipy.__version__
        from scipy import stats
        assert hasattr(stats, 'norm')

    def test_scipy_statistics(self):
        """Test scipy statistical functions."""
        from scipy import stats
        import numpy as np
        
        data = np.random.normal(loc=0, scale=1, size=1000)
        result = stats.normaltest(data)
        assert hasattr(result, 'pvalue')

    def test_scipy_optimization(self):
        """Test scipy optimization."""
        from scipy.optimize import minimize
        import numpy as np
        
        def objective(x):
            return (x - 2) ** 2 + 3
        
        result = minimize(objective, x0=0)
        assert result.success
        assert abs(result.x[0] - 2.0) < 1e-5


class TestMatplotlibFunctionality:
    """Test matplotlib installation and core operations."""

    def test_matplotlib_import(self):
        """Verify matplotlib can be imported."""
        import matplotlib
        assert matplotlib.__version__
        import matplotlib.pyplot as plt
        assert hasattr(plt, 'plot')

    def test_matplotlib_figure_creation(self):
        """Test creating matplotlib figures."""
        import matplotlib.pyplot as plt
        import numpy as np
        
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        
        fig, ax = plt.subplots()
        ax.plot(x, y)
        assert fig is not None
        assert ax is not None
        plt.close(fig)

    def test_matplotlib_backend(self):
        """Test matplotlib backend configuration."""
        import matplotlib
        backend = matplotlib.get_backend().lower()
        # On Windows without display, tkagg is common; Agg is also acceptable
        assert backend in ['agg', 'tkagg', 'tkinter'], f"Unexpected backend: {backend}"


class TestFastAPIFunctionality:
    """Test fastapi installation and core operations."""

    def test_fastapi_import(self):
        """Verify fastapi can be imported."""
        from fastapi import FastAPI
        assert callable(FastAPI)

    def test_fastapi_app_creation(self):
        """Test creating a FastAPI application."""
        from fastapi import FastAPI
        
        app = FastAPI()
        assert hasattr(app, 'get')
        assert hasattr(app, 'post')

    def test_fastapi_route(self):
        """Test creating a simple FastAPI route."""
        from fastapi import FastAPI
        from fastapi.testclient import TestClient
        
        app = FastAPI()
        
        @app.get("/test")
        def test_endpoint():
            return {"status": "ok"}
        
        client = TestClient(app)
        response = client.get("/test")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}


class TestUvicornFunctionality:
    """Test uvicorn installation and core operations."""

    def test_uvicorn_import(self):
        """Verify uvicorn can be imported."""
        import uvicorn
        assert uvicorn.__version__
        assert hasattr(uvicorn, 'run')

    def test_uvicorn_config(self):
        """Test uvicorn configuration object."""
        from uvicorn.config import Config
        from fastapi import FastAPI
        
        app = FastAPI()
        config = Config(app=app, host="127.0.0.1", port=8000)
        assert config.host == "127.0.0.1"
        assert config.port == 8000


class TestPytestFunctionality:
    """Test pytest and testing infrastructure."""

    def test_pytest_version(self):
        """Verify pytest can be imported."""
        import pytest as pt
        assert pt.__version__
        version_parts = pt.__version__.split('.')
        major_version = int(version_parts[0])
        assert major_version >= 7, "Pytest version too old"

    def test_pytest_markers(self):
        """Test pytest marker functionality."""
        import pytest as pt
        
        # Create a simple test that uses markers
        @pt.mark.parametrize("x,y,expected", [
            (1, 2, 3),
            (2, 3, 5),
            (3, 4, 7),
        ])
        def parametrized_test(x, y, expected):
            assert x + y == expected
        
        # Verify marker was applied
        assert hasattr(parametrized_test, 'pytestmark')


class TestPytestCovFunctionality:
    """Test pytest-cov coverage plugin."""

    def test_pytest_cov_import(self):
        """Verify pytest-cov can be imported."""
        import pytest_cov
        assert hasattr(pytest_cov, 'plugin')


class TestDependencyCompatibility:
    """Test cross-library compatibility."""

    def test_numpy_pandas_compatibility(self):
        """Test numpy and pandas work together."""
        import numpy as np
        import pandas as pd
        
        arr = np.array([1, 2, 3, 4, 5])
        series = pd.Series(arr)
        assert len(series) == 5

    def test_pandas_sklearn_compatibility(self):
        """Test pandas and scikit-learn work together."""
        import pandas as pd
        from sklearn.preprocessing import StandardScaler
        
        df = pd.DataFrame({
            'feature1': [1, 2, 3],
            'feature2': [4, 5, 6]
        })
        
        scaler = StandardScaler()
        scaled = scaler.fit_transform(df)
        assert scaled.shape == (3, 2)

    def test_fastapi_pydantic_v2_compatibility(self):
        """Test FastAPI with Pydantic v2 support."""
        from fastapi import FastAPI
        from pydantic import BaseModel
        
        app = FastAPI()
        
        class Item(BaseModel):
            name: str
            price: float
        
        @app.post("/items/")
        def create_item(item: Item):
            return item
        
        assert hasattr(app, 'openapi')


class TestPythonVersion:
    """Test Python version compatibility."""

    def test_python_3_10_plus(self):
        """Verify Python 3.10+ is running."""
        major, minor = sys.version_info[:2]
        assert major == 3
        assert minor >= 10, f"Python 3.10+ required, got {major}.{minor}"


if __name__ == '__main__':
    # Run pytest programmatically
    exit_code = pytest.main([
        __file__,
        '-v',
        '--tb=short',
        '--color=yes',
        '-ra',
    ])
    sys.exit(exit_code)
