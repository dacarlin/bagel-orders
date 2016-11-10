from random import randint
from glob import glob 

all_oligos = glob( '../../oligos/*fasta' )

for i in range( 20 ):
  print all_oligos[ randint( 0, len( all_oligos ) ) ].split( '/' )[-1].split( '.' )[0] 
