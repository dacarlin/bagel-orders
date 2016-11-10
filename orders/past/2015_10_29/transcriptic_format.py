import sys
import screed  

with open( '../../../bagel-main/roster.csv' ) as roster:
  haves = [ line.split( ',' )[1] for line in roster.readlines() ] 
  #print haves 

print 'mutant_label,oligo_label,sequence,scale,purification' 

for line in sys.stdin:
  if line.strip() not in haves:
    for record in screed.open( '../../oligos/{}.fasta'.format( line.strip() ) ):
      print '{0},{0},{1},25nm,standard'.format( line.strip(), record.sequence ) 
      


