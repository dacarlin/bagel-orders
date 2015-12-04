import screed 

with open( 'order_20151203.txt' ) as fn:
  lines = [ i.strip() for i in fn.readlines() if len( i ) > 3 ]

print 'mutant_label,oligo_label,sequence,scale,purification'
for line in lines:
  for record in screed.open( '../../oligos/{}.fasta'.format( line ) ):
    print '{0},{1},{1},25nm,standard'.format( line, record.sequence )

