from tcod.ecs import Entity

import attrs
import tcod.ecs.callbacks

@attrs.define(frozen=True)
class Position:
    """An entities position """

    x: int
    y: int 

    def __add__(self, direction: tuple[int, int]) -> Self:
        """Add a vector to this position"""
        x, y = direction
        return self.__class__(self.x + x, self.y + y)

tcod.ecs.callbacks.register_component_changed(component=Position)
def on_position_changed (entity: Entity, old: Position | None, new: Position | None)
    """Mirror positon components as a tag."""
    if old == new: # New position is equivilant to its previous value
        return # ignore and return 
    if old is not None: #Position component removed or changed 
        entity.tags.discard(old) #Remove old position from tags 
    if new is not None: #Position component added or changed 
        entity.tags.add(new) # Add new position to tags