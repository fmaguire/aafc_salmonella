makeblastdb -dbtype nucl -in mutator_sequences.fasta
for genome in ../../data/genomes/*.gz;
do 
    zcat $genome > $(basename $genome)
    blastn -query $(basename $genome) -db mutator_sequences.fasta -outfmt 6 > $(basename $genome | awk -F '_' '{print $1}').out6
    rm $(basename $genome)
done
