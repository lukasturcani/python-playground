"""
Vector3
=======

"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Vector3:
    """
    A vector.

    Parameters:

        x: The x value.
        y: The y value.
        z: The z value.

    """

    __slots__ = ['x', 'y', 'z']

    x: float
    y: float
    z: float


def add_scalar(vector: Vector3, scalar: float) -> Vector3:
    """
    Add a `vector` to a `scalar`.

    Parameters:

        vector: The vector.

        scalar: The scalar.

    Returns:

        A new vector.

    """

    return Vector3(
        x=vector.x+scalar,
        y=vector.y+scalar,
        z=vector.z+scalar,
    )


def add_vector(vector1: Vector3, vector2: Vector3) -> Vector3:
    """
    Add two vectors.

    Parameters:

        vector1: The first vector.

        vector2: The second vector.

    Returns:

        A new vector.

    """

    return Vector3(
        x=vector1.x+vector2.x,
        y=vector1.y+vector2.y,
        z=vector1.z+vector2.z,
    )


def multiply_scalar(vector: Vector3, scalar: float) -> Vector3:
    """
    Multiply a vector by a scalar.

    Parameters:

        vector: The vector.

        scalar: The scalar.

    Returns:

        A new vector.

    """

    return Vector3(
        x=vector.x*scalar,
        y=vector.y*scalar,
        z=vector.z*scalar,
    )
