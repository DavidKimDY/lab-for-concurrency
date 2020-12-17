import asyncio
import random

# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


async def makerandom(idx, threshold=9):
    color = c[idx]
    print(color + f'initiated makerandom({idx})')
    i = random.randint(0, 10)
    while i <= threshold:
        print(color + f'makerandom({idx}) == {i} is too low')
        await asyncio.sleep(idx)
        i = random.randint(0, 10)
    print(color + f'-----> Finished makerandom({idx}) is done with {i}')
    return i

async def main():
    res = await asyncio.gather(*[makerandom(idx) for idx in [1, 2, 3]])
    return res

if __name__ == '__main__':
    random.seed(44)
    r1, r2, r3 = asyncio.run(main())
    print(f'{c[0]}r1 : {r1}\nr2 : {r2}\nr3 : {r3}')