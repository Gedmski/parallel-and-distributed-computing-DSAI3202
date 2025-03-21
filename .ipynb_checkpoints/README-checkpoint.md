# Lab 3 Part 2: Data Parallel Model — Random Forest Optimization

## Author
**Gabriel Marquez**

---

## 📌 Objectives

- Build a **parallel program** to enhance the training of a machine learning model.
- Compare **sequential**, **threading**, and **multiprocessing** approaches to hyperparameter search.
- Measure **execution time** and **performance metrics** (Speedup, Efficiency, Amdahl’s, Gustafsson’s Laws).
- Understand when to use **threads** vs. **processes**.

---

## 🧪 Dataset Setup

1. Downloaded `housing_prices_data.zip` and `ModelingWithRandomForests.ipynb`.
2. Transferred the files to the remote machine using `scp`.
3. Moved them into the local repository:
   - Notebook to `notebooks/`
   - Zip file to `data/`, then unzipped and deleted the archive.

---

## ⚙️ Experiment Summary

Hyperparameter tuning of a **Random Forest Regressor** was performed with three approaches:

### 🔹 Sequential Execution

- **Best Parameters**:  
  `{'n_estimators': 100, 'max_features': None, 'max_depth': None}`  
- **RMSE**: 26,057.94  
- **MAPE**: 9.83%  
- **Execution Time**: **64.72 seconds**

---

### 🔹 Threading (Parallel Search)

- **Best Parameters**:  
  `{'n_estimators': 100, 'max_features': None, 'max_depth': None}`  
- **RMSE**: 26,057.94  
- **MAPE**: 9.87%  
- **Execution Time**: **24.12 seconds**

---

### 🔹 Multiprocessing (Parallel Search)

- **Best Parameters**:  
  `{'n_estimators': 100, 'max_features': None, 'max_depth': None}`  
- **RMSE**: 26,057.94  
- **MAPE**: 9.87%  
- **Execution Time**: **14.07 seconds**

---

## 📊 Performance Metrics

| Metric                | Threading      | Multiprocessing |
|----------------------|----------------|-----------------|
| **Speedup**          | 2.68×          | 4.60×           |
| **Efficiency**       | 44.73%         | 76.65%          |
| **Amdahl’s Law**     | 4.43×          | 4.43×           |
| **Gustafsson’s Law** | 5.64×          | 5.64×           |

---

## ❓ Lab Questions & Answers

### 1. How does execution time change between sequential, threading, and multiprocessing?

- **Threading** improved performance slightly but was limited by Python’s Global Interpreter Lock (GIL).
- **Multiprocessing** offered significant speedup by utilizing multiple cores and bypassing the GIL.
- Execution time dropped from **64.72s** (sequential) to **24.12s** (threading) to **14.07s** (multiprocessing).

---

### 2. Performance Metrics Summary

- **Speedup**: Shows how much faster the parallel versions are compared to the sequential version.
- **Efficiency**: Indicates how well parallel resources (threads/processes) are utilized.
- **Amdahl’s Law**: Predicts maximum theoretical speedup with fixed workload.
- **Gustafsson’s Law**: Accounts for workload scaling in parallel environments.

---

## ✅ Conclusion

- **Multiprocessing** is the best choice for **CPU-bound** tasks like model training and hyperparameter tuning.
- **Threading** may be more suitable for **I/O-bound** or lightweight tasks.
- Applying parallel programming techniques significantly reduces execution time in machine learning workflows.

---
