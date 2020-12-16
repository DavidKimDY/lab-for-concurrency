import logging
import time
import asyncio

logger_format = '%(asctime)s:%(threadName)s:%(message)s'
logging.basicConfig(format=logger_format, level=logging.INFO, datefmt='%H:%M:%S')

num_word_mapping = {1: 'ONE', 2: 'TWO', 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT",
                   9: "NINE", 10: "TEN"}


async def delay_message(delay):
    message = num_word_mapping[delay]
    logging.info(f'{message} received')
    await asyncio.sleep(delay)
    logging.info(f'Printing {message}')
    return message


async def main():
    start = time.time()
    logging.info('Main started')
    logging.info('Creating multiple tasks with asyncio.gather')
    await asyncio.gather(delay_message(2), delay_message(3))
    logging.info('Main Ended')
    end = time.time()
    logging.info(f'Taken time : {end - start}')

if __name__ == '__main__':
    asyncio.run(main())