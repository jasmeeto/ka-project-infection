#!/bin/bash
# total infection gen random test
#python main.py total -v -g -r 30 0.10 -w

# limited infection gen random test with limit 6
#python main.py limited -l 6 -v -g -r 30 0.10 -w

# limited infection test for edge case in customized bfs
#python main.py limited -l 4 -o output/limited.mp4 -v -g -w -i data/limited.dat -s 1

# run limited test
#python main.py limited -l 5 -i data/gen/random-2016-05-16_0310.dat -o output/test.mp4 -v -g -w -s 9

# run total test
#python main.py total -i data/gen/random-2016-05-16_0310.dat -o output/test.mp4 -v -g -w -s 2

# run cutsom total test
python main.py total -i data/weighted.dat -o output/test.mp4 -v -g -w -s 'Sal'