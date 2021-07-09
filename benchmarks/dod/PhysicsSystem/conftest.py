import pytest
from .case_data import PhysicsSystemTestCase
from playground.dod.data.data import (
    PhysicsConfig,
    PhysicsBody,
    SimulationBox,
    Meters,
    Vector3,
    Seconds,
)
from playground.dod.systems.physics import PhysicsSystem


@pytest.fixture(
    params=(
        1,
        10,
        100,
        1000,
    ),
)
def num_updates(request) -> int:
    return request.param


@pytest.fixture
def physics_system_test_case(
    num_updates: int,
) -> PhysicsSystemTestCase:

    return PhysicsSystemTestCase(
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
        num_updates=num_updates,
    )
