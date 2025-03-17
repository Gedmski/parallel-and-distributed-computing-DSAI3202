from src.database import ConnectionPool
import time
import random
import multiprocessing

def access_database(pool):
    """ 
    Simulate a process accessing the database by acquiring and releasing a connection.
    
    This function:
    - Waits for a connection if none are available.
    - Simulates performing a database operation by sleeping for a random duration.
    - Releases the connection after the operation is complete.
    
    Args:
        pool (ConnectionPool): The connection pool to acquire and release connections from.
    """
    print(f"{multiprocessing.current_process().name} is waiting for a connection...")
    connection = pool.get_connection()
    time.sleep(random.uniform(1, 3))  # Simulate database operation
    pool.release_connection(connection)

def execution():
    pool_size = 3  # Number of available connections
    num_processes = 6  # Total number of processes trying to access the database

    pool = ConnectionPool(pool_size)
    processes = [multiprocessing.Process(target=access_database, args=(pool,), name=f"Process-{i}") for i in range(num_processes)]

    for process in processes:
        process.start()
    
    for process in processes:
        process.join()