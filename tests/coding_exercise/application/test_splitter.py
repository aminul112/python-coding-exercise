from assertpy import assert_that

from src.coding_exercise.application.splitter import Splitter
from src.coding_exercise.domain.model.cable import Cable


def test_should_not_return_none_when_splitting_cable():
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)).is_not_none()
