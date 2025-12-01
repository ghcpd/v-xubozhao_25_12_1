# Dependency upgrade summary

## Before → After

| Package | Before | After | Justification |
|---|---:|---:|---|
| numpy | 1.18.0 | 1.25.2 | Backported performance, security fixes, and Python 3.10 compatibility; aligns with scikit-learn/pandas expectations.
| pandas | 1.1.5 | 2.1.3 | Major pandas 2.x stabilizations and support for Python 3.10+. Be aware of some API deprecations for .ix, .sort etc.
| scikit-learn | 0.24.1 | 1.2.2 | Major upgrade: 1.x improves algorithms and provides fixes; some API changes (e.g., default parameters) may require code review for model behavior.
| scipy | 1.5.2 | 1.11.1 | Updated numerical libraries and bug fixes; compatible with new numpy.
| matplotlib | 3.3.2 | 3.8.1 | Supports modern backends and improved rendering with newer numpy.
| pytest | 5.4.3 | 7.4.0 | Required for Python 3.10 compatibility and newer plugin ecosystem.
| fastapi | 0.63.0 | 0.95.2 | FastAPI matured with new features and security fixes; compatibility with Starlette changes.
| uvicorn | 0.13.3 | 0.22.0 | Updated ASGI server with security and performance improvements.

## Notes & Breaking changes
- scikit-learn 1.x: some functions deprecated or changed defaults; if you rely on estimator behavior (e.g., default solvers, random_state), check for changes.
- pandas 2.x: removed some deprecated APIs (e.g. DataFrame.equals behavior), string handling changes in some methods; adapt as needed.
- fastapi/uvicorn: test cases using internal Starlette APIs may break; use public FastAPI interfaces.

## Reproducibility
All versions are pinned in `requirements.txt` to provide a reproducible environment. The `setup.sh` script creates a venv and installs these exact versions.

## Security
The older versions included known CVEs (e.g., old numpy and pandas had vulnerabilities disclosed over 2020-2022). Upgrading to the pinned versions improves security posture while keeping compatibility.

## Testing
A minimal test suite using pytest is included in `tests/test_runtime.py` and a small demo script is provided at `scripts/demo_predict.py` to ensure runtime behavior.

## Notes about CI Python versions
- When running tests in this environment, the workspace Python is CPython 3.13. Some packages (notably `numpy`, `scikit-learn`, `matplotlib`, and `pandas`) had different wheels for CPython 3.13 vs 3.10; the `requirements.txt` file is pinned to versions compatible with CPython 3.13 to allow the reproducible venv to be created here and for the tests to run (see `requirements.txt`).
- If you prefer to target Python 3.10 specifically for runtime, update the pins accordingly; the chosen versions in `requirements.txt` are considered modern, stable, and tested in this repo.
