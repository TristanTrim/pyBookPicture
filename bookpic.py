
import argparse

parser = argparse.ArgumentParser(description='Tools for making Book-Pictures. They are not quite the same as Picture-Books.')
parser.add_argument('filename', metavar='f', type=str,
                           help='path to svg file.')

args = parser.parse_args()
print(args.filename)
import mkcolumns as mkclm
mkclm.mkcolumns(args.filename)

