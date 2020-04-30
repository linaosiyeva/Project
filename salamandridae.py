from ete3 import NCBITaxa
ncbi = NCBITaxa()

descendants = ncbi.get_descendant_taxa('Salamandridae')
print (ncbi.translate_to_names(descendants))

descendants = ncbi.get_descendant_taxa('Salamandridae', collapse_subspecies=True)
print (ncbi.translate_to_names(descendants))

tree = ncbi.get_descendant_taxa('Salamandridae', collapse_subspecies=True, return_tree=True)
print (tree.get_ascii(attributes=['sci_name', 'taxid']))

# ['Notophthalmus viridescens', 'Notophthalmus perstriatus', 'Notophthalmus meridionalis kallerti', 
# 'Notophthalmus meridionalis meridionalis', 'Pleurodeles waltl waltl', 'Pleurodeles poireti', 
# 'Pleurodeles nebulosus', 'Taricha granulosa', 'Taricha rivularis', 'Taricha torosa torosa', 
# 'Taricha torosa sierrae', 'Taricha sp. AMNH A168420', 'Triturus cristatus', 
# 'Triturus karelinii arntzeni', 'Triturus karelinii karelinii', 'Triturus carnifex carnifex', 
# 'Triturus dobrogicus dobrogicus', 'Triturus dobrogicus macrosomus', 'Triturus marmoratus marmoratus', 
# 'Triturus pygmaeus', 'Triturus macedonicus', 'Triturus cristatus x Triturus dobrogicus macrosomus', 
# 'Triturus cristatus s.l. AH-2007', "Triturus cf. karelinii 'eastern'", "Triturus cf. karelinii 'western'", 
# 'Triturus ivanbureschi', 'Triturus anatolicus', 'Cynops pyrrhogaster', 'Cynops ensicauda', 
# 'Cynops orientalis', 'Cynops cyanurus chuxiongensis', 'Cynops cyanurus cyanurus', 'Cynops orphicus', 
# 'Cynops fudingensis', 'Cynops glaucus', 'Euproctus montanus', 'Euproctus platycephalus', 
# 'Tylototriton taliangensis', 'Tylototriton verrucosus pulcherrima', 'Tylototriton shanjing', 
# 'Tylototriton kweichowensis', 
# Tylototriton sp. MH-2011', 'Tylototriton pseudoverrucosus', 'Tylototriton yangi', 'Tylototriton uyenoi', 
# 'Tylototriton shanorum', 'Tylototriton anguliceps', 'Tylototriton daweishanensis', 
# 'Tylototriton podichthys', 'Tylototriton himalayanus', 'Tylototriton ngarsuensis', 
# 'Tylototriton kachinorum', 'Tylototriton asperrimus', 'Tylototriton hainanensis', 
# 'Tylototriton cf. vietnamensis DWW-2006', 'Tylototriton wenxianensis dabienicus', 'Tylototriton notialis', 
# 'Tylototriton vietnamensis', 'Tylototriton cf. vietnamensis TK-2009', 'Tylototriton sp. KIZ0808027', 
# 'Tylototriton sp. KIZ0808024', 'Tylototriton lizhenchangi', 'Tylototriton ziegleri', 
# 'Tylototriton panhai', 'Tylototriton liuyangensis', 'Tylototriton cf. asperrimus YPX 9918', 
# 'Tylototriton anhuiensis', 'Tylototriton broadoridgus', 'Tylototriton dabienicus', 
# 'Pachytriton labiatus', 'Pachytriton brevipes', 'Pachytriton archospotus', 'Pachytriton granulosus', 
# 'Pachytriton inexpectatus', 'Pachytriton moi', 'Pachytriton feii', 'Pachytriton xanthospilos', 
# 'Pachytriton wuguanfui', 'Pachytriton changi', 'Pachytriton airobranchiatus', 'Pachytriton sp. IMCB-2001', 
# 'Paramesotriton caudopunctatus', 'Paramesotriton deloustali', 'Paramesotriton guanxiensis', 
# 'Paramesotriton hongkongensis', 'Paramesotriton chinensis', 'Paramesotriton fuzhongensis', 
# 'Paramesotriton zhijinensis', 'Paramesotriton longliensis', 'Paramesotriton ermizhaoi', 
# 'Paramesotriton yunwuensis', 'Paramesotriton maolanensis', 'Paramesotriton wulingensis', 
# 'Paramesotriton qixilingensis', 'Paramesotriton aurantius', "Paramesotriton sp. 'Rafael de Sa'", 
# 'Paramesotriton sp. FMNH259125', 'Paramesotriton sp. ROM35433', 'Paramesotriton sp. TP28303', 
# 'Paramesotriton sp. HW-2009', 'Paramesotriton sp. GZNU2006030004', 'Paramesotriton sp. GZNU2006030005', 
# 'Paramesotriton sp. GZNU2006030006', 'Neurergus crocatus', 'Neurergus strauchii strauchii', 
# 'Neurergus strauchii barani', 'Neurergus kaiseri', 'Neurergus derjugini', 
# 'Lissotriton vulgaris meridionalis', 'Lissotriton vulgaris lantzi', 'Lissotriton vulgaris vulgaris', 
# 'Lissotriton vulgaris graecus', 'Lissotriton vulgaris pannonicus', 'Lissotriton vulgaris ssp. 1RuHF', 
# 'Lissotriton vulgaris ampelensis', 'Lissotriton vulgaris schmidtlerorum', 
# 'Lissotriton vulgaris schreiberi', 'Lissotriton helveticus helveticus', 
# 'Lissotriton montandoni', 'Lissotriton italicus', 'Lissotriton boscai boscai', 
# 'Lissotriton vulgaris x Lissotriton montandoni', 'Lissotriton kosswigi', 
# 'Ichthyosaura alpestris inexpectatus', 'Ichthyosaura alpestris alpestris', 
# 'Ichthyosaura alpestris cyreni', 'Ichthyosaura alpestris piperianus', 'Ichthyosaura alpestris reiseri', 
# 'Ichthyosaura alpestris serdarus', 'Ichthyosaura alpestris veluchiensis', 'Calotriton asper', 
# 'Calotriton arnoldi', 'Echinotriton andersoni', 'Echinotriton chinhaiensis', 'Echinotriton maxiquadratus', 
# 'Ommatotriton vittatus vittatus', 'Ommatotriton vittatus cilicensis', 'Ommatotriton nesterovi', 
# 'Ommatotriton ophryticus ophryticus', 'Laotriton laoensis', 'Salamandra atra atra', 
# 'Salamandra atra aurorae', 'Salamandra atra prenjensis', 'Salamandra atra pasubiensis', 
# 'Salamandra salamandra crespoi', 'Salamandra salamandra morenica', 'Salamandra salamandra longirostris', 
# 'Salamandra salamandra gallaica', 'Salamandra salamandra salamandra', 'Salamandra salamandra terrestris', 
# 'Salamandra salamandra bernardezi', 'Salamandra salamandra alfredschmidti', 
# 'Salamandra salamandra almanzoris', 'Salamandra salamandra bejarae', 'Salamandra salamandra corsica', 
# 'Salamandra salamandra fastuosa', 'Salamandra salamandra gigliolii', 'Salamandra salamandra werneri', \
# 'Salamandra salamandra beschkovi', 'Salamandra infraimmaculata infraimmaculata', 
# 'Salamandra infraimmaculata orientalis', 'Salamandra infraimmaculata semenovi', 'Salamandra lanzai', 
# 'Salamandra corsica', 'Salamandra algira algira', 'Salamandra algira tingitana', 
# 'Salamandra algira spelaea', 'Salamandra algira splendens', 'Mertensiella caucasica', 
# 'Chioglossa lusitanica', 'Lyciasalamandra luschani basoglui', 'Lyciasalamandra luschani finikensis', 
# 'Lyciasalamandra luschani luschani', 'Lyciasalamandra antalyana anatalyana', 
# 'Lyciasalamandra antalyana gocmeni', 'Lyciasalamandra fazilae ulfetae', 'Lyciasalamandra billae arikani', 
# 'Lyciasalamandra billae irfani', 'Lyciasalamandra billae yehudahi', 'Lyciasalamandra flavimembris', 
# 'Lyciasalamandra atifi', 'Lyciasalamandra helverseni', 'Salamandrina terdigitata', 
# 'Salamandrina perspicillata']
# []

