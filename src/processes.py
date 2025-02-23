import multiprocessing
import time
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt

# using a Manager for shared memory
manager = multiprocessing.Manager()
best_rmse = manager.Value(float, float('inf'))
best_mape = manager.Value(float, float('inf'))
best_model = manager.list()
best_parameters = manager.dict()

def train_and_evaluate(n_estimators, max_features, max_depth, best_rmse, best_mape, best_model, best_parameters, X_train_filled, X_val_filled, y_train, y_val):
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
    
    # with best_rmse.get_lock():
    if rmse < best_rmse.value:
        best_rmse.value = rmse
        best_mape.value = mape
        best_model[:] = [rf_model]
        best_parameters.clear()
        best_parameters.update({
            'n_estimators': n_estimators,
            'max_features': max_features,
            'max_depth': max_depth
        })

def execution(X_train_filled, X_val_filled, y_train, y_val):
    start_time = time.time()
    
    # Define the parameter ranges
    n_estimators_range = [10, 25, 50, 100, 200, 300, 400]
    max_features_range = ['sqrt', 'log2', None]  # None means using all features
    max_depth_range = [1, 2, 5, 10, 20, None]  # None means no limit
    
    processes = []
    for n in n_estimators_range:
        for f in max_features_range:
            for d in max_depth_range:
                p = multiprocessing.Process(target=train_and_evaluate, args=(n, f, d, best_rmse, best_mape, best_model, best_parameters, X_train_filled, X_val_filled, y_train, y_val))
                processes.append(p)
                p.start()
    
    # Wait for all processes to complete
    for p in processes:
        p.join()
    
    print(f"Best Parameters: {dict(best_parameters)} -> RMSE: {best_rmse.value}, MAPE: {best_mape.value}%")
    end_time = time.time()
    
    processing_time = end_time - start_time
    print(f"Multiprocessing execution time is: {processing_time} seconds")
    return processing_time