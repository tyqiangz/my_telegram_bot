"""
This script tests all the 
"""
from ...my_telegram_bot.bot import _start


def test_start():
    """Test if the `_start` function will return
    'Hello, I'm your personal assistant <3 How can I help you?'
    as output.
    """
    assert _start(
    ) == "Hello, I'm your personal assistant <3 How can I help you?"
