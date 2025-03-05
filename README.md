This repository is used for the course DSAI 3202, Parallel and Distributed Computing. :)

Currently, we are working on Lab 4 Part 2: Machine Learning Application.

Multiprocessing Speedup: 5.14.
Multiprocessing Efficiency: 0.86.
Amdahl's: 5.981478871697615.
Gustafson's: 5.996903587106189.

Speedup Analysis:
A speedup of 5.14 indicates that parallel execution reduced computation time greatly compared to sequential execution.

Efficiency Analysis:
Multiprocessing did scale perfectly with the number of cores available, improving performance by 86%.

Confusion Matrix for Random Forest:
 [[17  5]
 [ 4 17]]
Metric	Random Forest
0	Accuracy	0.790698
1	Precision	0.791553
2	Recall	0.790698
3	F1-score	0.790698

Confusion Matrix for Support Vector Machine:
 [[12 10]
 [ 3 18]]
Metric	Support Vector Machine
0	Accuracy	0.697674
1	Precision	0.723256
2	Recall	0.697674
3	F1-score	0.690671

Confusion Matrix for Logistic Regression:
 [[18  4]
 [ 3 18]]
0	Accuracy	0.837209
1	Precision	0.838115
2	Recall	0.837209
3	F1-score	0.837209

# DSAI 3202 - Parallel and Distributed Computing

This repository is part of the coursework for **DSAI 3202 - Parallel and Distributed Computing**. It contains the implementation and results for **Lab 4 Part 2: Machine Learning Application**.

## Performance Metrics

### Multiprocessing Performance:
- **Speedup:** 5.14
- **Efficiency:** 0.86
- **Amdahl's Law:** 5.98
- **Gustafson's Law:** 5.99

### Performance Analysis:
- **Speedup** of 5.14 indicates a significant reduction in computation time when parallelized compared to sequential execution.
- **Efficiency** of 0.86 suggests near-perfect scaling with the number of cores, improving performance by 86%.

## Machine Learning Model Results

### 1. Random Forest
- **Confusion Matrix:**
  
17	5
4	17


- **Metrics:**
- **Accuracy:** 0.791
- **Precision:** 0.792
- **Recall:** 0.791
- **F1-score:** 0.791

### 2. Support Vector Machine (SVM)
- **Confusion Matrix:**

12	10
3	18


- **Metrics:**
- **Accuracy:** 0.698
- **Precision:** 0.723
- **Recall:** 0.698
- **F1-score:** 0.691

### 3. Logistic Regression
- **Confusion Matrix:**


18	4
3	18


- **Metrics:**
- **Accuracy:** 0.837
- **Precision:** 0.838
- **Recall:** 0.837
- **F1-score:** 0.837

## Conclusion

The models exhibit different performance levels across accuracy, precision, recall, and F1-score, with Logistic Regression performing the best among the three. The parallel execution demonstrated strong scalability with a speedup of 5.14 and high efficiency, demonstrating the effectiveness of multiprocessing for this task.
