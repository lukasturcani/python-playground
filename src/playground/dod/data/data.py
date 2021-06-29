"""
Data
====

"""

from typing import NewType
from dataclasses import dataclass
from .vector3 import Vector3


@dataclass(frozen=True)
class PhysicsBody:
    """
    Holds physics data.

    Parameters:

        position:
            The position of the body.

        velocity:
            The velocity of the body.

    """

    __slots__ = ['position', 'velocity']

    position: Vector3
    velocity: Vector3


Seconds = NewType('Seconds', float)
Meters = NewType('Meters', float)


@dataclass(frozen=True)
class SimulationBox:
    """
    The box in which the physics bodies should be contained.

    Parameters:

        x_length:
            The size of the box in the x dimension.

        y_length:
            The size of the box in the y dimension.

        z_length:
            The size of the box in the z dimension.

    """

    x_length: Meters
    y_length: Meters
    z_length: Meters


@dataclass(frozen=True)
class PhysicsConfig:
    """
    Configuration for :class:`.PhysicsSystem`.

    Parameters:

        time_step:
            The size of the time step.

        simulation_box:
            The box in which the physics bodies should be contained.

    """

    __slots__ = ['time_step', 'simulation_box']

    time_step: Seconds
    simulation_box: SimulationBox


@dataclass(frozen=True)
class Data:
    """
    Holds the data required by the simulation.

    Parameters:

        physics_config:
            The configuration for the :class:`.PhysicsSystem`.

        physics_bodies:
            The physics bodies in the simulation.

    """

    __slots__ = ['physics_config', 'physics_bodies']

    physics_config: PhysicsConfig
    physics_bodies: tuple[PhysicsBody, ...]
