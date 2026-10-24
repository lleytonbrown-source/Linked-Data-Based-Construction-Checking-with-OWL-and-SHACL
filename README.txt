Linked Data Based Construction Checking with OWL and SHACL
Overview
This repository demonstrates ontology-driven validation of construction schedules using OWL and SHACL.

Technologies
RDF
OWL
SHACL
Turtle
Python
pySHACL
Repository Structure
ontology/ OWL ontology data/ Example schedules shapes/ SHACL validation rules results/ Validation reports

Validation
Install:

pip install -r requirements.txt

Run:

python validate.py

Expected Result:

Conforms: True (valid schedule)

or

Conforms: False (invalid schedule)