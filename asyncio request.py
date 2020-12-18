import asyncio
import requests
import time

async def main():
    loop = asyncio.get_event_loop()
    future1 = loop.run_in_executor(None, requests.get, 'https://www.google.com')
    future2 = loop.run_in_executor(None, requests.get, 'https://www.naver.com')
    future3 = loop.run_in_executor(None, requests.get, 'https://www.daum.net')

    start = time.time()
    for _ in range(10):
        res1 = await future1
        res2 = await future2
        res3 = await future3
    end = time.time()

    result = f'res1 : {res1}\nres2 : {res2}\nres3 : {res3}'
    print(result)

    return end - start

A = asyncio.run(main())
print(f'taken time is {A}')

def sync_main():

    start = time.time()
    for _ in range(10):
        res1 = requests.get('https://www.google.com')
        res2 = requests.get('https://www.naver.com')
        res3 = requests.get('https://www.daum.net')
    end = time.time()

    result = f'res1 : {res1}\nres2 : {res2}\nres3 : {res3}'
    print(result)
    return end - start



a = sync_main()
print(f'taken time is {a}')