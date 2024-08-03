from typing import List
from rdflib import Graph, Namespace, Literal, XSD


def read_rdf(file_path) -> Graph:
    """
    Reads an RDF file and returns the parsed RDF graph.

    Args:
        file_path (str): The path to the RDF file.

    Returns:
        rdflib.Graph: The parsed RDF graph.

    """
    rdfGraph = Graph()
    rdfGraph.parse(file_path, format='xml')
    return rdfGraph


def get_project_name(rdfGraph: Graph) -> str:
    """
    Get the name of the project.

    Args:
        rdfGraph (Graph): The RDF graph.

    Returns:
        str: The name of the project.
    """
    DOAP = Namespace("http://usefulinc.com/ns/doap#")
    query = """
    SELECT ?name WHERE {
        ?project a doap:Project .
        ?project doap:name ?name .
    }
    """
    result = rdfGraph.query(query, initNs={'doap': DOAP})
    for row in result:
        return str(row.name)
    return "Project name not found"
