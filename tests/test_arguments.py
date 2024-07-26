import os
from be_graph_local_py.cli.arguments import Arguments

def test_is_valid_file_path():
    parser = Arguments()
    arguments = parser.parse_args(['-f', 'data/doap.rdf'])
    assert os.path.isfile(arguments.f)