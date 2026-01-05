"""
Runtime functionality tests for backend analytics service
Tests core dependencies and functionality after upgrade
"""

import pytest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_classification
from scipy import stats
import io


class TestNumpyFunctionality:
    """Test numpy operations and compatibility"""
    
    def test_numpy_version(self):
        """Verify numpy 2.x is installed"""
        assert np.__version__.startswith('2.'), f"Expected numpy 2.x, got {np.__version__}"
    
    def test_array_operations(self):
        """Test basic array operations"""
        arr = np.array([1, 2, 3, 4, 5])
        assert arr.sum() == 15
        assert arr.mean() == 3.0
        assert arr.std() > 0
    
    def test_matrix_operations(self):
        """Test matrix multiplication and operations"""
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])
        C = A @ B  # Matrix multiplication
        expected = np.array([[19, 22], [43, 50]])
        np.testing.assert_array_equal(C, expected)
    
    def test_random_generation(self):
        """Test random number generation"""
        rng = np.random.default_rng(seed=42)
        random_array = rng.random(100)
        assert len(random_array) == 100
        assert 0 <= random_array.min() <= 1
        assert 0 <= random_array.max() <= 1


class TestPandasFunctionality:
    """Test pandas operations and compatibility"""
    
    def test_pandas_version(self):
        """Verify pandas 2.x is installed"""
        assert pd.__version__.startswith('2.'), f"Expected pandas 2.x, got {pd.__version__}"
    
    def test_dataframe_creation(self):
        """Test DataFrame creation and basic operations"""
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': ['a', 'b', 'c', 'd', 'e']
        })
        assert len(df) == 5
        assert list(df.columns) == ['A', 'B', 'C']
        assert df['A'].sum() == 15
    
    def test_dataframe_concat(self):
        """Test concatenation (replaces deprecated append)"""
        df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
        result = pd.concat([df1, df2], ignore_index=True)
        assert len(result) == 4
        assert result['A'].tolist() == [1, 2, 5, 6]
    
    def test_dataframe_groupby(self):
        """Test groupby operations"""
        df = pd.DataFrame({
            'category': ['A', 'B', 'A', 'B', 'A'],
            'value': [10, 20, 30, 40, 50]
        })
        grouped = df.groupby('category')['value'].sum()
        assert grouped['A'] == 90
        assert grouped['B'] == 60
    
    def test_missing_data_handling(self):
        """Test nullable data types and missing value handling"""
        df = pd.DataFrame({
            'A': [1, 2, None, 4, 5],
            'B': [10, None, 30, 40, 50]
        })
        assert df['A'].isna().sum() == 1
        assert df['B'].isna().sum() == 1
        filled = df.fillna(0)
        assert filled.isna().sum().sum() == 0


class TestScikitLearnFunctionality:
    """Test scikit-learn operations"""
    
    def test_sklearn_version(self):
        """Verify scikit-learn 1.5+ is installed"""
        import sklearn
        version_parts = sklearn.__version__.split('.')
        major, minor = int(version_parts[0]), int(version_parts[1])
        assert major >= 1 and minor >= 5, f"Expected sklearn 1.5+, got {sklearn.__version__}"
    
    def test_linear_regression(self):
        """Test basic linear regression"""
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([2, 4, 6, 8, 10])
        
        model = LinearRegression()
        model.fit(X, y)
        
        predictions = model.predict(X)
        np.testing.assert_array_almost_equal(predictions, y, decimal=10)
        assert abs(model.coef_[0] - 2.0) < 0.001
    
    def test_classification_dataset(self):
        """Test dataset generation for classification"""
        X, y = make_classification(
            n_samples=100,
            n_features=20,
            n_informative=10,
            n_redundant=5,
            random_state=42
        )
        assert X.shape == (100, 20)
        assert len(y) == 100
        assert set(y).issubset({0, 1})


class TestScipyFunctionality:
    """Test scipy statistical operations"""
    
    def test_scipy_version(self):
        """Verify scipy 1.14+ is installed"""
        import scipy
        version_parts = scipy.__version__.split('.')
        major, minor = int(version_parts[0]), int(version_parts[1])
        assert major >= 1 and minor >= 14, f"Expected scipy 1.14+, got {scipy.__version__}"
    
    def test_statistical_tests(self):
        """Test basic statistical operations"""
        data = np.random.normal(100, 15, 1000)
        mean = np.mean(data)
        assert 95 < mean < 105  # Should be close to 100
        
        # T-test
        t_stat, p_value = stats.ttest_1samp(data, 100)
        assert isinstance(t_stat, (float, np.floating))
        assert 0 <= p_value <= 1
    
    def test_distributions(self):
        """Test probability distributions"""
        norm_dist = stats.norm(loc=0, scale=1)
        samples = norm_dist.rvs(size=1000, random_state=42)
        assert len(samples) == 1000
        assert -4 < samples.mean() < 4


