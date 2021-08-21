import pytest

from magneto.sequence_identifier import SimpleSequenceIdentifier


class TestSimpleSequenceIdentifier:
    @pytest.mark.parametrize(
        "sequence, length, expected",
        [
            ("", 2, 0),
            ("a", 2, 0),
            ("aa", 2, 1),
            ("aaa", 2, 1),
            ("aaaa", 2, 2),
            ("aabaa", 2, 2),
            ("abab", 2, 0),
            ("abaa", 2, 1),
            ("aabb", 2, 2),
        ],
    )
    def test_simple_sequences(self, sequence, length, expected):
        assert SimpleSequenceIdentifier().count_repeated_sequences(sequence, length) == expected
