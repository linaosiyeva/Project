
from ete3 import Tree, NodeStyle, TreeStyle, NCBITaxa

ncbi = NCBITaxa()

my_tree = ncbi.get_topology([54263, 8324, 8323, 8327, 8325, 57571, 323754])

ts = TreeStyle()
ts.show_leaf_name = True

for n in my_tree.traverse():
   nstyle = NodeStyle()
   nstyle["fgcolor"] = "yellow"
   nstyle["size"] = 10
   n.set_style(nstyle)

my_tree.img_style["size"] = 20
my_tree.img_style["fgcolor"] = "green"
ts.scale = 100
my_tree.show(tree_style=ts)