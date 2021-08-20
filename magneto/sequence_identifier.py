from abc import ABC, abstractmethod
from typing import Iterable


class SequenceIdentifier(ABC):
    @abstractmethod
    def count_repeated_sequences(self, seq: Iterable[str], length: int) -> int:
        raise NotImplementedError()
