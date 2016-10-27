# IgraphNetworkXIntroduction

A basic introduction to the python packages available for network creation, manipulation and analyzation: NetworkX and Igraph. Both packages are used in Python 2.7.

# data 

The folder [Igraph](https://github.com/AuelJonas/IgraphNetworkXIntroduction/tree/master/Igraph "Igraph") contains a jupyter notebook with basic network operations using igraph. If you don't have jupyter notebook installed, you can also use the [igraph_python.py](https://github.com/AuelJonas/IgraphNetworkXIntroduction/blob/master/Igraph/igraph_python.py "igraph_python.py") file. Additionally there is a real world data network polblogs.gml which is used in the python scripts.

The [NetworkX](https://github.com/AuelJonas/IgraphNetworkXIntroduction/tree/master/NetworkX "NetworkX") folder similary contains a NetworkX jupyter notebook and the corresponding [NetworkX.py](https://github.com/AuelJonas/IgraphNetworkXIntroduction/blob/master/NetworkX/NetworkX.py "NetworkX.py"). As a real world data network dolphins.gml is used in the python scripts. 

The real world datasets are taken from:
http://www-personal.umich.edu/~mejn/netdata/

The folder [Praesentation](https://github.com/AuelJonas/IgraphNetworkXIntroduction/tree/master/Praesentation "Praesentation") contains a beamer presentation about these two packages with some useful references.

# usage

To run the .py files in your linux terminal use
<pre><code> python igraph_python.py </code></pre>
or
<pre><code> python NetworkX.py </code></pre>
in the corresponding folder.

If you'd rather use the jupyter notebooks, you can easily install it here:
https://www.continuum.io/downloads .

After installation just run 
<pre><code> jupyter notebook </code></pre>
in your terminal to open a local notebook server in your browser. You can then select the notebooks provided and run them.