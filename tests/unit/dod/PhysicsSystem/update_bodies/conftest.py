import pytest
from .case_data import UpdateBodiesTestCase
from playground.dod.data.data import (
    PhysicsConfig,
    PhysicsBody,
    SimulationBox,
    Meters,
    Vector3,
    Seconds,
)
from playground.dod.systems.physics import PhysicsSystem


@pytest.fixture
def update_bodies_test_case() -> UpdateBodiesTestCase:
    return UpdateBodiesTestCase(
        physics_config=PhysicsConfig(
            time_step=Seconds(1),
            simulation_box=SimulationBox(
                x_length=Meters(10),
                y_length=Meters(10),
                z_length=Meters(10),
            ),
        ),
        physics_system=PhysicsSystem(),
        bodies=(
            PhysicsBody(
                position=Vector3(0., 0., 0.),
                velocity=Vector3(0., 0., 0),
            ),
        ),
        expected_bodies=(
            PhysicsBody(
                position=Vector3(0., 0., 0.),
                velocity=Vector3(0., 0., 0),
            ),
        ),
    )
