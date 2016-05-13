import sys
import argparse
import graph
import infection
import os.path
from user import User


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help="input file location")
    parser.add_argument('type', help="total or limited")
    parser.add_argument('--source', help="source name")
    parser.add_argument('--limit', type=int, help="number to limit by")

    args = parser.parse_args()

    if not os.path.isfile(args.input_file):
        print "need to give valid input file"
        exit(1)

    if args.type == "total":
        g = graph.create_graph(args.input_file)
        if args.source: 
            infection.total_infection(g, args.source)
        else: 
            infection.total_infection(g)
        graph.draw(g)

if __name__ == "__main__":
    main()

