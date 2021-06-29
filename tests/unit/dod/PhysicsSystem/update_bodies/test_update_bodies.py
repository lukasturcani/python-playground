import itertools
from .case_data import UpdateBodiesTestCase


def test_update_bodies(
    update_bodies_test_case: UpdateBodiesTestCase,
) -> None:
    """
    Test :meth:`.PhysicsSystem.update_bodies`.

    Parameters:
        update_bodies_test_case:
            The test case.

    """

    for actual_body, expected_body in itertools.zip_longest(
        update_bodies_test_case.physics_system.update_bodies(
            physics_config=update_bodies_test_case.physics_config,
            bodies=update_bodies_test_case.bodies,
        ),
        update_bodies_test_case.expected_bodies,
    ):
        assert actual_body == expected_body
