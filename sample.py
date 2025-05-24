# version 6
def hello() -> str:
    return "Hello, world!"

def greet(name: str) -> str:
    return f"Hello, {name}!"

def sum_values(a: int = 2, b: int = 3) -> str:
    return f"Sum is {a + b}"
