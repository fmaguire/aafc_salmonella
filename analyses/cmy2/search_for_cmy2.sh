#!/bin/bash

grep -A1 --no-group-separator "ARO_Name:CMY-2" card_prevalence/nucleotide_fasta_protein_homolog_model_variants.fasta  > CMY2_card_prev_all_sequences.fasta
cd-hit -i CMY2_card_prev_all_sequences.fasta -o CMY2_card_prev_uniq_sequences.fasta -c 1.0
mafft --maxiterate 1000 --localpair CMY2_card_prev_uniq_sequences.fasta > CMY2_alignment.afa
hmmbuild -n CMY2 CMY2_HMM CMY2_alignment.afa 
hmmpress CMY2_HMM

mkdir -p hmm_output

x=1
for genome in ../genomes/*.fasta
do
	nhmmscan -o hmm_output/$(basename $genome).stdout --tblout hmm_output/$(basename $genome).tbl --noali --notextw CMY2_HMM $genome && echo "$genome success" >> nhmmscan_run.log || echo "$genome failed" >> nhmmscan_run.log
	echo "$x of 166"
	x=$((x+1))
done