#                                                                                                    /-Paramesotriton sp. 'Rafael de Sa', 377351
#                                                                                                   |
#                                                                                                   |--Paramesotriton sp. HW-2009, 608508
#                                                                                                   |
#                                                                                                   |--Paramesotriton sp. GZNU2006030004, 990546
#                                                                                                   |
#                                                                                                   |--Paramesotriton sp. GZNU2006030005, 990547
#                                                                /unclassified Paramesotriton, 2632613
#                                                               |                                   |--Paramesotriton sp. GZNU2006030006, 990548
#                                                               |                                   |
#                                                               |                                   |--Paramesotriton sp. FMNH259125,
# 385660
#                                                               |                                   |
#                                                               |                                   |--Paramesotriton sp. ROM35433, 385661
#                                                               |                                   |
#                                                               |                                    \-Paramesotriton sp. TP28303, 385662
#                                                               |
#                                                               |--Paramesotriton aurantius, 1930247
#                                                               |
#                                                               |--Paramesotriton wulingensis, 1325622
#                                                               |
#                                                               |--Paramesotriton caudopunctatus, 164969
#                                                               |
#                                                               |--Paramesotriton deloustali, 164970
#                                                               |
#                                          /Paramesotriton, 164968-Paramesotriton guanxiensis, 164971
#                                         |                     |
#                                         |                     |--Paramesotriton hongkongensis, 164972
#                                         |                     |
#                                         |                     |--Paramesotriton qixilingensis, 1483467
#                                         |                     |
#                                         |                     |--Paramesotriton longliensis, 608507
#                                         |                     |
#                                         |                     |--Paramesotriton yunwuensis, 942857
#                                         |                     |
#                                         |                     |--Paramesotriton maolanensis, 1264777
#                                         |                     |
#                                         |                     |--Paramesotriton zhijinensis, 489831
#                                         |                     |
#                                         |                     |--Paramesotriton chinensis, 189294
#                                         |                     |
#                                         |                     |--Paramesotriton fuzhongensis, 189295
#                                         |                     |
#                                         |                      \-Paramesotriton ermizhaoi, 663921
#                                         |
#                                         |                                     /-Tylototriton sp. KIZ0808027, 1150472
#                                         |                                    |
#                                         |                                    |--Tylototriton sp. KIZ0808024, 1150473
#                                         |                                    |
#                                         |                                    |--Tylototriton hainanensis, 385675
#                                         |                                    |
#                                         |                                    |--Tylototriton cf. vietnamensis DWW-2006, 385677
#                                         |                                    |
#                                         |                                    |--Tylototriton wenxianensis, 385678
#                                         |                                    |
#                                         |                                    |--Tylototriton asperrimus, 385674
#                                         |                                    |
#                                         |                                    |--Tylototriton liuyangensis, 1496723
#                                         |                                    |
#                                         |                                    |--Tylototriton cf. vietnamensis TK-2009, 1128649
#                                         |                                    |
#                                         |                    /Yaotriton, 926548-Tylototriton panhai, 1431319
#                                         |                   |                |
#                                         |                   |                |--Tylototriton notialis, 926545
#                                         |                   |                |
#                                         |                   |                |--Tylototriton vietnamensis, 926546
#                                         |                   |                |
#                                         |                   |                |--Tylototriton anhuiensis, 2058614
#                                         |                   |                |
#                                         |                   |                |--Tylototriton lizhenchangi, 1267581
#                                         |                   |                |
#                                         |                   |                |--Tylototriton ziegleri, 1267598
#                                         |                   |                |
#                                         |                   |                |--Tylototriton cf. asperrimus YPX 9918, 1729662
#                                         |                   |                |
#                                         |                   |                |--Tylototriton broadoridgus, 2080724
#                                         |                   |                |
#                                         |-Tylototriton, 129884                \-Tylototriton dabienicus, 2080725
#                                         |                   |
#                                         |                   |                    /-Tylototriton verrucosus, 164973
#                                         |                   |                   |
#                                         |                   |                   |--Tylototriton anguliceps, 1591418
#                                         |                   |                   |
#                                         |                   |                   |--Tylototriton daweishanensis, 1591419
#                                         |                   |                   |
#                                         |                   |                   |--Tylototriton podichthys, 1729661
#                                         |                   |                   |
#                                         |                   |                   |--Tylototriton kweichowensis, 385676
#                                         |                   |                   |
#                                         |                   |                   |--Tylototriton shanorum, 1485970
#                                         |                   |                   |
#                                         |                   |                   |--Tylototriton sp. MH-2011, 1040635
#                                         |                   |                   |
#                                         |                    \Tylototriton, 926547-Tylototriton uyenoi, 1431318
#                                         |                                       |
#                                         |                                       |--Tylototriton kachinorum, 2565413
#                                         |                                       |
#                                         |                                       |--Tylototriton taliangensis, 129885
#                                         |                                       |
#                                         |                                       |--Tylototriton pseudoverrucosus, 1357718
#                                         |                                       |
#                                         |                                       |--Tylototriton yangi, 1357719
#                                         |                                       |
#                                         |                                       |--Tylototriton shanjing, 356254
#                                         |                                       |
#                                         |                                       |--Tylototriton ngarsuensis, 2500536
#                                         |                                       |
#                                         |                                        \-Tylototriton himalayanus, 1783266
#                                         |
#                                         |-Ichthyosaura, 339873-Ichthyosaura alpestris, 54263
#                                         |
#                                         |                   /unclassified Pachytriton, 2621867-Pachytriton sp. IMCB-2001, 157709
#                                         |                  |
#                                         |                  |--Pachytriton xanthospilos, 1249911
#                                         |                  |
#                                         |                  |--Pachytriton labiatus, 156859
#                                         |                  |
#                                         |                  |--Pachytriton airobranchiatus, 2135270
#                                         |                  |