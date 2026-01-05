"""
Simple demo: train DecisionTree on Iris and make a prediction
"""
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier


def run_demo():
    data = load_iris()
    X, y = data.data, data.target
    model = DecisionTreeClassifier(random_state=0)
    model.fit(X[:100], y[:100])
    pred = model.predict([X[100]])
    print('Predicted:', pred[0])


if __name__ == '__main__':
    run_demo()
