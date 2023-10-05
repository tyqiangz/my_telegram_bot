from src.bot import application

def test_echo():
    assert bot._echo("hello") == "hello"

def test_start():
    assert bot._start() == "Hello, I'm your personal assistant <3 How can I help you?"