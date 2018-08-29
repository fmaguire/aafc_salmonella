from glob import glob
import pandas as pd


if __name__ == '__main__':

    # SeqSero parsing
    # outputs everything to separate file
    seqsero_results = {'ID': [], 'genome': [], 'antigenic_profile': [], 'serotype': []}
    for seqsero_run in glob('serotype/SeqSero/SeqSero_result_*'):
        result = seqsero_run + '/Seqsero_result.txt'
        genome, profile, serotype, ID = None, None, None, None
        with open(result) as fh:
            for line in fh:
                if line.startswith('Input files:'):
                    genome = line.split(':')[-1].strip().replace('.fasta.gz.fixed.fasta', '')
                    ID = "_".join(genome.split('_')[:-1])
                elif line.startswith('Predicted antigenic profile:'):
                    profile = line.split(':')[-1].strip()
                elif line.startswith('Predicted serotype(s):'):
                    serotype = line.split(':')[-1].strip().replace('*', '')

            if genome and profile and serotype and ID:
                seqsero_results['genome'].append(genome)
                seqsero_results['ID'].append(ID)
                seqsero_results['antigenic_profile'].append(profile)
                seqsero_results['serotype'].append(serotype)
            else:
                print("Missing information in: ", result)

    seqsero_df = pd.DataFrame(seqsero_results)
    seqsero_df = seqsero_df.set_index('ID')
    seqsero_df.to_csv('seqsero.tsv', sep='\t')
