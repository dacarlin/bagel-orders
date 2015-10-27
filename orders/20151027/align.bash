for i in out/*fasta; do
  blastn -subject bagel.fasta -query $i -out ${i/fasta/blast}  
done 
