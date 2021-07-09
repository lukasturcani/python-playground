from .case_data import PhysicsSystemTestCase


def test_physics_system(
    benchmark,
    physics_system_test_case: PhysicsSystemTestCase,
) -> None:
    """
    Test :meth:`.PhysicsSystem.update_bodies`.

    Parameters:

        update_bodies_test_case:
            The test case.

    """

    benchmark(_test_physics_system, physics_system_test_case)


def _test_physics_system(
    test_case: PhysicsSystemTestCase,
) -> None:

    bodies = test_case.bodies
    for _ in range(test_case.num_updates):
        bodies = tuple(test_case.physics_system.update_bodies(
            physics_config=test_case.physics_config,
            bodies=bodies,
        ))
