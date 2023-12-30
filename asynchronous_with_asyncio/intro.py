import time

import asyncio


async def count():
    print('one')
    await asyncio.sleep(1)
    print('two')


async def main():
    # throwing one by one
    await count()
    await count()
    await count()
    await count()
    # async: gather -> throws one by one, but as soon as starts sleeping yells up to the event loop and gives control
    #                  back, so, next count() is called and so on.
    print('****************with gather*********************')
    await asyncio.gather(count(), count(), count(), count())

if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f'{__file__} executed in {elapsed:0.2f} seconds')
