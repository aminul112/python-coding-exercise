from assertpy import assert_that

from src.coding_exercise.application.splitter import Splitter
from src.coding_exercise.domain.model.cable import Cable

import pytest


def test_should_not_return_none_when_splitting_cable():
    assert_that(Splitter().split(Cable(10, "copper_cable"), 1)).is_not_none()


def test_should_raise_error_if_float_provided_for_times():
    given_cable = Cable(10, "copper_cable")
    with pytest.raises(ValueError) as exc_info:
        Splitter().split(given_cable, 5.6)
    assert exc_info.value.args[0] == "The number of times to split must be integer."


def test_should_raise_error_if_cable_is_not_a_true_instance():
    test_string: str = "abc"
    with pytest.raises(ValueError) as exc_info:
        Splitter().split(test_string, 5.6)
    assert exc_info.value.args[0] == "cable is not an object of Class Cable."


def test_split_even_length():
    given_cable = Cable(10, "copper_cable")
    result = Splitter().split(given_cable, 1)
    expected = [Cable(5, "copper_cable-00"), Cable(5, "copper_cable-01")]
    assert len(result) == 2
    assert result[0].length == expected[0].length
    assert result[1].length == expected[1].length


def test_split_odd_length():
    given_cable = Cable(5, "copper_cable")
    result = Splitter().split(given_cable, 2)
    expected = [
        Cable(1, "copper_cable-00"),
        Cable(1, "copper_cable-01"),
        Cable(1, "copper_cable-02"),
        Cable(1, "copper_cable-03"),
        Cable(1, "copper_cable-04"),
    ]
    assert len(result) == 5
    for i in range(5):
        assert result[i].length == expected[i].length
        assert result[i].name == expected[i].name


def test_split_with_remainder():
    given_cable = Cable(7, "copper_cable")
    result = Splitter().split(given_cable, 2)
    expected = [
        Cable(2, "copper_cable-00"),
        Cable(2, "copper_cable-01"),
        Cable(2, "copper_cable-02"),
        Cable(1, "copper_cable-03"),
    ]
    assert len(result) == 4
    for i in range(4):
        assert result[i].length == expected[i].length
        assert result[i].name == expected[i].name


def test_invalid_times():
    given_cable = Cable(10, "copper_cable")
    with pytest.raises(ValueError) as exc_info1:
        Splitter().split(given_cable, 0)
    assert (
        exc_info1.value.args[0]
        == "The number of times to split must be between 1 and 64 inclusive."
    )
    with pytest.raises(ValueError) as exc_info2:
        Splitter().split(given_cable, 65)
    assert (
        exc_info2.value.args[0]
        == "The number of times to split must be between 1 and 64 inclusive."
    )


def test_invalid_length():
    given_cable = Cable(1, "copper_cable")
    with pytest.raises(ValueError) as exc_info1:
        Splitter().split(given_cable, 1)
    assert (
        exc_info1.value.args[0] == "Cable length must be between 2 and 1024 inclusive."
    )
    given_cable = Cable(1025, "copper_cable")
    with pytest.raises(ValueError) as exc_info2:
        Splitter().split(given_cable, 1)
    assert (
        exc_info2.value.args[0] == "Cable length must be between 2 and 1024 inclusive."
    )


def test_split_length_less_than_1():
    given_cable = Cable(2, "copper_cable")
    with pytest.raises(ValueError) as exc_info:
        Splitter().split(given_cable, 2)
    assert exc_info.value.args[0] == "Resulting cable length can not be less than 1."
