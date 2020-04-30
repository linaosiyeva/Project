import random
from ete3 import Tree, NodeStyle, TreeStyle, NCBITaxa, faces

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

code_name = {
        "54263":"Ichthyosaura alpestris",
        "8324":"Lissotriton vulgaris",
        "8323":"Triturus cristatus",
        "8327":"Triturus dobrogicus",
        "8325":"Triturus karelinii ",
        "57571":"Salamandra salamandra ", 
        "323754":"Lissotriton montandoni"
        }

def mylayout(node):

    if node.is_leaf():
        longNameFace = faces.TextFace(code_name[node.name], fsize=15, fgcolor="green")
        faces.add_face_to_node(longNameFace, node, column=0)

ts = TreeStyle()
ts.layout_fn = mylayout
ts.scale = 100
my_tree.show(tree_style=ts)