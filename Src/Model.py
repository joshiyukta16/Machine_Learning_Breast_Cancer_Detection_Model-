# ==========================================
# Breast Cancer Detection using ML (SVM)
# ==========================================

# Install dependencies before running:
# pip install -r requirements.txt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay


# ------------------------------
# 1. Load Dataset
# ------------------------------
df = pd.read_csv("data/GSE183947_fpkm.csv.gz", compression='gzip')

print("Initial Shape:", df.shape)


# ------------------------------
# 2. Data Preprocessing
# ------------------------------

# Set first column (gene names) as index
df = df.set_index(df.columns[0])

# Transpose (samples as rows, genes as columns)
df = df.T

print("Shape after transpose:", df.shape)

# Convert to numeric (important for ML)
df = df.apply(pd.to_numeric, errors="coerce")

# Handle missing values
missing_values = df.isnull().sum().sum()
print("Total missing values:", missing_values)

df = df.fillna(df.median())


# ------------------------------
# 3. Label Assignment
# ------------------------------
labels = ["tumor"] * 30 + ["normal"] * 30
df["label"] = labels

# Separate features and target
X = df.drop(columns=["label"])
y = df["label"]

print("Feature shape:", X.shape)
print("Label distribution:\n", y.value_counts())


# ------------------------------
# 4. Log Transformation
# ------------------------------
X = np.log2(X + 1)


# ------------------------------
# 5. Feature Scaling
# ------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert back to DataFrame
X_scaled = pd.DataFrame(X_scaled, columns=X.columns, index=X.index)


# ------------------------------
# 6. Train-Test Split
# ------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)


# ------------------------------
# 7. Feature Selection
# ------------------------------
selector = SelectKBest(score_func=f_classif, k=100)

X_train_selected = selector.fit_transform(X_train, y_train)
X_test_selected = selector.transform(X_test)

print("After feature selection:", X_train_selected.shape)


# ------------------------------
# 8. Model Training (SVM)
# ------------------------------
model = SVC(kernel='linear', random_state=42)
model.fit(X_train_selected, y_train)


# ------------------------------
# 9. Prediction & Evaluation
# ------------------------------
y_pred = model.predict(X_test_selected)

accuracy = accuracy_score(y_test, y_pred)
print("\nFinal Accuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", cm)

# Classification Report
print("\nClassification Report:\n", classification_report(y_test, y_pred))


# ------------------------------
# 10. Visualization
# ------------------------------
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["tumor", "normal"])
disp.plot()

plt.title("Confusion Matrix - SVM Model")
plt.show() 