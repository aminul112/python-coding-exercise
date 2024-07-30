from src.coding_exercise.domain.model.cable import Cable


class Splitter:

    def __validate(self):
        valid = True
        if not valid:
            raise ValueError

    def split(self, cable: Cable, times: int) -> list[Cable]:
        self.__validate()

        return []
