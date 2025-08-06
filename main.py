#!/usr/bin/env python3
from __future__ import annotations
import attrs
import tcod.console
import tcod.context
import tcod.event
import tcod.tileset 
import g

@attrs.define()
class ExampleState:
    """Example state with hard coded player position"""
    player_x: int
    """Player X position, left most position is zero"""
    player_y: int
    """Player Y position, top-most psition is zero"""
    def on_draw(self, console: tcod.console.Console) -> None:
        """Draw the player glyph."""
        console.print(self.player_x, self.player_y, "@")
    def on_event(self, event: tcod.event.Event) -> None:
        match event:
            case tcod.event.Quit():
                raise SystemExit
            case tcod.event.KeyDown(sym=tcod.event.KeySym.LEFT) | tcod.event.KeyDown(sym=tcod.event.KeySym.A):
                self.player_x -= 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.RIGHT) | tcod.event.KeyDown(sym=tcod.event.KeySym.D):
                self.player_x += 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.UP) | tcod.event.KeyDown(sym=tcod.event.KeySym.W):
                self.player_y -= 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.DOWN) | tcod.event.KeyDown(sym=tcod.event.KeySym.S):
                self.player_y += 1
                

def main() -> None:
    """Load a tileset and open a window using it, this window will immediatly close"""
    tileset = tcod.tileset.load_tilesheet(
        "data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
    )
    tcod.tileset.procedural_block_elements(tileset=tileset)
    console = tcod.console.Console(80, 60)
    state =ExampleState(player_x=console.width // 2, player_y=console.height //2)
    with tcod.context.new(console=console, tileset=tileset) as g.context:
        while True: # MAIN LOOP
            console.clear() #clear console bfore drawing
            state.on_draw(console) #draw current state
            g.context.present(console) #render console to window and show it
            for event in tcod.event.wait(): # Event Loop, blocks until pending events exist
                print(event)
                state.on_event(event)
    
if __name__ == "__main__":
    main()