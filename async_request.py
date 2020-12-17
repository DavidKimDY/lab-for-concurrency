import requests
import asyncio
import json
import time

with open('CLO.json', 'r', encoding='utf-8') as f:
     data = (data for data in json.load(f))

print(data.__next__()['url'])

async def main():

    loop = asyncio.get_event_loop()
    start = time.time()

    futrue1 = loop.run_in_executor(None, requests.get, 'https://www.google.com')
    futrue2 = loop.run_in_executor(None, requests.get, 'https://www.google.com')
    futrue3 = loop.run_in_executor(None, requests.get, 'https://www.google.com')
    for i in range(10):
        print(f'start {i}')
        res1 = await futrue1
        res2 = await futrue2
        res3 = await futrue3
        print(f'end {i} {res1} {res2} {res3}')

    end = time.time()
    print(end - start)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


