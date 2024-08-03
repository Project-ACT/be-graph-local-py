from be_graph_local_py.cli.arguments import Arguments
from be_graph_local_py.rdf import read_rdf
from be_graph_local_py.rdf.rdf import get_project_name


def main():
    """
    Entry point of the program.
    """
    arguments = Arguments().parse_args()

    # Read an RDF file from the path provided by the "f" argument.
    rdf_graph = read_rdf(arguments.f)

    # Print project name.
    result = get_project_name(rdf_graph)
    print(result)


if __name__ == "__main__":
    main()
