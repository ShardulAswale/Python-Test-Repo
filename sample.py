# Version 7

def hello() -> str:
    """Return the default greeting."""
    return "Hello, world!"

def greet(name: str) -> str:
    """Return a personalized greeting."""
    return f"Hello, {name}!"

def sum_values(a: int = 2, b: int = 3) -> str:
    """Return a formatted sum of two numbers."""
    return f"Sum is {a + b}"

