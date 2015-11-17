# use: bash merge.bash <transcriptic mapping CSV>

for i in $( cut -d, -f3 $1 ); do
  ASEQ=fwd_reads/$i*seq
  BSEQ=rev_reads/$i*seq
  merger -asequence $ASEQ -bsequence $BSEQ -sreverse2 -outfile out/$i.merger -outseq out/$i.fasta
done 
