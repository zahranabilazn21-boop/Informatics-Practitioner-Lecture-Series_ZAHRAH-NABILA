"""Prediksi penjualan harian dari dataset transaksi ritel publik UCI ID 352."""
import pandas as pd
import numpy as np
from ucimlrepo import fetch_ucirepo
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.dummy import DummyRegressor

def main():
    ds = fetch_ucirepo(id=352)
    df = pd.concat([ds.data.features, ds.data.targets], axis=1)
    print("Dataset:", ds.metadata.get("name"), "| shape:", df.shape)
    # Kolom UCI Online Retail biasanya memakai nama berikut.
    required = ["InvoiceDate", "Quantity", "InvoiceNo"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Kolom yang dibutuhkan tidak ditemukan: {missing}. Kolom tersedia: {list(df.columns)}")
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    # Invoice yang diawali C adalah pembatalan; kuantitas <=0 dikeluarkan dari penjualan bersih sederhana.
    df = df.dropna(subset=["InvoiceDate", "Quantity"])
    df = df[~df["InvoiceNo"].astype(str).str.upper().str.startswith("C")]
    df = df[df["Quantity"] > 0].copy()
    daily = df.groupby(df["InvoiceDate"].dt.floor("D"))["Quantity"].sum().rename("units_sold").reset_index()
    daily = daily.sort_values("InvoiceDate")
    daily["day_of_week"] = daily["InvoiceDate"].dt.dayofweek
    daily["month"] = daily["InvoiceDate"].dt.month
    daily["day_of_month"] = daily["InvoiceDate"].dt.day
    daily["lag_1_day"] = daily["units_sold"].shift(1)
    daily["lag_7_days"] = daily["units_sold"].shift(7)
    daily = daily.dropna().reset_index(drop=True)
    print("\nDaily sales rows:", len(daily))
    print("Period:", daily["InvoiceDate"].min(), "to", daily["InvoiceDate"].max())
    # Time-based split: data lebih awal untuk train, periode akhir untuk test.
    split = int(len(daily) * .8)
    train, test = daily.iloc[:split], daily.iloc[split:]
    features = ["day_of_week", "month", "day_of_month", "lag_1_day", "lag_7_days"]
    X_train, y_train = train[features], train["units_sold"]
    X_test, y_test = test[features], test["units_sold"]
    models = {
        "Baseline median": DummyRegressor(strategy="median"),
        "Random Forest": RandomForestRegressor(n_estimators=200, random_state=42, min_samples_leaf=3)
    }
    results = []
    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = np.maximum(0, model.predict(X_test))
        mae = mean_absolute_error(y_test, pred)
        rmse = np.sqrt(mean_squared_error(y_test, pred))
        results.append({"model": name, "MAE_units": mae, "RMSE_units": rmse})
        print(f"{name}: MAE={mae:.2f} units, RMSE={rmse:.2f} units")
    out = pd.DataFrame(results)
    out.to_csv("retail_model_comparison.csv", index=False)
    daily.to_csv("daily_retail_sales.csv", index=False)
    print("\nSaved: retail_model_comparison.csv, daily_retail_sales.csv")
    print("Catatan: prediksi berdasarkan transaksi historis ini tidak menjamin kinerja pada periode atau bisnis lain.")
if __name__ == "__main__":
    main()
