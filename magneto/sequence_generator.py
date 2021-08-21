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
