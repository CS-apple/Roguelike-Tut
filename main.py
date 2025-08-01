#!/usr/bin/env python3
from __future__ import annotations
import attrs
import tcod.context
import tcod.tileset 


def main() -> None:
    """Load a tileset and open a window using it, this window will immediatly close"""
    tileset = tcod.tileset.load_tilesheet(
        "data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
    )
    tcod.tileset.procedural_block_elements(tileset=tileset)
    console = tcod.console.Console(80, 60)
    console.print(0, 0, "Hello World") #test by printing "Hello World" to the console
    with tcod.context.new(console=console, tileset=tileset) as context:
        while True: # MAIN LOOP
            context.present(console) #render console to window and show it
            for event in tcod.event.wait(): # Event Loop, blocks until pending events exist
                print(event)
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit
    
if __name__ == "__main__":
    main()