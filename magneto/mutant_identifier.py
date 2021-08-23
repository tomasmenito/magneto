from abc import ABC, abstractmethod
from typing import Sequence

from magneto.sequence_generator import SequenceGenerator
from magneto.sequence_identifier import SequenceIdentifier


class MutantIdentifier(ABC):
    def __init__(
        self,
        sequence_generator: SequenceGenerator,
        sequence_identifier: SequenceIdentifier,
        sequence_length: int = 4,
        minimum_sequences: int = 2,
    ):
        self.sequence_generator = sequence_generator
        self.sequence_identifier = sequence_identifier
        self.sequence_length = sequence_length
        self.minimum_sequences = minimum_sequences

    @abstractmethod
    def is_mutant(self, matrix: Sequence[Sequence[str]]) -> bool:
        raise NotImplementedError()


class SimpleMutantIdentifier(MutantIdentifier):
    def is_mutant(self, matrix: Sequence[Sequence[str]]) -> bool:
        count = 0
        for sequence in self.sequence_generator.generate_sequences(matrix):
            count += self.sequence_identifier.count_repeated_sequences(sequence, self.sequence_length)
            if count >= self.minimum_sequences:
                return True
        return False
