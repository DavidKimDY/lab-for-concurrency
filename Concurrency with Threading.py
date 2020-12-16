import logging
import time
import threading

logger_format = '%(asctime)s:%(threadName)s:%(message)s'
logging.basicConfig(format=logger_format, level=logging.INFO, datefmt='%H:%M:%S')

num_word_mapping = {1: 'ONE', 2: 'TWO', 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT",
                   9: "NINE", 10: "TEN"}


def delay_message(delay):
    message = num_word_mapping[delay]
    logging.info(f'{message} received')
    time.sleep(delay)
    logging.info(f'Printing {message}')

def main():
    start = time.time()
    logging.info('Main started')
    threads = [threading.Thread(target=delay_message, args=delay) for delay in [[2], [3]]]

    for thread in threads:
        print(thread)
        thread.start()
    for thread in threads:
        thread.join()

    logging.info('Main Ended')
    end = time.time()
    logging.info(f'Taken time : {end - start}')

main()