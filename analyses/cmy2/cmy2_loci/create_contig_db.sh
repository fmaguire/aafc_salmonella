#for i in *.fa;
#do 
#    anvi-script-FASTA-to-contigs-db $i
#done
#
#echo -e "name\tcontigs_db_path" > genomes.tsv
#mkdir -p rgi aa
#for i in *.db; 
#do 
#    echo -e "cmy$(echo $i | awk -F '_' '{print $1}')\t$i" >> genomes.tsv; 
#    #anvi-get-sequences-for-gene-calls -c $i --get-aa-sequences -o aa/$i.faa
#    #rgi main -i aa/$i.faa -o rgi/$i -n 2 -t protein
#    #tblastn -query aa/$i.faa -db vf/sequences -outfmt 6 -evalue 1E-20 > vf/$i.out6
#    #cat rgi/$i.txt | awk -F $'\t' 'BEGIN {OFS = FS; print "gene_callers_id", "source", "accession", "function", "e_value"}; NR>1{print $1, $6"RGI", "", $9, 0}' > aa/$i.tsv
#    #cat vf/$i.out6 | awk -F $'\t' 'BEGIN {OFS = FS} {print $1, "VFDB", "", "$2", 0}' >> aa/$i.tsv
#    #anvi-import-functions -c $i -i aa/$i.tsv
#done

anvi-gen-genomes-storage -e genomes.tsv -o CMY2LOCI-GENOMES.db

#anvi-pan-genome -g CMY2LOCI-GENOMES.db -n CMY2LOCI

