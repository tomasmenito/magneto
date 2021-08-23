import pytest

from magneto.mutant_identifier import SimpleMutantIdentifier
from magneto.sequence_generator import AllDirectionsSequenceGenerator
from magneto.sequence_identifier import SimpleSequenceIdentifier


class TestSimpleMutantIdentifier:
    @pytest.fixture
    def mutant_identifier(self):
        return SimpleMutantIdentifier(AllDirectionsSequenceGenerator(), SimpleSequenceIdentifier())

    @pytest.mark.parametrize(
        "matrix, expected",
        [
            (["ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"], False),
            (["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"], True),
        ],
    )
    def test_mutant_identifier(self, mutant_identifier, matrix, expected):
        result = mutant_identifier.is_mutant(matrix)
        assert result is expected
