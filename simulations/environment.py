from typing import Tuple
from enum import Enum

from dataclasses import dataclass

from simulations.utils import Constants


@dataclass
class ActorMoves(Enum):
    MOVE_UP = 0
    MOVE_RIGHT = 1
    MOVE_DOWN = 2
    MOVE_LEFT = 3
    STAY = 4


class ActorSensors(Enum):
    ACTOR_UP = 0
    ACTOR_RIGHT = 1
    ACTOR_DOWN = 2
    ACTOR_LEFT = 3
    FOOD_UP = 4
    FOOD_RIGHT = 5
    FOOD_DOWN = 6
    FOOD_LEFT = 7
    WALL_UP = 8
    WALL_RIGHT = 9
    WALL_DOWN = 10
    WALL_LEFT = 11


class Position:
    """Stores an object position in a 2D environment, in units"""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return f"Position( x = {self.x}, y = {self.y} )"

    def as_tuple(self) -> Tuple[int, int]:
        return self.x, self.y

    @classmethod
    def from_tuple(cls, position: Tuple[int, int]):
        return cls(*position)


class Environment:

    def __init__(self, width: int, height: int):

        self.width = width
        self.height = height

    def calculate_actor_move(self, position: Position, action_name: str):

        new_x = position.x
        new_y = position.y
        if action_name == ActorMoves.MOVE_UP.name:
            if position.y < self.height - 1:
                new_y += 1
        elif action_name == ActorMoves.MOVE_DOWN.name:
            if position.y > 0:
                new_y -= 1
        elif action_name == ActorMoves.MOVE_RIGHT.name:
            if position.x < self.width - 1:
                new_x += 1
        elif action_name == ActorMoves.MOVE_LEFT.name:
            if position.x > 0:
                new_x -= 1
        elif action_name == ActorMoves.STAY.name:
            pass
        else:
            raise ValueError(f"Actor move {action_name} not recognized.")

        return Position(new_x, new_y)


def main():
    pass


if __name__ == '__main__':
    main()
