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

# Measures
ns:meanPopulation a rdf:Property, qb:MeasureProperty ;
  rdfs:label "Střední stav obyvatel"@cs,"Mean population"@en ;
  rdfs:range xsd:integer .

# Structure definition
ns:population qb:DataStructureDefinition ;
  qb:component [ qb:dimension ns:county ; ] ;
  qb:component [ qb:dimension ns:region ; ] ;
  qb:component [ qb:measure ns:meanPopulation ; ] .

# Instance
ns:dataCubeInstance qb:DataSet ;
  rdfs:label "Population"@en ;
  qb:structure ns:population .

'''
def main():
    rdf = generate_rdf_data()
    print_rdf_as_trig(rdf)


def generate_rdf_data():
    result = Graph()
    prefix = "http://schafric.com/datacube-homework/"
    resource1 = URIRef(f"http://schafric.com/population/1")
    result.add((resource1, URIRef(prefix + "county"), Literal("Praha")))
    result.add((resource1, URIRef(prefix + "region"), Literal("Praha")))
    result.add((resource1, URIRef(prefix + "meanPopulation"), Literal(1000000)))

    return result


def print_rdf_as_trig(graph: Graph):
    print(graph.serialize(format="trig"))


if __name__ == "__main__":
    main()
