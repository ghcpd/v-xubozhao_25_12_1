# Before → After Dependency Diff

```diff
- scikit-learn==0.24.1
+ scikit-learn==1.4.2   # Py3.10+ support; performance and bug fixes; deprecated APIs removed

- numpy==1.18.0
+ numpy==1.26.4         # Py3.10+ wheels; security fixes; ecosystem compatibility (SciPy/Sklearn/Pandas)

- pandas==1.1.5
+ pandas==2.2.2         # Py3.10+ support; major performance improvements; deprecated APIs removed

- matplotlib==3.3.2
+ matplotlib==3.8.4     # Py3.10+ wheels; rendering/styling improvements; bug/security fixes

- scipy==1.5.2
+ scipy==1.11.4         # Py3.10+ support; numerical stability & performance fixes

- pytest==5.4.3
+ pytest==8.2.0         # Modern pytest features; Py3.10+; better warning/fixture handling

- fastapi==0.63.0
+ fastapi==0.115.6      # Security fixes; Pydantic v2; async improvements; breaking changes noted

- uvicorn==0.13.3
+ uvicorn[standard]==0.30.6  # ASGI/HTTP2 improvements; security fixes; click>=8

+ httpx==0.27.2         # Added for FastAPI/Starlette TestClient; async HTTP client
```

## Justification Highlights
- **Python compatibility:** All upgraded packages provide wheels for Python 3.10+ (tested on Python 3.11).
- **Security:** Old versions are EOL and have known vulnerabilities; upgrades bring patched dependencies.
- **Ecosystem alignment:** NumPy 1.26.x ensures compatibility with current SciPy/Sklearn/Pandas; FastAPI aligned with Pydantic v2.
- **Testing:** Added `httpx` explicitly to support `fastapi.testclient`.
