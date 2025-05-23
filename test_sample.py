import sample

def test_hello():
    assert sample.hello() == "Hello, world!"

def test_greet():
    assert sample.greet("Alice") == "Hello, Alice!"
