import random
from ete3 import Tree, TreeStyle, NodeStyle, faces, AttrFace, CircleFace, NCBITaxa

def layout(node):
    if node.is_leaf():
        N = AttrFace("name", fsize=10, fgcolor="black")
        faces.add_face_to_node(N, node, 0)
    if "weight" in node.features:
        C = CircleFace(radius=node.weight, color="blue", style="sphere")
        C.opacity = 0.3
        faces.add_face_to_node(C, node, 0, position="float")

def my_tree():
    ncbi = NCBITaxa()
    my_tree = ncbi.get_topology([54263, 8324, 8323, 8327, 8325, 57571, 323754])

    for n in my_tree.traverse():
        n.add_features(weight=random.randint(0, 50))

    ts = TreeStyle()

    ts.layout_fn = layout

    ts.mode = "c"

    ts.show_branch_length = True
    ts.show_branch_support = True
    my_tree.get_ascii(attributes=["sci_name", "rank"])
    return my_tree, ts

if __name__ == "__main__":
    my_tree, ts = my_tree()

    my_tree.show(tree_style=ts)