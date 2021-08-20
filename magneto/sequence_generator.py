from abc import ABC, abstractmethod
from typing import Iterable


class SequenceGenerator(ABC):
    @abstractmethod
    def generate_sequences(
        self,
    ) -> Iterable[Iterable[str]]:
        raise NotImplementedError()
