import asyncio
from timeit import default_timer as timer

async def run_task(name,seconds):
    print(f'{name} starts as :{timer()}')
    await asyncio.sleep(seconds)
    print(f'{name} completed at{timer()}')

async def main():
    start=timer()
    await asyncio.gather(
        run_task('task1',2),
        run_task('task2',1),
        run_task('task3',3)
    )
    print(f'\n total time :{timer()-start:.2f} s')

asyncio.run(main())