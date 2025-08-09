""" A collection of game states"""

from __future__ import annotations

import attrs
import tcod.console
import tcod.event

import g
from game.components import Gold, Graphic, Position
from game.constants import DIRECTION_KEYS
from game.tags import IsItem, IsPlayer


@attrs.define()
class InGame:
    """Primary Game State"""
    def on_event(self, event: tcod.event.Event) -> None:
        """Handle events for the in-game state"""
        (player,) = g.world.Q.all_of(tags=[IsPlayer])
        match event:
            case tcod.event.Quit():
                raise SystemExit()
            case tcod.event.KeyDown(sym=sym) if sym in DIRECTION_KEYS:
                player.components[Position] += DIRECTION_KEYS[sym]
                print(player.components[Position])
                #auto pick up gold
                for gold in g.world.Q.all_of(components=[Gold], tags=[player.components[Position], IsItem]):
                    print("found gold")
                    player.components[Gold] += gold.components[Gold]
                    print("added gold")
                    text = f"Picked up {gold.components[Gold]}g, total: {player.components[Gold]}g"
                    g.world[None].components["Text", str] = text
                    print("picked up gold")
                    gold.clear()
                    print("delete gold")

    def on_draw(self, console: tcod.console.Console) -> None:
        """Draw the standard screen"""
        for entity in g.world.Q.all_of(components=[Position, Graphic]):
            pos = entity.components[Position]
            if not (0 <= pos.x < console.width and 0 <= pos.y <console.height):
                continue
            graphic = entity.components[Graphic]
            console.rgb[["ch", "fg"]][pos.y, pos.x] = graphic.ch, graphic.fg

        if text := g.world[None].components.get(("Text", str)):
            console.print(x=0, y=console.height -2, text= text, fg=(255, 255, 255), bg=(0, 0, 0))
