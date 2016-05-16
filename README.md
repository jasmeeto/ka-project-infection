
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
The above runs limited infection, with a limit of 4, with output file at output/limited.mp4, with visualization, using graphviz, weighted, with input file data/limited.dat and infection starting at node '1'

## Testing
Follow examples in `test.sh` to run tests. Again it is relatively easy to create random cases and execute from command line so the need for a full test suite was not prevalent.

## Implementation

#### Input
The input is a directed graph with possibly weighted edges to be used in limited infection.

The following represents a directed edge from node `4` to node `21` which semantically means that `4` coaches `21` and `21` is coached by `4`.

![Directed](https://cloud.githubusercontent.com/assets/1384045/15299835/0d9ab7f6-1b74-11e6-83e0-9b8a7edb97d1.png)
####Total Infection

Total infection essentially runs a BFS on the provided source node and infects the whole connected component containing that node. If a source node is not provided then it randomly picks a node using `np.random.choice(g.nodes())`.

BFS is used to ensure the requirement that `"each teacher-student pair should be on the same version of the site"`

In total infection the direction is not important since we infect the entire component anyway, so the graph is converted to an undirected graph and then run with the bfs python edge generator created by networkx using this function [here](https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.traversal.breadth_first_search.bfs_edges.html)

Example Output (`'Sal'` is source node):
![total](https://cloud.githubusercontent.com/assets/1384045/15300158/378c931c-1b75-11e6-94a3-81a7be08d206.PNG)

####Limited Infection

Limited infection is implemented quite differently taking a few heuristics into account.

The first heuristic considered is `"Ideally we’d like a coach and all of their students to either have a feature or not."`


