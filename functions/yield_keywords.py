def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
    print(next(gen))


def echo_generator():
    while True:
        received = yield
        print("Received:", received)


gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")
gen.send("World")


def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")


gen = my_gen()
print(next(gen))
gen.close()
