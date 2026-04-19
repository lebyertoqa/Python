"""Tests for the fibonacci module."""

import pytest

from maths.fibonacci import fibonacci_iterative, fibonacci_recursive, fibonacci_sequence


FIBONACCI_NUMBERS = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
]


@pytest.mark.parametrize("n, expected", FIBONACCI_NUMBERS)
def test_fibonacci_recursive(n: int, expected: int) -> None:
    assert fibonacci_recursive(n) == expected


@pytest.mark.parametrize("n, expected", FIBONACCI_NUMBERS)
def test_fibonacci_iterative(n: int, expected: int) -> None:
    assert fibonacci_iterative(n) == expected


def test_fibonacci_recursive_negative() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        fibonacci_recursive(-1)


def test_fibonacci_iterative_negative() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        fibonacci_iterative(-1)


def test_fibonacci_sequence_basic() -> None:
    assert fibonacci_sequence(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_fibonacci_sequence_zero() -> None:
    assert fibonacci_sequence(0) == [0]


def test_fibonacci_sequence_one() -> None:
    assert fibonacci_sequence(1) == [0, 1, 1]


def test_fibonacci_sequence_negative() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        fibonacci_sequence(-5)


def test_both_implementations_agree() -> None:
    for n in range(30):
        assert fibonacci_recursive(n) == fibonacci_iterative(n)
