import itertools
from random import choice
from copy import deepcopy

import numpy as np
from dataclasses import dataclass

from simulations.environment import Position, ActorMoves
from simulations.game_entity import BaseId, GameEntity


@dataclass
class Tito:
    reaction_speed: float
    life_expectancy: int

    @classmethod
    def create_random(cls) -> 'Tito':
        reaction_speed = np.random.uniform(0, 1)
        life_expectancy = np.random.uniform(80, 120)
        return Tito(reaction_speed, life_expectancy)


class ActorID(BaseId):
    id_iter = itertools.count()

    @classmethod
    def generate_id(cls):
        """Generate a new ID"""
        idx = f"Tito-{next(ActorID.id_iter)}"
        return ActorID(idx)


class Actor(GameEntity):

    def __init__(self, actor: Tito, idx: ActorID, family: str):
        self.actor = actor
        self.age = 0
        self.family = family
        super().__init__(idx=idx)

    def __repr__(self):
        return f"{self.idx} , {hex(id(self))}"

    def as_json(self) -> dict:
        actor_json = deepcopy(self.actor.__dict__)
        actor_json.update({"age": self.age, "family": self.family, "id": self.idx.idx})
        return actor_json

    def move(self) -> str:
        return self.random_move()

    def increase_age(self):
        self.age += 1

    def has_to_die(self):
        return self.age >= self.actor.life_expectancy

    @staticmethod
    def random_move() -> str:
        return choice(ActorMoves.values_as_list())

    def has_priority(self, other: 'Actor'):
        return self.actor.reaction_speed > other.actor.reaction_speed

    @classmethod
    def generate_random(cls) -> 'Actor':
        actor = Tito.create_random()
        idx = ActorID.generate_id()
        return Actor(actor=actor, idx=idx, family=idx.idx)

    def reproduce(self) -> 'Actor':
        actor = deepcopy(self.actor)
        idx = ActorID.generate_id()
        return Actor(actor=actor, idx=idx, family=self.family)


@dataclass
class MovingActor:
    last_position: Position
    actor: Actor
    action: str
