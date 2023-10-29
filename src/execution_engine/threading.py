```python
import threading
from queue import Queue
from src.execution_engine.run_time_execution import execute_node

class Worker(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            node, data = self.queue.get()
            try:
                execute_node(node, data)
            finally:
                self.queue.task_done()

class ThreadPool:
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks).start()

    def add_task(self, node, data):
        self.tasks.put((node, data))

    def wait_completion(self):
        self.tasks.join()
```