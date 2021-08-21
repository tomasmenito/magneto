from abc import ABC, abstractmethod
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
