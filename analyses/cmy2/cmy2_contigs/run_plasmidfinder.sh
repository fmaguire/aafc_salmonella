for contig in *.fa;
do
    abricate --db plasmidfinder $genome > $(basename $contig | awk -F '_' '{print $1}').tab
done
abricate --summary *.tab > cmy2_all_plasmids.tsv

