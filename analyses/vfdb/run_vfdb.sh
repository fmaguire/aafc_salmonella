#for genome in ../../data/genomes/*.gz;
#do
#    abricate --db vfdb $genome > $(basename $genome | awk -F '_' '{print $1}').tab
#done
abricate --summary *.tab > all_vfdb.tsv
