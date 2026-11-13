import time
from timeit import default_timer as timer

def run_task(name,seconds):
    print(f'{name} starts as :{timer()}')
    time.sleep(seconds)
    print(f'{name} completed at{timer()}')

start=timer()
run_task('task1',2)
run_task('task2',1)
run_task('task3',3)
print(f'\n total time :{timer()-start:.2f} s')
