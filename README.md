# 🧬 Breast Cancer Detection using Machine Learning (Gene Expression Data)

---

## 📌 Overview
This project focuses on classifying breast cancer samples into **tumor** and **normal** categories using gene expression data.  
The dataset is obtained from the NCBI Gene Expression Omnibus (GEO) with accession ID **GSE183947**.

Machine learning techniques are applied to analyze high-dimensional RNA-Seq data and build a predictive classification model.

---

## 🎯 Objective
To develop an accurate and reliable machine learning model for classifying breast cancer samples based on gene expression profiles.

---

## 📊 Dataset Information

- **Source:** NCBI GEO  
- **Accession ID:** GSE183947  
- **Data Type:** RNA-Seq (FPKM normalized)  
- **Total Samples:** 60  
  - Tumor: 30  
  - Normal: 30  
- **Features:** ~20,000 genes  

---

## 🛠️ Tools and Technologies

- **IDE:** Visual Studio Code  
- **Language:** Python  

### 📚 Libraries Used
- NumPy  
- Pandas  
- Matplotlib  
- Scikit-learn  
- SciPy  

---

## ⚙️ Project Workflow

### 1️⃣ Data Collection
Dataset downloaded from GEO database.

### 2️⃣ Data Preprocessing
- Dataset transposed (samples → rows, genes → columns)  
- Converted to numeric format  
- Missing values handled  
- Log₂(x + 1) transformation applied  
- Feature scaling using StandardScaler  

### 3️⃣ Label Assignment
- Tumor and Normal labels assigned  
- Data split into:
  - **X (features)**
  - **y (labels)**  

### 4️⃣ Train-Test Split
- 80% training, 20% testing  
- Stratified sampling used  

### 5️⃣ Feature Selection
- SelectKBest (ANOVA F-test) used  
- Reduced dimensionality  

### 6️⃣ Model Building
- Algorithm: **Support Vector Machine (SVM)**  
- Kernel: Linear  

### 7️⃣ Model Evaluation
- Accuracy Score  
- Confusion Matrix  
- Classification Report  

---

## 📈 Results

- High accuracy achieved in classification  
- Feature selection improved performance  
- Model generalized well on test data  

---

## 📊 Confusion Matrix

![Confusion Matrix](Images/Confusion_Matrix_Output_Image.png) 

---

## 📋 Classification Report 

Classification Report:
               precision    recall  f1-score   support

      normal       1.00      1.00      1.00         6
       tumor       1.00      1.00      1.00         6

    accuracy                           1.00        12
   macro avg       1.00      1.00      1.00        12
weighted avg       1.00      1.00      1.00        12

---

## 🏁 Conclusion

In this project, a machine learning pipeline was developed to classify breast cancer samples using high-dimensional gene expression data. The dataset was preprocessed using log transformation and feature scaling to improve data quality and model performance. Feature selection helped reduce dimensionality and retain the most informative genes.

A Support Vector Machine (SVM) model was trained and evaluated, achieving strong performance in distinguishing tumor and normal samples. The results demonstrate the effectiveness of machine learning techniques in analyzing complex biological data.

This project highlights the potential of computational approaches in bioinformatics for disease classification and can be extended for biomarker discovery and precision medicine applications. 

--- 

📁 Project Structure 

Machine_Learning_Project/
│
├── data/
│   └── GSE183947_fpkm.csv
│
├── notebooks/
│   └── Machine_Learning_Project.ipynb
│
├── src/
│   └── model.py
│
├── README.md
└── requirements.txt 

--- 

▶️ How to Run 

git clone https://github.com/joshiyukta16/Machine_Learning_Breast_Cancer_Detection_Model-.git
cd Breast-Cancer-Detection-ML
pip install -r requirements.txt
jupyter notebook 

--- 

## 🧠 Applications
- Breast cancer detection
- Biomarker discovery
- Precision medicine
- Bioinformatics research 

## 🔮 Future Scope
- Apply deep learning models
- Perform feature importance analysis
- Integrate multi-omics data
- Deploy as a web application 

--- 

👩‍💻 Author

Yukta Joshi
B.Tech Bioinformatics (AI & ML) 

🙏 Acknowledgment

Data provided by NCBI GEO database.

⭐ If you like this project, give it a star!! 

--- 
