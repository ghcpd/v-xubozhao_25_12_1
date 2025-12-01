from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}

# Simple function using numpy/pandas for demonstration
import numpy as np
import pandas as pd

def demo_process(a):
    # simple numpy operations and return a pandas df
    arr = np.array(a)
    stats = {
        "mean": float(arr.mean()),
        "sum": float(arr.sum()),
    }
    df = pd.DataFrame([stats])
    return df


if __name__ == "__main__":
    print("Demo app - run uvicorn: uvicorn demo.demo_app:app --reload")
