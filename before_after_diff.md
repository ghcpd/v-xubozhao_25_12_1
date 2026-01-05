# Before -> After Requirements Diff

Original `requirements_old.txt`:

```
scikit-learn==0.24.1  
numpy==1.18.0  
pandas==1.1.5  
matplotlib==3.3.2  
scipy==1.5.2  
pytest==5.4.3  
fastapi==0.63.0  
uvicorn==0.13.3  
```

New `requirements.txt`:

```
numpy==2.3.5
scikit-learn==1.7.2
pandas==2.3.3
matplotlib==3.10.7
scipy==1.16.3
pytest==9.0.1
fastapi==0.123.0
uvicorn==0.38.0
```

Justifications for changes are included in `dependency_report.md` (compatibility, security, and wheel availability).
