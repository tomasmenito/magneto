# Magneto

This project identifies mutant dna sequences. A DNA is mutant if it has 2 or more sequences of 4 equal letters. Sequences can be formed in horizontal, vertical or oblique directions.

### Resources

Flask is being used to serve 2 endpoints:
- mutant: endponit that receives a post with the dna sequence and answers status code 200 if is mutant and status code 403 otherwise
- stats: endponit that gives status about identified dna

DynamoDB is being used as database for the stats, and serverless is being used to deploy all the stack on aws (api gateway + lambda + dynamodb)
