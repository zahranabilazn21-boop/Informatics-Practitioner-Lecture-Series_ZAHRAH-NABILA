"""Analisis risiko kredit menggunakan dataset publik UCI ID 350."""
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix

def main():
    ds = fetch_ucirepo(id=350)
    X = ds.data.features.copy()
    y_raw = ds.data.targets.copy()
    print("Dataset:", ds.metadata.get("name"))
    print("Rows/columns:", X.shape)
    print("Feature columns:", list(X.columns))
    print("Target columns:", list(y_raw.columns))
    # UCI biasanya menyediakan satu target; gunakan kolom target pertama.
    y = y_raw.iloc[:, 0]
    # Pastikan label dua kelas. Target dataset ini biasanya 1=default, 0=non-default.
    y = pd.to_numeric(y, errors="coerce")
    valid = y.notna()
    X, y = X.loc[valid], y.loc[valid].astype(int)
    print("\nTarget distribution:")
    print(y.value_counts(dropna=False).sort_index())
    print("\nMissing values (top 15):")
    print(X.isna().sum().sort_values(ascending=False).head(15))
    numeric = X.select_dtypes(include="number").columns.tolist()
    categorical = [c for c in X.columns if c not in numeric]
    transformers = []
    if numeric:
        transformers.append(("num", Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scale", StandardScaler())
        ]), numeric))
    if categorical:
        transformers.append(("cat", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent"))
        ]), categorical))
    prep = ColumnTransformer(transformers, remainder="drop")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=.25, random_state=42, stratify=y
    )
    model = Pipeline([
        ("prep", prep),
        ("model", LogisticRegression(max_iter=2000, class_weight="balanced"))
    ])
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    prob = model.predict_proba(X_test)[:, 1]
    print("\n=== Test set results ===")
    print("Confusion matrix [actual rows, predicted columns]:\n", confusion_matrix(y_test, pred))
    print(classification_report(y_test, pred, zero_division=0))
    print("ROC-AUC:", round(roc_auc_score(y_test, prob), 4))
    print("\nInterpretation: metrics describe this held-out sample only. Evaluate calibration, decision costs, and external validity before operational use.")
if __name__ == "__main__":
    main()
