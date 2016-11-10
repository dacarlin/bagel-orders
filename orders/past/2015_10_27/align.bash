for i in out/*fasta; do
  blastn -subject bagel.fasta -query $i -out ${i/fasta/blast}  
  blastn -subject bagel.fasta -query $i -outfmt "6 sseq qseq" -out ${i/fasta/aligned} 
  tblastn -subject $i -query bglb.pep -outfmt "6 qseq sseq" -out ${i/fasta/diff} 
done 
