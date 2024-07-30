from typing import List

from src.coding_exercise.domain.model.cable import Cable

import structlog

logger = structlog.get_logger(__name__)


class Splitter:

    def __validate(self, cable: Cable, times: int) -> None:
        """
        Validates important parameter before a split operation.
        :param cable: Cable object.
        :param times: number of times the cable need to be split.
        :return: None
        """
        if not isinstance(cable, Cable):
            error = "cable is not an object of Class Cable."
            logger.error(error)
            raise ValueError(error)
        if not isinstance(times, int):
            error = "The number of times to split must be integer."
            logger.error(error)
            raise ValueError(error)
        if not (2 <= cable.length <= 1024):
            error = "Cable length must be between 2 and 1024 inclusive."
            logger.error(error)
            raise ValueError(error)

        if not (1 <= times <= 64):
            error = "The number of times to split must be between 1 and 64 inclusive."
            logger.error(error)
            raise ValueError(error)

    def split(self, cable: Cable, times: int) -> List[Cable]:
        """
        This will split the given cable according to rules provided by
        https://github.com/onlifeltd/python-coding-exercise
        :param cable: Cable object.
        :param times: number of times the cable need to be split.
        :return: a list of Cable object.
        """
        self.__validate(cable, times)

        generated_cables = []
        max_possible_initial_length = cable.length // (times + 1)

        if max_possible_initial_length < 1:
            raise ValueError("Resulting cable length can not be less than 1.")

        remaining_length = cable.length
        for i in range(times):
            if remaining_length < max_possible_initial_length:
                break
            generated_cables.append(
                Cable(max_possible_initial_length, f"{cable.name}-{str(i).zfill(2)}")
            )
            remaining_length -= max_possible_initial_length

        while remaining_length >= max_possible_initial_length:
            generated_cables.append(
                Cable(
                    max_possible_initial_length,
                    f"{cable.name}-{str(len(generated_cables)).zfill(2)}",
                )
            )
            remaining_length -= max_possible_initial_length

        if remaining_length > 0:
            generated_cables.append(
                Cable(
                    remaining_length,
                    f"{cable.name}-{str(len(generated_cables)).zfill(2)}",
                )
            )

        return generated_cables
