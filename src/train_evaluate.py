from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def train_and_evaluate(model, model_name):
    model.fit(X_train, y_train)  # Train the model
    y_pred = model.predict(X_test)  # Make predictions

    # Compute metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average="weighted")
    recall = recall_score(y_test, y_pred, average="weighted")
    f1 = f1_score(y_test, y_pred, average="weighted")
    conf_matrix = confusion_matrix(y_test, y_pred)

    # Display results
    results_df = pd.DataFrame({
        "Metric": ["Accuracy", "Precision", "Recall", "F1-score"],
        model_name: [accuracy, precision, recall, f1]
    })

    print(f"\nConfusion Matrix for {model_name}:\n", conf_matrix)

    return results_df

def execute(df):
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_results = train_and_evaluate(rf_model, "Random Forest")
    
    print(rf_results)
    
    svm_model = SVC(kernel="linear", random_state=42)
    svm_results = train_and_evaluate(svm_model, "Support Vector Machine")
    
    print(svm_results)
    
    log_reg_model = LogisticRegression(random_state=42)
    log_reg_results = train_and_evaluate(log_reg_model, "Logistic Regression")
    
    print(log_reg_results)