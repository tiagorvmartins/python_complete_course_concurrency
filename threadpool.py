import time
from concurrent.futures import ThreadPoolExecutor


def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user, {time.time() - start}')


def complex_calculation():
    start = time.time()
    print('Started calculating...')
    [x**2 for x in range(20000000)]
    print(f'Complex_calculation, {time.time() - start}')


start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time() - start}')

start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:   # waits for the pool to finish
    pool.submit(complex_calculation)
    pool.submit(ask_user)

# or if u dont use the with, then use pool.shutdown() - blocking operation

print(f'Two thread total time: {time.time() - start}')