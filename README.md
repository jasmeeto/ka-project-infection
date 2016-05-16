
## Khan Academy Limited Infection

### Requirements

1. `python 2.7` or greater
2. `networkx` (install with `pip install networkx`)
3. `matplotlib` (install with `pip install matplotlib`)
4. `pygraphviz` and `graphviz` (optional - results in better visualizations) 

### Usage

```bash
usage: main.py [-h] [-l LIMIT] [-t THRESHOLD] [-r RANDOM RANDOM] [-s SOURCE]
               [-i INPUT_FILE] [-w] [-v] [-o OUTPUT] [-g]
               type

positional arguments:
  type                  total or limited

optional arguments:
  -h, --help            show this help message and exit
  -l LIMIT, --limit LIMIT
                        number to limit by for limited
  -t THRESHOLD, --threshold THRESHOLD
                        threshold value for limited (defaults to 0)
  -r RANDOM RANDOM, --random RANDOM RANDOM
                        use random test, takes in num nodes and edge
                        probability as argument (creates new file in data
                        folder)
  -s SOURCE, --source SOURCE
                        source node name
  -i INPUT_FILE, --input_file INPUT_FILE
                        input file location
  -w, --weighted        is the input weighted
  -v, --visualize       whether or not to visualize graph
  -o OUTPUT, --output OUTPUT
                        store visualization to output - must be mp4 format - (requires ffmpeg) -
                        paired with -v option
  -g, --graphviz        (optional) use graphviz to visualize (requires pygraphviz)
```

The command line arguments are pretty self-explanatory.

#### Sample Usages
```
python main.py total -v -g -r 30 0.10 -w
```
The above runs total infection, with visualization, using graphviz, generating a randomized graph with 30 nodes and edge probability of 10% and is weighted.

Generated inputs are stored in `data/gen/` and generated outputs are stored in `output/gen/`

```
python main.py limited -l 6 -t 20 -v -g -r 30 0.10 -w
```
The above runs the same as example befoe, except it uses limited infection, with a limit of 6 nodes and a threshold of 20
These values are explained in section [Limited Infection](#limited-infection)

```
python main.py limited -l 4 -o output/limited.mp4 -v -g -w -i data/limited.dat -s 1
```
The above runs limited infection, with a limit of 4, with output file at output/limited.mp4, with visualization, using graphviz, weighted, with input file data/limited.dat and infection starting at node `1`

## Implementation
####Total Infection

####Limited Infection


