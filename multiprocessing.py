import threading
import time
from datetime import datetime
import random

def worker():
    # Generate a random sleep time between 0 and 1 seconds
    sleep_time = random.uniform(0, 1)
    
    # Sleep for the random time
    time.sleep(sleep_time)
    
    # Print the current time after sleeping
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Thread {threading.current_thread().name} - Current Time: {current_time}")
    
if __name__ == "__main__":
    # Create three separate threads
    threads = [threading.Thread(target=worker) for _ in range(3)]
    
    # Start each thread
    for thread in threads:
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()


#bug report I had no struggles with using threading but did with multiprocessing
#as my keyword to import and use, I wanted to try the way I knew versus something 
#new