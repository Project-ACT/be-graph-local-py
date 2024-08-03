import argparse


def Arguments() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser for the command-line interface.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    parser = argparse.ArgumentParser(description="Process some RDF data.")
    parser.add_argument('-f', metavar="Files", type=str, required=False, help="Parse RDF or n3 file.")
    parser.add_argument('files', metavar="Files", type=str, nargs='*', help='Parse RDF or n3 file.')
    return parser
