#!/home/hithesh/miniconda3/bin/python

#usage: GC_percent_calc.py Input_file.fasta
#System requirements:python2 or 3 with biopython module installed
import sys
from Bio import SeqIO

filename=sys.argv[1]

fh= open(filename,'r')

F_1 = SeqIO.parse(fh, "fasta")

for F_2 in F_1:
    c=0
    a=0
    g=0
    t=0
    for x in str(F_2.seq):
        if "C" in x:
            c+=1    
        elif "G" in x:
            g+=1
        elif "A" in x:
            a+=1    
        elif "T" in x:
            t+=1
gc_percent=(g+c)*100.0/(a+t+g+c)
print("\nGC %","=",gc_percent,'\n\nCode by Hithesh')
