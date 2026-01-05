# Dependency Audit and Upgrade Plan

## Summary
- **Target Python:** 3.10+
- **Goal:** Replace unmaintained/incompatible versions with current stable releases; pin for reproducibility.
- **Approach:** Choose well-supported versions that interoperate (notably NumPy 1.26.x to avoid ecosystem incompatibilities with NumPy 2.0), note breaking changes, and provide upgrade justification.

## Before → After

| Package | Before | After (Pinned) | Key Reasons / Notes |
|---------|--------|----------------|----------------------|
| numpy | 1.18.0 | 1.26.4 | 1.18 doesn't support Python ≥3.10; numerous CVEs (integer overflows, buffer overreads) fixed in later releases; 1.26.x is the last 1.x line, widely supported by SciPy/Scikit-Learn/Pandas.
| scipy | 1.5.2 | 1.11.4 | 1.5.x doesn't support Python ≥3.10; 1.11.x is stable, supports NumPy 1.26.x, drops Python <3.9.
| pandas | 1.1.5 | 2.2.2 | 1.1.x EOL, no Py3.10 support; 2.2.x brings performance & bug fixes; note breaking changes (string dtype, index behavior, removed deprecated APIs).
| scikit-learn | 0.24.1 | 1.4.2 | 0.24.x EOL, no Py3.10 support; 1.4.x stable with NumPy 1.26.x; some deprecated estimators/parameters removed.
| matplotlib | 3.3.2 | 3.8.4 | 3.3.x EOL, no Py3.10 wheels; 3.8.x compatible with NumPy 1.26.x; style/rcParam defaults evolved.
| pytest | 5.4.3 | 8.2.0 | 5.x unsupported; 8.x supports Py3.10+ with improved fixtures; some plugins may need updates.
| fastapi | 0.63.0 | 0.115.6 | 0.63.x predates Pydantic v2; security & performance fixes; **breaking**: Pydantic v2 model semantics; Starlette upgrades.
| uvicorn | 0.13.3 | 0.30.6 | Old version misses HTTP/2, ASGI improvements; security fixes; requires `click>=8`.
| httpx | — | 0.27.2 | Added explicitly for `fastapi.testclient`/Starlette TestClient; modern async HTTP client, Py3.8+.

## Breaking-Change Highlights
- **FastAPI / Pydantic v2:**
  - Models now use `pydantic` v2; `BaseModel` validation semantics changed; use `model_validate`, `field_validator`, etc.
  - Response models/`from_orm` behavior updated; `Config` → `model_config`.
- **Pandas 2.x:**
  - Deprecated APIs removed (e.g., `DataFrame.append`), stricter type handling, `Index`/`RangeIndex` behaviors.
- **NumPy 1.26:**
  - Drops Python <3.9; some legacy aliases removed; stricter type casting.
- **Scikit-Learn 1.4:**
  - Deprecated parameters removed; `n_features_in_` handling and feature name validation stricter.
- **Matplotlib 3.8:**
  - Default colormaps/styles evolved; some deprecated rcParams removed; encourages `plt.show(block=False)` in headless.
- **Pytest 8:**
  - Older plugins may break; `--strict-markers` recommended; internal deprecations removed.

## Security & Maintenance Concerns (Old Versions)
- **Unmaintained:** All prior versions are EOL; no security fixes.
- **Known CVEs:** Various CVEs affected NumPy, Pandas, Pytest, Uvicorn in older releases (buffer overflows, path traversal, ReDoS). Upgrading mitigates these.

## Compatibility Strategy
- Pin to mutually compatible versions (NumPy 1.26.x to avoid NumPy 2.0 adoption lag in SciPy/Sklearn/Pandas).
- Leverage wheels for Py3.10+ to avoid build-from-source where possible.
- Tests validate core functionality of each stack component.
