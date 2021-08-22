from abc import ABC, abstractmethod
from enum import Enum
from typing import Iterable, Sequence


class SequenceGenerator(ABC):
    @abstractmethod
    def generate_sequences(self, matrix: Sequence[Sequence[str]]) -> Iterable[Iterable[str]]:
        raise NotImplementedError()


class HorizontalSequenceGenerator(SequenceGenerator):
    def generate_sequences(self, matrix: Sequence[Sequence[str]]) -> Iterable[Iterable[str]]:
        for row in matrix:
            yield row


class VerticalSequenceGenerator(SequenceGenerator):
    def generate_sequences(self, matrix: Sequence[Sequence[str]]) -> Iterable[Iterable[str]]:
        length = len(matrix[0])
        for index in range(length):
            yield self._vertical_sequence(matrix, index)

    def _vertical_sequence(self, matrix: Sequence[Sequence[str]], index: int) -> Iterable[str]:
        for row in matrix:
            yield row[index]


class ObliqueSequenceGenerator(SequenceGenerator):
    class Direction(Enum):
        DOWN_RIGHT = 1
        DOWN_LEFT = 2

    def __init__(self, direction: Direction = Direction.DOWN_RIGHT):
        self.direction = direction

    def generate_sequences(self, matrix: Sequence[Sequence[str]]) -> Iterable[Iterable[str]]:
        height = len(matrix)
        width = len(matrix[0])
        if self.direction == self.Direction.DOWN_RIGHT:
            for row in reversed(range(height)):
                yield self._oblique_sequence(matrix, row, 0)
            for column in range(1, width):
                yield self._oblique_sequence(matrix, 0, column)
        elif self.direction == self.direction.DOWN_LEFT:
            for row in reversed(range(height)):
                yield self._oblique_sequence(matrix, row, width - 1)
            for column in reversed(range(0, width - 1)):
                yield self._oblique_sequence(matrix, 0, column)
        else:
            raise NotImplementedError()

    def _oblique_sequence(self, matrix: Sequence[Sequence[str]], row: int, column: int) -> Iterable[str]:
        if self.direction == self.Direction.DOWN_RIGHT:
            increment = 1
        elif self.direction == self.direction.DOWN_LEFT:
            increment = -1
        else:
            raise NotImplementedError()
        while True:
            try:
                yield matrix[row][column]
            except IndexError:
                break
            else:
                row += 1
                column += increment
                if column < 0:
                    break
