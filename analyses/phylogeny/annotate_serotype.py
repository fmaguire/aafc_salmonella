import ete3
import pandas as pd
import seaborn as sns

tree = ete3.Tree('pangenome_snps.phylip.contree')

serovars = pd.read_csv('../serotyping/final_serotypes.tsv', sep='\t', names=['Index', 'Serotype'])
serovars['Index'] = serovars['Index'].astype(str)
serovars = serovars.set_index('Index')

for leaf in tree.iter_leaves():
    serovar = serovars.loc[leaf.name, 'Serotype']
    leaf.add_features(serovar=serovar)

current_palette = sns.color_palette("hls", 7)

# no support for hsl straight out as far as I can tell
#serovar_colours = {k: v for k,v in zip(aafc_serovar.unique(), current_palette)}

sero_lut = dict(zip(['Kentucky', 'Hadar', 'Heidelberg',
                     'I:4,[5],12:i:', 'Enteritidis',
                     'Typhimurium', 'Thompson', 'None'], sns.color_palette().as_hex()))

ts = ete3.TreeStyle()

for n in tree.traverse():
    if n.support >= 95:
        nstyle = ete3.NodeStyle()
        nstyle["fgcolor"] = "red"
        nstyle["size"] = 5
    elif n.support < 95:
        nstyle = ete3.NodeStyle()
        nstyle["fgcolor"] = "black"
        nstyle["size"] = 5
    else:
        nstyle = ete3.NodeStyle()
        nstyle["fgcolor"] = "grey"
        nstyle["size"] = 1
    n.set_style(nstyle)

for l in tree.iter_leaves():
    # create a new label with a color attribute
    N = ete3.AttrFace("serovar", fgcolor=sero_lut[l.serovar])
    # label margins
    N.margin_top = N.margin_bottom = N.margin_left = 4.0
    # labels aligned to the same level
    l.add_face(N, 1, position='aligned')

# reroot on thompson
thompson_node = tree.search_nodes(name='3193')[0]

tree.set_outgroup(thompson_node)

ts.show_leaf_name = True
#ts.show_branch_support = True
tree.render('phylogeny_serotype.pdf', tree_style=ts)
