def greet():
    friend = yield
    print(f'Hello, {friend}')

g = greet()
g.send(None) # priming the generator  (runs right before the yield)
g.send('Adam')