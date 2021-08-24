from flask import Flask, Response, request

from magneto.mutant_identifier import SimpleMutantIdentifier
from magneto.sequence_generator import AllDirectionsSequenceGenerator
from magneto.sequence_identifier import SimpleSequenceIdentifier

app = Flask(__name__)

identifier = SimpleMutantIdentifier(AllDirectionsSequenceGenerator(), SimpleSequenceIdentifier())


@app.route("/mutant", methods=["POST"])
def mutant():
    is_mutant = identifier.is_mutant(request.json["dna"])
    return Response(status=200 if is_mutant else 403)
