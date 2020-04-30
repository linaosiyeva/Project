from ete3 import NCBITaxa
ncbi = NCBITaxa()

tree = ncbi.get_topology([54263, 8324, 8323, 8327, 8325, 57571, 323754])
print (tree.get_ascii(attributes=["sci_name", "rank"]))


# 54263, 323754, 8324, 8323, 8327, 8325, 57571

#                                                             /-Triturus cristatus, species
#                                                            |
#                                              /Triturus, genus-Triturus karelinii, species
#                                             |              |
#                                             |               \-Triturus dobrogicus, species
#                                             |
#                      /Pleurodelinae, subfamily                 /-Lissotriton vulgaris, species
#                     |                       |-Lissotriton, genus
#                     |                       |                  \-Lissotriton montandoni, species
# -Salamandridae, family                      |
#                     |                        \-Ichthyosaura alpestris, species
#                     |
#                      \-Salamandra salamandra, species