from typing import Tuple
from dataclasses import dataclass
from playground.dod.data.data import (
    PhysicsConfig,
    PhysicsBody,
)
from playground.dod.systems.physics import PhysicsSystem


@dataclass(frozen=True)
class PhysicsSystemTestCase:
    """
    Holds data for a test case.

    """

    physics_config: PhysicsConfig
    physics_system: PhysicsSystem
    bodies: Tuple[PhysicsBody]
    num_updates: int
