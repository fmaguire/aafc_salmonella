#!/usr/bin/env python
import glob
import sys
import gzip
import tqdm

if __name__ == '__main__':
     hits = {}
     for hmm_table in glob.glob("hmm_output/*.tbl"):
         with open(hmm_table) as fh:
             locus_info = []
             for line in fh:
                 line = line.strip()
                 if line.startswith("# Query file:"):
                     genome = line.replace("# Query file:", '')
                     genome = genome.strip() + '.gz.fixed'
                 if line.startswith('CMY2'):
                     line = line.split()

                     # if better than min e-value
                     if float(line[12]) <= float(sys.argv[1]):
                         contig = line[2]
                         start = int(line[6])
                         end = int(line[7])
                         strand = line[11]
                         locus_info.append((contig, start, end, strand))
             if len(locus_info) > 0:
                 hits[genome] = locus_info

     with open('cmy2_loci.fasta', 'w') as loci_fh:
         with open('cmy2_contig.fasta', 'w') as contig_fh:
             for genome in tqdm.tqdm(hits.keys()):
                 with gzip.open(genome, 'rb') as genome_fh:
                     ix = 0
                     for line in genome_fh:
                         ix+=1
                         if ix % 2 == 1:
                             accession = line.strip().decode("utf-8")
                             continue
                         if ix % 2 == 0:
                             seq = line.strip().decode("utf-8")

                         for hit_contig, start, end, strand in hits[genome]:
                             if accession.startswith(">" + hit_contig):
                                 #5bkp +/-
                                 #if strand == '-':
                                 #    start, end = end, start

                                 region_start = start - 5000
                                 if region_start < 0:
                                     region_start = 0

                                 region_end = end + 5000
                                 if region_end > len(seq):
                                     region_end = len(seq)

                                 seq_frag = seq[region_start: region_end]

                                 print(len(seq_frag))

                                 loci_fh.write('{} {}:{}\n{}\n'.format(accession,
                                                                  region_start,
                                                                  region_end,
                                                                  seq_frag))

                                 contig_fh.write('{}\n{}\n'.format(accession,
                                                                   seq))

