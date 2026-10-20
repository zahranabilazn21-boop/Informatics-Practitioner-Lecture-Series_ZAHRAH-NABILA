"""Benchmark sederhana serial vs multiprocessing pada dataset UCI Air Quality."""
import time
from concurrent.futures import ProcessPoolExecutor
import pandas as pd
from ucimlrepo import fetch_ucirepo

def summarize_column(args):
    name, values = args
    s = pd.to_numeric(pd.Series(values), errors="coerce")
    return {"column": name, "count": int(s.notna().sum()),
            "mean": float(s.mean()), "std": float(s.std())}

def main():
    ds = fetch_ucirepo(id=360)
    df = pd.concat([ds.data.features, ds.data.targets], axis=1)
    numeric = df.select_dtypes(include="number")
    if numeric.empty:
        numeric = df.apply(pd.to_numeric, errors="coerce").dropna(axis=1, how="all")
    tasks = [(col, numeric[col].tolist()) for col in numeric.columns]
    print("Dataset:", ds.metadata.get("name"), "| shape:", df.shape)
    t0 = time.perf_counter()
    serial = [summarize_column(t) for t in tasks]
    t_serial = time.perf_counter() - t0
    t0 = time.perf_counter()
    with ProcessPoolExecutor() as pool:
        parallel = list(pool.map(summarize_column, tasks))
    t_parallel = time.perf_counter() - t0
    print("\nSerial time:", round(t_serial, 4), "seconds")
    print("Parallel time:", round(t_parallel, 4), "seconds")
    print("Speedup:", round(t_serial / t_parallel, 3) if t_parallel else "n/a")
    print("\nSummary:")
    print(pd.DataFrame(serial).to_string(index=False))
    print("\nCaution: for a modest dataset, process startup overhead can exceed parallel benefits. This measures this machine only.")
if __name__ == "__main__":
    main()
