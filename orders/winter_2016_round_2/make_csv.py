import screed 
from sys import argv

with open( argv[1] ) as fn:
  lines = [ i.strip() for i in fn.readlines() if len( i ) > 3 ]

with open( 'we_have_in_house.txt' ) as inhouse:
  inhouse = [ i.strip() for i in inhouse.readlines() if len( i ) > 3 ]

already_got = set( lines ).intersection( set( inhouse ) )  
# use to see if we already have mutant  

print 'mutant_label,oligo_label,sequence,scale,purification'
for line in lines:
  if line not in already_got:
    for record in screed.open( '../../oligos/{}.fasta'.format( line ) ):
      print '{0},{1},{1},25nm,standard'.format( line, record.sequence )

