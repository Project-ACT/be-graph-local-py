import argparse

parser = argparse.ArgumentParser(description="Process some RDF data.")
parser.add_argument('-f', metavar="Files", type=str, required=False, help="Parse RDF or n3 file.")
parser.add_argument('files', metavar="Files", type=str, nargs='*', help='Parse RDF or n3 file.')
# parser.add_argument('--sum', dest='accumulate', action='store_const', required=False,
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
parser.parse_args()
