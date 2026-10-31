from pyshacl import validate
import os

DATA_FILE = "data/invalid-equipment.ttl"
SHAPES_FILE = "shapes/schedule-shapes.ttl"
ONTOLOGY_FILE = "ontology/ontology.ttl"

print("=" * 60)
print("LDCC VALIDATION")
print("=" * 60)
print(f"Schedule File : {DATA_FILE}")
print(f"Shapes File   : {SHAPES_FILE}")
print(f"Ontology File : {ONTOLOGY_FILE}")
print()

conforms, report_graph, report_text = validate(
    DATA_FILE,
    shacl_graph=SHAPES_FILE,
    ont_graph=ONTOLOGY_FILE,
    inference="rdfs",
    abort_on_first=False
)

print("=" * 60)
print("RESULTS")
print("=" * 60)
print(f"Conforms: {conforms}")
print()
print(report_text)

input("\nPress Enter to exit...")