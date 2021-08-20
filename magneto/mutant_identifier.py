from typing import Sequence

from magneto.sequence_generator import SequenceGenerator
from magneto.sequence_identifier import SequenceIdentifier


class MutantIdentifier:
    def __init__(self, sequence_generator: SequenceGenerator, sequence_identifier: SequenceIdentifier):
        self.sequence_generator = sequence_generator
        self.sequence_identifier = sequence_identifier

    def is_mutant(self, dna_rows: Sequence[Sequence[str]]) -> bool:
        return False
