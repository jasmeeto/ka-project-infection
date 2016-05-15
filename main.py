import sys
import argparse
import graph
import infection
import os.path
from user import User
from datetime import datetime

def random_test():
    filename = 'output/random-%s.dat' % datetime.now().strftime('%Y-%m-%d_%H%M')
    print filename
    return filename

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help="input file location")
    parser.add_argument('type', help="total or limited")
    parser.add_argument('-s', '--source', help="source name")
    parser.add_argument('-l', '--limit', type=int, help="number to limit by")
    parser.add_argument('-v', '--visualize', action='store_true', help="number to limit by")
    parser.add_argument('-w', '--weighted', action='store_true', help="is the input weighted")
    parser.add_argument('-o', '--output', help="store to output (requires ffmpeg)")
    parser.add_argument('-g', '--graphviz', action='store_true', help="use graphviz to visualize (requires pygraphviz)")
    parser.add_argument('-r', '--random', action='store_true', help="use random test (creates new file in data folder)")

    args = parser.parse_args()

    if not os.path.isfile(args.input_file) and not r:
        print "need to give valid input file"
        exit(1)

    if args.random:
        args.input_file = random_test()

    g = graph.create_graph(args.input_file, args.weighted)
    iterations = []
    if args.type == "limited":
        if not args.limit:
            print "need to give valid limit for 'limited' option"
            exit(1)
        if args.source: 
            iterations = infection.limited_infection(g, args.source, args.limit)
        else: 
            iterations = infection.limited_infection(g, limit=args.limit)
    else: ##argtype total or anything
        if args.source: 
            iterations = infection.total_infection(g, args.source)
        else: 
            iterations = infection.total_infection(g)

    if args.visualize:
        graph.animate(g, iterations, args.output, args.graphviz, args.weighted)


if __name__ == "__main__":
    main()
