import pytest

from magneto.sequence_generator import HorizontalSequenceGenerator, VerticalSequenceGenerator


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


class TestVerticalSequenceGenerator:
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            (["aa"], ["a", "a"]),
            (["aa", "bb"], ["ab", "ab"]),
            (["ab", "cd"], ["ac", "bd"]),
        ],
    )
    def test_vertical_sequence_generator(self, matrix, expected):
        sequences = list(VerticalSequenceGenerator().generate_sequences(matrix))
        assert ["".join(s) for s in sequences] == expected
