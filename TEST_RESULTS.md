# Pytest execution results

Environment: CPython 3.13.9

Command run: `./setup.ps1` (or `./setup.sh` in POSIX), then `run_tests.ps1` / `run_tests.sh`

Output:

6 passed in 2.72s

(Full logs are in CI output; this is the captured summary.)

Notes:
- First attempt used pinned numpy 1.x which required building from source for CPython 3.13; adjusted to numpy 2.x.
- scikit-learn 1.6.0 installs prebuilt wheels for CPython 3.13.
- Matplotlib 3.10 installs prebuilt wheel for CPython 3.13; earlier 3.8 attempted source build and failed due to missing C toolchain.
