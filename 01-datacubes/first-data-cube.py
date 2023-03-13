#!/usr/bin/env python3
import csv

from rdflib import Graph, URIRef, BNode, Literal

'''
# Dimensions
ns:county a rdf:Property, qb:DimensionProperty ;
  rdfs:label "Okres"@cs, "County"@en ;
  rdfs:range xsd:string .

ns:region a rdf:Property, qb:DimensionProperty ;
  rdfs:label "Kraj"@cs, "Region"@en ;
  rdfs:range xsd:string .

ns:fieldOfCare a rdf:Property, qb:DimensionProperty ;
  rdfs:label "Obor péče"@cs, "Field of care"@en ;
  rdfs:range xsd:string .

# Measures
ns:numberOfCareProviders a rdf:Property, qb:MeasureProperty ;
  rdfs:label "Počet poskytovatelů péče"@cs,"Number of care providers"@en ;
  rdfs:range xsd:integer .

# Structure definition
ns:careProvider qb:DataStructureDefinition ;
  qb:component [ qb:dimension ns:county ; ] ;
  qb:component [ qb:dimension ns:region ; ] ;
  qb:component [ qb:dimension ns:fieldOfCare ; ] ;
  qb:component [ qb:measure ns:fieldOfCare ; ] .

# Instance
ns:dataCubeInstance qb:DataSet ;
  rdfs:label "Care providers"@en ;
  qb:structure ns:careProvider .
'''
def main():
    rdf = generate_rdf_data()
    print_rdf_as_trig(rdf)


def generate_rdf_data():
    result = Graph()
    prefix = "http://schafric.com/datacube-homework/"
    resource1 = URIRef(f"http://schafric.com/care-provider/1")
    result.add((resource1, URIRef(prefix + "county"), Literal("Praha")))
    result.add((resource1, URIRef(prefix + "region"), Literal("Praha")))
    result.add((resource1, URIRef(prefix + "fieldOfCare"), Literal("X")))
    result.add((resource1, URIRef(prefix + "numberOfCareProviders"), Literal(5)))

    return result


def print_rdf_as_trig(graph: Graph):
    print(graph.serialize(format="trig"))


if __name__ == "__main__":
    main()
