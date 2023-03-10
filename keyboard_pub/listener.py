import time
from enum import Enum
from typing import Union

from pynput.keyboard._xorg import KeyCode

from keyboard_pub.patch.keys import keyboard
from keyboard_pub.storage import memory


def on_press(key: Union[Enum, KeyCode]) -> None:
    if isinstance(key, Enum):
        key = key.value
    if key.char is None:
        return
    memory.last = time.time()
    memory.seq.append(key.char)


def start() -> None:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
