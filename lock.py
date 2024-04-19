import threading
from contextlib import contextmanager
import os
import fcntl

class FileLock(object):
    """
    Lock a critical section across multiple processes.
    It is a blocking mechanism with no timeout.
    """
    def __init__(self, lock_file):
        self.lock_file = lock_file
        self.fd = None

    def __enter__(self):
        self.fd = os.open(self.lock_file, os.O_CREAT)
        fcntl.flock(self.fd, fcntl.LOCK_EX)

    def __exit__(self, *args):
        fcntl.flock(self.fd, fcntl.LOCK_UN)
        os.close(self.fd)
        self.fd = None

class TimeoutLock(object):
    """_summary_
    lock with timeout
    Args:
        object (_type_): _description_
    """
    def __init__(self):
        self._lock = threading.Lock()

    def acquire(self, blocking=True, timeout=-1):
        return self._lock.acquire(blocking, timeout)
    
    @contextmanager
    def acquire_timeout(self, timeout):
        result = self._lock.acquire(timeout=timeout)
        yield result
        if result:
            self._lock.release()

    def release(self):
        self._lock.release()
        
lock = TimeoutLock()

def thread_func():
    #print current thread id
    print(threading.current_thread().ident)
    with lock.acquire_timeout(9) as acquired:
        import time
        if acquired:
            print("thread:%s acquired"%(threading.current_thread().ident))
            #sleep
            time.sleep(1)
            print("thread:%s release"%(threading.current_thread().ident))
        else:
            print("thread:%s not acquired"%(threading.current_thread().ident))

#start 10 threads
threads = []
for i in range(10):
    t = threading.Thread(target=thread_func)
    threads.append(t)
    t.start()
#wait for all threads to finish
for i in range(10):
    threads[i].join()
print("all threads finished")
