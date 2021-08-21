import pytest

from magneto.sequence_generator import HorizontalSequenceGenerator


class TestHorizontalSequenceGenerator:
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            (["aa"], ["aa"]),
            (["aa", "bb"], ["aa", "bb"]),
            (["ab", "cd"], ["ab", "cd"]),
        ],
    )
    def test_horizontal_sequence_generator(self, matrix, expected):
        sequences = list(HorizontalSequenceGenerator().generate_sequences(matrix))
        assert sequences == expected
