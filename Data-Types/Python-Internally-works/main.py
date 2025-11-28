import dis

def multiply(a, b):
    return a * b

print("Bytecode for multiply():")
dis.dis(multiply)

print("Execution result:", multiply(6, 7))
