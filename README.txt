Linked Data Based Construction Checking with OWL and SHACL

Overview

This repository demonstrates ontology-driven validation of construction schedule data using Web Ontology Language (OWL), Shapes Constraint Language (SHACL), and Python.

This repository is intended to be used alongside the dissertation: Integrating 4D Generative Scheduling into Construction Project Planning: A Framework for Workflow, Data Control, and Decision Governance in Minesite Maintenance EPCM Contracting.

The example implements a simplified Linked Data Based Construction Checking (LDCC) workflow to validate schedule information, semantic relationships, and task dependencies.

Technologies in use
RDF (Resource Description Framework)
OWL (Web Ontology Language)
SHACL (Shapes Constraint Language)
Turtle (.ttl)
Python
pySHACL

Repository Structure
ontology/
    ontology.ttl          # OWL ontology

shapes/
    schedule-shapes.ttl   # SHACL validation rules

data/
    valid-schedule.ttl
    invalid-dependency.ttl
    invalid-equipment.ttl

validate.py

README.txt

To use this code, install python and pyshacl.