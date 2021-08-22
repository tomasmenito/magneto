import pytest

from magneto.sequence_generator import (
    ComposedSequenceGenerator,
    HorizontalSequenceGenerator,
    ObliqueSequenceGenerator,
    VerticalSequenceGenerator,
)


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


class TestObliqueSequenceGenerator:
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            (["aa"], ["a", "a"]),
            (["aa", "bb"], ["b", "ab", "a"]),
            (["ab", "cd"], ["c", "ad", "b"]),
        ],
    )
    def test_oblique_sequence_generator_down_right(self, matrix, expected):
        sequences = list(
            ObliqueSequenceGenerator(
                direction=ObliqueSequenceGenerator.Direction.DOWN_RIGHT
            ).generate_sequences(matrix)
        )
        assert ["".join(s) for s in sequences] == expected

    @pytest.mark.parametrize(
        "matrix, expected",
        [
            (["aa"], ["a", "a"]),
            (["aa", "bb"], ["b", "ab", "a"]),
            (["ab", "cd"], ["d", "bc", "a"]),
        ],
    )
    def test_oblique_sequence_generator_down_left(self, matrix, expected):
        sequences = list(
            ObliqueSequenceGenerator(
                direction=ObliqueSequenceGenerator.Direction.DOWN_LEFT
            ).generate_sequences(matrix)
        )
        assert ["".join(s) for s in sequences] == expected


class TestComposedGenerator:
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            (["aa"], ["aa", "a", "a"]),
            (["aa", "bb"], ["aa", "bb", "ab", "ab"]),
            (["ab", "cd"], ["ab", "cd", "ac", "bd"]),
        ],
    )
    def test_composed_generator(self, matrix, expected):
        composed = ComposedSequenceGenerator(HorizontalSequenceGenerator(), VerticalSequenceGenerator())
        assert ["".join(s) for s in composed.generate_sequences(matrix)] == expected
