import time
import random
import multiprocessing

class ConnectionPool:
    def __init__(self, size):
        """ 
        Initialize the connection pool with a semaphore and a list of available connections.
        
        Args:
            size (int): The maximum number of simultaneous connections allowed.
        """
        self.pool_size = size
        self.semaphore = multiprocessing.Semaphore(size)
        self.connections = [f"Connection-{i}" for i in range(size)]
        self.lock = multiprocessing.Lock()  # Ensures thread-safe operations on the pool

    def get_connection(self):
        """ 
        Acquire a connection from the pool.
        
        This method blocks if no connection is available until one is released.
        
        Returns:
            str: The connection identifier that was acquired.
        """
        self.semaphore.acquire()
        with self.lock:
            connection = self.connections.pop()
        print(f"{multiprocessing.current_process().name} acquired {connection}")
        return connection

    def release_connection(self, connection):
        """ 
        Release a connection back to the pool.
        
        Args:
            connection (str): The connection identifier to be released.
        """
        with self.lock:
            self.connections.append(connection)
        self.semaphore.release()
        print(f"{multiprocessing.current_process().name} released {connection}")