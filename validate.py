from pyshacl import validate

data_graph = "data/invalid-schedule.ttl"
shape_graph = "shapes/schedule-shapes.ttl"

conforms, report_graph, report_text = validate(
    data_graph,
    shacl_graph=shape_graph,
    inference="rdfs",
    abort_on_first=False
)

print("Conforms:", conforms)
print(report_text)
