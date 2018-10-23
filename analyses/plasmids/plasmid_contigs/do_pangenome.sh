for i in *.fas; 
do 
    rgi main -i $i -o rgi/$i -n 2 --low_quality
    blastn -query $i -db vf/sequences -outfmt 6 -evalue 1E-20 > vf/$i.out6
done

