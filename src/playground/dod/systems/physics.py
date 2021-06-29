"""
Physics System
==============

"""

from typing import Iterable
from playground.dod.data.vector3 import (
    add_vector,
    multiply_scalar,
)
from playground.dod.data.data import (
    PhysicsConfig,
    PhysicsBody,
    Seconds,
)


class PhysicsSystem:
    """
    Updates the positions and velocities.

    """

    def update_bodies(
        self,
        physics_config: PhysicsConfig,
        bodies: Iterable[PhysicsBody],
    ) -> Iterable[PhysicsBody]:
        """
        Update the position and velocities of `bodies`.

        Parameters:

            physics_config:
                The configuration for the update step.

            bodies:
                The bodies to update.

        Yields:

            An updated :class:`.PhysicsBody`.

        """

        for body in bodies:
            yield self._update_body(physics_config.time_step, body)

    def _update_body(
        self,
        time_step: Seconds,
        body: PhysicsBody,
    ) -> PhysicsBody:

        return PhysicsBody(
            position=add_vector(
                vector1=body.position,
                vector2=multiply_scalar(body.velocity, time_step),
            ),
            velocity=body.velocity,
        )
