"""
This script tests all the 
"""
from ...src.bot import _echo, _start


def test_echo():
    """Test if the `_echo` function will return
    any input string as output.
    """
    assert _echo("hello") == "hello"


def test_start():
    """Test if the `_start` function will return
    'Hello, I'm your personal assistant <3 How can I help you?'
    as output.
    """
    assert _start(
    ) == "Hello, I'm your personal assistant <3 How can I help you?"
