# Dependency Upgrade & Test Harness for oswe-mini-prime

This project upgrades an old dependency list and provides an automated pytest validation pipeline.

Files added/updated
- `requirements.txt` — Upgraded and pinned dependencies for Python 3.10+.
- `setup.sh` — Create a reproducible venv and install requirements.
- `run_tests.sh` — Activate venv and run pytest.
- `demo/demo_app.py` — Small FastAPI app and a demo function using numpy/pandas.
- `tests/test_runtime.py` — pytest tests that validate runtime features of numpy, pandas, scipy, matplotlib, scikit-learn, and FastAPI.
- `AUDIT.md` — Explains the before/after dependency changes and justification.

How to run
1. Ensure `python3` on PATH and is v3.10+.
2. Run in bash (or WSL):

```bash
./setup.sh
./run_tests.sh
```

This will create a `.venv` folder in the repo and run pytest. The suite provides baseline assurance that our key libs function properly with the upgraded versions.

Notes & next steps
- Consider running `pip-audit` or `safety` for CVE checks and frequency of the next upgrade cycle.
- If your code depends on pandas 1.x behavior or pydantic v1 APIs, consider a dedicated migration plan to move to pandas 2.x and pydantic v2.
