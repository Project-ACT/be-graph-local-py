from rdflib import Graph, URIRef, Literal, XSD
from rdflib.namespace import RDF, FOAF


def example_01():
    """
    Creates an RDF graph, adds triples to the graph, and queries the graph for name and age information.

    Returns:
        None
    """
    # Create a new RDF graph
    g = Graph()

    # Define some URIs
    person_uri = URIRef("http://example.org/person/JohnDoe")
    name_uri = FOAF.name
    age_uri = FOAF.age

    # Add triples to the graph
    g.add((person_uri, RDF.type, FOAF.Person))
    g.add((person_uri, name_uri, Literal("John Doe", datatype=XSD.string)))
    g.add((person_uri, age_uri, Literal(42, datatype=XSD.integer)))

    # Query the graph
    query = """
    SELECT ?name ?age
    WHERE {
        ?person a foaf:Person .
        ?person foaf:name ?name .
        ?person foaf:age ?age .
    }
    """
    results = g.query(query)

    # Print the results
    for row in results:
        print(f"Name: {row.name}, Age: {row.age}")


def example_02():
    """
    Read a graph from a file.

    This function creates a Graph object and parses an RDF file hosted on the Internet.
    It then loops through each triple in the graph and checks if there is at least one triple.
    Finally, it prints the number of triples in the graph and the entire graph in the RDF Turtle format.
    """
    # Create a Graph
    g = Graph()

    # Parse in an RDF file hosted on the Internet
    g.parse("http://www.w3.org/People/Berners-Lee/card")

    # Loop through each triple in the graph (subj, pred, obj)
    for subj, pred, obj in g:
        # Check if there is at least one triple in the Graph
        if (subj, pred, obj) not in g:
            raise Exception("It better be!")

    # Print the number of "triples" in the Graph
    print(f"Graph g has {len(g)} statements.")
    # Prints: Graph g has 86 statements.

    # Print out the entire Graph in the RDF Turtle format
    print(g.serialize(format="turtle"))


def example_03():
    """
    This function demonstrates how to create a Graph using RDFLib and add triples to it.
    It also shows how to iterate over the triples in the graph and print them out.
    """
    # Create a Graph
    g = Graph()

    # Create an RDF URI node to use as the subject for multiple triples
    donna = URIRef("http://example.org/donna")

    # Add triples using store's add() method.
    g.add((donna, RDF.type, FOAF.Person))
    g.add((donna, FOAF.nick, Literal("donna", lang="en")))
    g.add((donna, FOAF.name, Literal("Donna Fales")))
    g.add((donna, FOAF.mbox, URIRef("mailto:donna@example.org")))

    # Add another person
    ed = URIRef("http://example.org/edward")

    # Add triples using store's add() method.
    g.add((ed, RDF.type, FOAF.Person))
    g.add((ed, FOAF.nick, Literal("ed", datatype=XSD.string)))
    g.add((ed, FOAF.name, Literal("Edward Scissorhands")))
    g.add((ed, FOAF.mbox, Literal("e.scissorhands@example.org", datatype=XSD.anyURI)))

    # Iterate over triples in store and print them out.
    print("--- printing raw triples ---")
    for s, p, o in g:
        print((s, p, o))

    # For each foaf:Person in the store, print out their mbox property's value.
    print("--- printing mboxes ---")
    for person in g.subjects(RDF.type, FOAF.Person):
        for mbox in g.objects(person, FOAF.mbox):
            print(mbox)

    # Bind the FOAF namespace to a prefix for more readable output
    g.bind("foaf", FOAF)

    # print all the data in the Notation3 format
    print("--- printing mboxes ---")
