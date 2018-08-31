for genome in ../../data/genomes/*.gz;
do
    abricate --db plasmidfinder $genome > $(basename $genome | awk -F '_' '{print $1}').tab
done
abricate --summary * > all_plasmids.tsv

