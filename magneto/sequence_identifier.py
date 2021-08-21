from abc import ABC, abstractmethod
from typing import Iterable


class SequenceIdentifier(ABC):
    @abstractmethod
    def count_repeated_sequences(self, seq: Iterable[str], length: int) -> int:
        raise NotImplementedError()


class SimpleSequenceIdentifier(SequenceIdentifier):
    def count_repeated_sequences(self, seq: Iterable[str], length: int) -> int:
        sequences: int = 0
        last_letter: str = ""
        count: int = 0
        for element in seq:
            if last_letter != element:
                last_letter = element
                count = 1
            else:
                count += 1
                if count >= length:
                    sequences += 1
                    count = 0
        return sequences
