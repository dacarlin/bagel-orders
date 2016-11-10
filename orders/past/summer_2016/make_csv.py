import pandas 
import screed 

df = pandas.read_csv( 'raw_collect.txt', sep='\s+' )

errors = []

print 'mutant_name,oligo_name,sequence,scale,purification\n',
for index, mutant in df.iterrows():
  try:
    for record in screed.open( '../../oligos/{}.fasta'.format( mutant.name.lower() ) ):
      print '{0},{0},{1},25nm,standard'.format( mutant.name, record.sequence ) 
  except Exception as e:
    errors += [ mutant ] # the pandas series so I can follow up with students  

print errors  
