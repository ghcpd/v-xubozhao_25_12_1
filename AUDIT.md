# Dependency Upgrade Audit

This repository originally contained `requirements_old.txt` with older, potentially insecure and Python-incompatible packages. Below is a summary of the audit and what was changed.

## Before (old `requirements_old.txt`)
- scikit-learn==0.24.1
- numpy==1.18.0
- pandas==1.1.5
- matplotlib==3.3.2
- scipy==1.5.2
- pytest==5.4.3
- fastapi==0.63.0
- uvicorn==0.13.3

## After (`requirements.txt`) — new, pinned, Python 3.10+ compatible
- numpy==1.25.3
  - Justification: 1.18 is several years old; 1.25 includes performance and security fixes and supports Python 3.10+.
- scipy==1.11.2
  - Justification: Required for modern numerical methods and bug/security fixes.
- pandas==1.5.3
  - Justification: Modern pandas with Python 3.10 support without moving to pandas 2.x to avoid API-breaking surprises.
- matplotlib==3.7.2
  - Justification: Latest stable branch supporting Python 3.10+ and improved rendering.
- scikit-learn==1.2.2
  - Justification: Newer scikit-learn provides performance, compatibility and fixes for Python 3.10.
- pytest==7.4.0
  - Justification: Pytest 5.x is no longer maintained; 7.x supports 3.10+ and has many improvements.
- fastapi==0.95.2
  - Justification: Ensures compatibility with modern Python and ASGI stack; avoid too-high jumps that may require Pydantic v2 migration.
- uvicorn==0.22.0
  - Justification: ASGI server updated to improve performance and security.
- pydantic==1.10.12
  - Justification: Keep pydantic v1 for now to avoid Pydantic v2 migration. FastAPI 0.95 supports Pydantic v1.
- httpx==0.24.1
  - Justification: Utility to test FastAPI endpoints reliably.

## Migration notes
- We chose to prefer gradual upgrades where possible to avoid breaking API changes (e.g., pandas 1.5.x vs 2.x and Pydantic v1 vs v2).
- If the main application intends to adopt Pydantic v2 (pydantic 2.x), further code changes are required and FastAPI should be upgraded to a version compatible with pydantic v2.

## How to run the tests
- Ensure Python 3.10+ is installed
- Run `./setup.sh` to create a venv and install dependencies
- Run `./run_tests.sh` to run pytest

All tests are implemented using pytest in `tests/test_runtime.py` and exercise basic functionality of the major libraries.

---

If additional packages are discovered in the codebase (not found in `requirements_old.txt`), they should be audited and handled similarly.
