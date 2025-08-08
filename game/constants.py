from __future__ import annotations

from typing import Final

from tcod.event import KeySym

DIRECTION_KEYS: Final = {
    #arrow keys
    KeySym.LEFT: (-1, 0),
    KeySym.RIGHT: (1, 0),
    KeySym.UP: (0, -1),
    KeySym.DOWN: (0, 1),
    #Arrow key diagonals
    KeySym.HOME: (-1, -1),
    KeySym.END: (-1, 1),
    KeySym.PAGEUP: (1, -1),
    KeySym.PAGEDOWN: (1, 1),
    #Keypad
    KeySym.KP_1: (-1, 1),
    KeySym.KP_2: (0, 1),
    KeySym.KP_3: (1, 1),
    KeySym.KP_4: (-1, 0),
    KeySym.KP_5: (0, 0),
    KeySym.KP_6: (1, 0),
    KeySym.KP_7: (-1, -1),
    KeySym.KP_8: (0, -1),
    KeySym.KP_9: (1, -1),
}