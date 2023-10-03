from pathlib import Path
import sys

# directory reach
directory = Path(__file__).absolute().parent.parent.parent / "src"
 
# setting path
sys.path.insert(0, str(directory))

from bot import _echo, _start

def test_echo():
    assert _echo("hello") == "hello"

def test_start():
    assert _start() == "Hello, I'm your personal assistant <3 How can I help you?"