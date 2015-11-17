from glob import glob 

for fil in glob( 'out/*diff' ):
  with open( fil ) as fn:
    sub, que = fn.readlines()[0].split( '\t' )   
    d = '+'.join( [ '{}{}{}'.format(i, n+1, j).lower() for (n, (i, j)) in enumerate( zip( sub, que ) ) if i != j ] ) 
    if fil.split( '/' )[1].split( '.' )[0].split( '-' )[0] == d:
      print fil.split( '/' )[1].split( '.' )[0], 'has the correct sequence' 
    

