from glob import glob 
import pandas 
import json 

df = pandas.read_csv( 'transcriptic_mapping.csv' )  
df.set_index( 'mutant', inplace=True )  

picks = { } 
for fil in glob( 'out/*diff' ):
  with open( fil ) as fn:
    sub, que = fn.readlines()[0].split( '\t' )   
    d = '+'.join( [ '{}{}{}'.format(i, n+1, j).lower() for (n, (i, j)) in enumerate( zip( sub, que ) ) if i != j ] ) 
    if fil.split( '/' )[1].split( '.' )[0].split( '-' )[0] == d:
      thing = fil.split( '/' )[1].split( '.' )[0]
      picks.update( { d: df.loc[ thing ].well } ) 

print json.dumps( picks, indent=2 )
    

