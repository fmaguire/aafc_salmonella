#for i in *.fa;
#do 
#    anvi-script-FASTA-to-contigs-db $i
#done

mkdir -p rgi aa vf nt 
for i in *.db; 
do 
    #anvi-get-sequences-for-gene-calls -c $i -o nt/$i.fa
    #centrifuge -f -x centrifuge/p+h+v/p+h+v nt/$i.fa -S centrifuge/$i.tsv
    #anvi-import-taxonomy-for-genes -c $i -i centrifuge/$i.tsv centrifuge/$i.tsv -p centrifuge

    anvi-get-sequences-for-gene-calls -c $i --get-aa-sequences -o aa/$i.faa
    rgi main -i aa/$i.faa -o rgi/$i -n 2 -t protein
    tblastn -query aa/$i.faa -db vf/sequences -outfmt 6 -evalue 1E-20 > vf/$i.out6
    cat rgi/$i.txt | awk -F $'\t' 'BEGIN {OFS = FS; print "gene_callers_id", "source", "accession", "function", "e_value"}; NR>1{print $1, $6"RGI", "", $9, 0}' > aa/$i.tsv
    cat vf/$i.out6 | awk -F $'\t' 'BEGIN {OFS = FS} {print $1, "VFDB", "", "$2", 0}' >> aa/$i.tsv
    anvi-import-functions -c $i -i aa/$i.tsv
done

anvi-gen-genomes-storage -e genomes.tsv -o SUBSET-GENOMES.db
anvi-pan-genome -g SUBSET-GENOMES.db -n SUBSET
anvi-import-misc-data -p SUBSET/SUBSET-PAN.db -t layer_orders phylogeny_data.txt
anvi-import-misc-data serotypes.tsv -p SUBSET/SUBSET-PAN.db --target-data-table layers
