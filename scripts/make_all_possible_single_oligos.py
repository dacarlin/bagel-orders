import screed 
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument( 'wt_seq', help='Wild type sequence' ) 
args = parser.parse_args() 

def reverse_complement( nucleotide_sequence ):
  return ''.join([ { 'a': 't', 't': 'a', 'c': 'g', 'g': 'c' }[b] for b in nucleotide_sequence ])[::-1] 

for record in screed.open( args.wt_seq ):

  codons = [ record.sequence[i:i+3] for i in range( 0, len( record.sequence ), 3 ) ] 
  ecoli_prefer_codons = { 'g':'ggc', 'a':'gcg', 'v':'gtg', 'f':'ttt', 'e':'gaa', 'd':'gat', 'n':'aac', 
                          'h':'cat', 'p':'ccg', 'q':'cag', 'w':'tgg', 'y':'tat', 'i':'att', 'm':'atg', 
                          'c':'tgc', 'k':'aaa', 'l':'ctg', 'r':'cgt', 't':'acc', 's':'agc'}

  translate = { 'ata':'i', 'atc':'i', 'att':'i', 'atg':'m', 'aca':'t', 'acc':'t', 'acg':'t', 'act':'t', 
                'aac':'n', 'aat':'n', 'aaa':'k', 'aag':'k', 'agc':'s', 'agt':'s', 'aga':'r', 'agg':'r', 
                'cta':'l', 'ctc':'l', 'ctg':'l', 'ctt':'l', 'cca':'p', 'ccc':'p', 'ccg':'p', 'cct':'p', 
                'cac':'h', 'cat':'h', 'caa':'q', 'cag':'q', 'cga':'r', 'cgc':'r', 'cgg':'r', 'cgt':'r', 
                'gta':'v', 'gtc':'v', 'gtg':'v', 'gtt':'v', 'gca':'a', 'gcc':'a', 'gcg':'a', 'gct':'a', 
                'gac':'d', 'gat':'d', 'gaa':'e', 'gag':'e', 'gga':'g', 'ggc':'g', 'ggg':'g', 'ggt':'g', 
                'tca':'s', 'tcc':'s', 'tcg':'s', 'tct':'s', 'ttc':'f', 'ttt':'f', 'tta':'l', 'ttg':'l', 
                'tac':'y', 'tat':'y', 'taa':'_', 'tag':'_', 'tgc':'c', 'tgt':'c', 'tga':'_', 'tgg':'w'} 

  for i, codon in enumerate( codons ):
    if 5 < i < len( codons ) - 5:

      print '---'
      print 'zero index:', i
      print 'one index:', i+1 
      print 'original codon:', codon 
      print 'original region:', codons[i-4:i+5] #gives 3 * 4 = 12 bp on each side, 12 + 12 + 3 = 27 bp oligo  
      print 'left flank:', codons[i-4:i]
      print 'right flank:', codons[i+1:i+5] 

      for j, (aa, new_codon) in enumerate( ecoli_prefer_codons.iteritems() ):
        print 'new amino acid:', aa 
        print 'new codon:', new_codon
        print 'new region:', codons[i-4:i] + [ new_codon ] + codons[i+1:i+5] 

        name_of_mutant = '{}{}{}'.format( translate[ codon ] , i+1, aa ) 
        new_region = codons[i-4:i] + [ new_codon ] + codons[i+1:i+5] 

        print 'reverse_complement:', reverse_complement( ''.join( new_region ) )

        with open( 'oligos/{}.fasta'.format( name_of_mutant) , 'w' ) as fasta:
          fasta.write( '>{}\n'.format( name_of_mutant ) )
          fasta.write( reverse_complement( ''.join( new_region ) ) ) 
