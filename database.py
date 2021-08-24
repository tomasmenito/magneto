import json
from abc import ABC, abstractmethod
from numbers import Number
from typing import Sequence

import boto3
from boto3.dynamodb.conditions import Key


class Database(ABC):
    @abstractmethod
    def create_record(self, dna_row: Sequence[Sequence[str]], is_mutant: bool):
        raise NotImplementedError()

    @abstractmethod
    def stats(self) -> dict[str, Number]:
        raise NotImplementedError()


class DynamoDBDatabase:
    def __init__(self, table_name: str = "mutant"):
        self.table_name = table_name
        self.table = boto3.resource("dynamodb").Table(self.table_name)

    def create_record(self, dna_row: Sequence[Sequence[str]], is_mutant: bool):
        return self.table.put_item(Item={"is_mutant": int(is_mutant), "dna_rows": json.dumps(dna_row)})

    def stats(self) -> dict[str, Number]:
        stats = {
            "count_mutant_dna": self.mutant_count(True),
            "count_human_dna": self.mutant_count(False),
        }
        try:
            ratio: float = stats["count_mutant_dna"] / (stats["count_mutant_dna"] + stats["count_human_dna"])
        except ZeroDivisionError:
            ratio = 0.0
        stats["ratio"] = ratio
        return stats

    def mutant_count(self, is_mutant: bool) -> int:
        return self.table.query(Select="COUNT", KeyConditionExpression=Key("is_mutant").eq(int(is_mutant)))[
            "Count"
        ]
