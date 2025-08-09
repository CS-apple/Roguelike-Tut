
""" Collection of common components"""
from __future__ import annotations

from typing import Final, Self

import attrs
import tcod.ecs.callbacks
from tcod.ecs import Entity

@attrs.define(frozen=True)
class Position:
    """An entities position """

    x: int
    y: int 

    def __add__(self, direction: tuple[int, int]) -> Self:
        """Add a vector to this position"""
        x, y = direction
        return self.__class__(self.x + x, self.y + y)

@tcod.ecs.callbacks.register_component_changed(component=Position)
def on_position_changed(entity: Entity, old: Position | None, new: Position | None) -> None:
    """Mirror positon components as a tag."""
    if old == new: # New position is equivilant to its previous value
        return # ignore and return 
    if old is not None: #Position component removed or changed 
        entity.tags.discard(old) #Remove old position from tags 
    if new is not None: #Position component added or changed 
        entity.tags.add(new) # Add new position to tags

@attrs.define(frozen=True)
class Graphic:
    """an entities color and icon """

    ch: int = ord("!")
    fg: tuple[int, int, int,] = [255, 255, 255]

Gold: Final = ("Gold", int)
"""Amount of gold"""