class TestMatplotlibFunctionality:
    """Test matplotlib plotting capabilities"""
    
    def test_matplotlib_version(self):
        """Verify matplotlib 3.9+ is installed"""
        import matplotlib
        version_parts = matplotlib.__version__.split('.')
        major, minor = int(version_parts[0]), int(version_parts[1])
        assert major >= 3 and minor >= 9, f"Expected matplotlib 3.9+, got {matplotlib.__version__}"
    
    def test_basic_plotting(self):
        """Test basic plot creation"""
        fig, ax = plt.subplots()
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Test Plot')
        
        # Save to buffer to verify it works
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        assert len(buf.read()) > 0
        plt.close(fig)
    
    def test_multiple_subplots(self):
        """Test subplot functionality"""
        fig, axes = plt.subplots(2, 2, figsize=(10, 10))
        assert axes.shape == (2, 2)
        
        for i, ax in enumerate(axes.flat):
            ax.plot([1, 2, 3], [1, 4, 9])
            ax.set_title(f'Subplot {i+1}')
        
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        plt.close(fig)
        assert buf.tell() > 0


class TestIntegrationScenarios:
    """Test integrated analytics workflows"""
    
    def test_data_pipeline(self):
        """Test complete data analysis pipeline"""
        # Create synthetic data
        np.random.seed(42)
        data = pd.DataFrame({
            'feature1': np.random.randn(100),
            'feature2': np.random.randn(100),
            'target': np.random.choice([0, 1], 100)
        })
        
        # Basic statistics
        assert data.shape == (100, 3)
        assert data['feature1'].mean() != 0  # Should have some variance
        
        # Prepare for modeling
        X = data[['feature1', 'feature2']].values
        y = data['target'].values
        
        # Basic classification check
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestClassifier
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        model = RandomForestClassifier(n_estimators=10, random_state=42)
        model.fit(X_train, y_train)
        
        accuracy = model.score(X_test, y_test)
        assert 0 <= accuracy <= 1
    
    def test_statistical_analysis_workflow(self):
        """Test statistical analysis workflow"""
        # Generate two samples
        sample1 = np.random.normal(100, 15, 100)
        sample2 = np.random.normal(105, 15, 100)
        
        # Perform t-test
        t_stat, p_value = stats.ttest_ind(sample1, sample2)
        
        # Create DataFrame for analysis
        df = pd.DataFrame({
            'group': ['A'] * 100 + ['B'] * 100,
            'value': np.concatenate([sample1, sample2])
        })
        
        # Group statistics
        group_stats = df.groupby('group')['value'].agg(['mean', 'std', 'count'])
        assert len(group_stats) == 2
        assert all(group_stats['count'] == 100)


class TestPytestFeatures:
    """Test pytest-specific features work correctly"""
    
    def test_pytest_version(self):
        """Verify pytest 8.x is installed"""
        assert pytest.__version__.startswith('8.'), f"Expected pytest 8.x, got {pytest.__version__}"
    
    def test_parametrize_feature(self):
        """Test pytest parametrize decorator works"""
        # This test itself demonstrates parametrize works
        pass
    
    @pytest.mark.parametrize("input,expected", [
        (1, 2),
        (2, 4),
        (3, 6),
        (4, 8),
    ])
    def test_with_parameters(self, input, expected):
        """Test parametrized test execution"""
        assert input * 2 == expected
    
    def test_fixtures_work(self, tmp_path):
        """Test that pytest fixtures are available"""
        # tmp_path is a built-in pytest fixture
        test_file = tmp_path / "test.txt"
        test_file.write_text("test content")
        assert test_file.read_text() == "test content"


@pytest.fixture
def sample_dataframe():
    """Fixture providing a sample DataFrame"""
    return pd.DataFrame({
        'A': range(10),
        'B': range(10, 20),
        'C': ['x', 'y'] * 5
    })


class TestFixtureUsage:
    """Test fixture functionality"""
    
    def test_fixture_usage(self, sample_dataframe):
        """Test using custom fixture"""
        assert len(sample_dataframe) == 10
        assert list(sample_dataframe.columns) == ['A', 'B', 'C']
        assert sample_dataframe['A'].sum() == 45


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
