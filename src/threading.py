import concurrent.futures
import time

# Define the parameter ranges
n_estimators_range = [10, 25, 50, 100, 200, 300, 400]
max_features_range = ['sqrt', 'log2', None]  # None means using all features
max_depth_range = [1, 2, 5, 10, 20, None]  # None means no limit

best_rmse = float('inf')
best_mape = float('inf')
best_model = None
best_parameters = {}

def train_and_evaluate(n_estimators, max_features, max_depth, X_train_filled, X_val_filled, y_train, y_val):
    global best_rmse, best_mape, best_model, best_parameters
    
    rf_model = RandomForestRegressor(
        n_estimators=n_estimators,
        max_features=max_features,
        max_depth=max_depth,
        random_state=42
    )
    rf_model.fit(X_train_filled, y_train)
    
    y_val_pred = rf_model.predict(X_val_filled)
    rmse = sqrt(mean_squared_error(y_val, y_val_pred))
    mape = mean_absolute_percentage_error(y_val, y_val_pred) * 100
    
    print(f"Parameters: {n_estimators}, {max_features}, {max_depth} -> RMSE: {rmse}, MAPE: {mape}%")
    
    if rmse < best_rmse:
        best_rmse = rmse
        best_mape = mape
        best_model = rf_model
        best_parameters = {
            'n_estimators': n_estimators,
            'max_features': max_features,
            'max_depth': max_depth
        }

def execution(X_train_filled, X_val_filled, y_train, y_val):
    global n_estimators_range, max_features_range, max_depth_range
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for n_estimators in n_estimators_range:
            for max_features in max_features_range:
                for max_depth in max_depth_range:
                    futures.append(executor.submit(train_and_evaluate, n_estimators, max_features, max_depth, X_train_filled, X_val_filled, y_train, y_val))
        
        # Wait for all threads to complete
        for future in concurrent.futures.as_completed(futures):
            future.result()
    
    print(f"Best Parameters: {best_parameters} -> RMSE: {best_rmse}, MAPE: {best_mape}%")
    end_time = time.time()
    threading_time = end_time - start_time
    print(f"Threading execution time is: {threading_time} seconds")

    return threading_time