"""Analisis empiris data Forest Fires UCI ID 162."""
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def main():
    ds = fetch_ucirepo(id=162)
    X = ds.data.features.copy()
    ydf = ds.data.targets.copy()
    y = pd.to_numeric(ydf.iloc[:, 0], errors="coerce")
    valid = y.notna()
    X, y = X.loc[valid], y.loc[valid]
    df = X.copy()
    df["burned_area"] = y
    print("Dataset:", ds.metadata.get("name"), "| shape:", df.shape)
    print("\nTarget summary:")
    print(df["burned_area"].describe().round(3))
    print("Rows with zero burned area:", int((df["burned_area"] == 0).sum()))
    print("\nNumeric correlation with burned area:")
    corr = df.select_dtypes(include="number").corr(numeric_only=True)["burned_area"].sort_values(ascending=False)
    print(corr.round(3))
    # Target area sering sangat skewed; log1p stabilizes target scale.
    y_log = np.log1p(y.clip(lower=0))
    num = X.select_dtypes(include="number").columns.tolist()
    cat = [c for c in X.columns if c not in num]
    transformers = []
    if num:
        transformers.append(("num", SimpleImputer(strategy="median"), num))
    if cat:
        transformers.append(("cat", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ]), cat))
    prep = ColumnTransformer(transformers)
    X_train, X_test, y_train, y_test = train_test_split(X, y_log, test_size=.25, random_state=42)
    model = Pipeline([("prep", prep), ("model", RandomForestRegressor(n_estimators=250, random_state=42, min_samples_leaf=2))])
    model.fit(X_train, y_train)
    pred_log = model.predict(X_test)
    # Evaluate on log scale, which is the model's training target.
    print("\nTest MAE (log1p area):", round(mean_absolute_error(y_test, pred_log), 4))
    print("Test RMSE (log1p area):", round(np.sqrt(mean_squared_error(y_test, pred_log)), 4))
    print("R2 (log1p area):", round(r2_score(y_test, pred_log), 4))
    print("\nInterpretation: association/prediction does not establish causal drivers; this dataset is not satellite-based deforestation attribution.")
if __name__ == "__main__":
    main()
