import ete3
import copy
import pandas as pd
import seaborn as sns

tree = ete3.Tree('pangenome_snps.phylip.contree')


serovars = pd.read_csv('../serotyping/final_serotypes.tsv', sep='\t', names=['Index', 'Serotype'])
serovars['Index'] = serovars['Index'].astype(str)
serovars = serovars.set_index('Index')
print(serovars)

for leaf in tree.iter_leaves():
    serovar = serovars.loc[leaf.name, 'Serotype']
    leaf.add_features(serovar=serovar)


sns.set_palette('colorblind')
# no support for hsl straight out as far as I can tell
#serovar_colours = {k: v for k,v in zip(aafc_serovar.unique(), current_palette)}

sero_lut = dict(zip(['Kentucky', 'Hadar', 'Heidelberg',
                     'I:4,[5],12:i:', 'Enteritidis',
                     'Typhimurium', 'Thompson', 'None'], sns.color_palette('colorblind').as_hex()))

print(sero_lut)

ts = ete3.TreeStyle()
ts.mode = 'c'
#ts.scale = 5000


for n in tree.traverse():
    if n.support >= 95:
        nstyle = ete3.NodeStyle()
        nstyle["fgcolor"] = "red"
        nstyle["size"] = 5
    elif n.support < 95:
        nstyle = ete3.NodeStyle()
        nstyle["fgcolor"] = "black"
        nstyle["size"] = 5
    #else:
    #    nstyle = ete3.NodeStyle()
    #    nstyle["fgcolor"] = "grey"
    #    nstyle["size"] = 1
    n.set_style(nstyle)





#for l in tree.iter_leaves():
#    l.img_style['bgcolor'] = sero_lut[l.serovar]

# hadar
hadar = tree.get_common_ancestor('3125', '3158')
hadar_style = ete3.NodeStyle()
hadar_style['bgcolor'] = sero_lut['Hadar']
hadar.set_style(hadar_style)

# heidelberg
heid = tree.get_common_ancestor('1760', '3342')
heid_style = ete3.NodeStyle()
heid_style['bgcolor'] = sero_lut['Heidelberg']
heid.set_style(heid_style)

# typh
typh = tree.get_common_ancestor('3151', '3199')
typh_style = ete3.NodeStyle()
typh_style['bgcolor'] = sero_lut['Typhimurium']
typh.set_style(typh_style)

typh_node = tree.search_nodes(name='3333')[0]
typh_node.set_style(typh_style)

# i4
i4 = tree.get_common_ancestor('1893', '1792')
i4_style = ete3.NodeStyle()
i4_style['bgcolor'] = sero_lut['I:4,[5],12:i:']
i4.set_style(i4_style)

# kentucky
kent = tree.get_common_ancestor('3336', '3184')
kent_style = ete3.NodeStyle()
kent_style['bgcolor'] = sero_lut['Kentucky']
kent.set_style(kent_style)

kent = tree.get_common_ancestor('3326', '3184')
kent.set_style(kent_style)

#kent = tree.get_common_ancestor('3132', '3317')
#kent.set_style(kent_style)

# Enter sub group
enter = tree.get_common_ancestor('1797', '3303')
enter_style = ete3.NodeStyle()
enter_style['bgcolor'] = sero_lut['Enteritidis']
enter.set_style(enter_style)

enter = tree.search_nodes(name = '1758')[0]
enter.set_style(enter_style)





# reroot on thompson
thompson_node = tree.search_nodes(name='3193')[0]
thompson_node.img_style['bgcolor'] = sero_lut['Thompson']

# highlight the subsampled taxa

subset_nodes = []
sub_tree = copy.copy(tree)
for i in "1760 3125 3145 3193 1778 3126 3166 3333 1797 3132 3179 3339 1893 3142 3186".split():
    node = sub_tree.search_nodes(name=i)[0]
    subset_nodes.append(node)
    node.name = serovars.loc[node.name, 'Serotype'].replace(',', '_').replace('[', '').replace(']', '').replace(':', '') + '_' + node.name




sub_tree.prune(subset_nodes)
with open('../pangenome/anvio_subsample/phylogeny_data.txt', 'w') as fh:
    fh.write('item_name\tdata_type\tdata_value\n')
    fh.write('Core_SNP_Phylogeny\tnewick\t{}\n'.format(sub_tree.write(format=1)))






for node in subset_nodes:
    node.name = node.name + " * "







tree.set_outgroup(thompson_node)
for l in tree.iter_leaves():
    l.name = l.name + " (" + l.serovar + ")"


ts.show_leaf_name = True
#ts.show_branch_support = True
tree.render('phylogeny_serotype.pdf', tree_style=ts)
