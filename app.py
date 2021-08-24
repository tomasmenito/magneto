from flask import Flask, Response, request

from database import DynamoDBDatabase
from magneto.mutant_identifier import SimpleMutantIdentifier
from magneto.sequence_generator import AllDirectionsSequenceGenerator
from magneto.sequence_identifier import SimpleSequenceIdentifier

app = Flask(__name__)

identifier = SimpleMutantIdentifier(AllDirectionsSequenceGenerator(), SimpleSequenceIdentifier())

database = DynamoDBDatabase()


@app.route("/mutant", methods=["POST"])
def mutant():
    dna_row = request.json["dna"]
    is_mutant = identifier.is_mutant(dna_row)
    database.create_record(dna_row, is_mutant)
    return Response(status=200 if is_mutant else 403)


@app.route("/stats", methods=["GET"])
def stats():
    return database.stats()
