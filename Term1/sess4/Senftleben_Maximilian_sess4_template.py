# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 23:42:57 2018

@author: maser
"""

def parse_fasta(filename):
    fil=open(filename)
    listindex=[]
    listsequence=[]
    for line in fil:
        if line.startswith(">UniRef") == True:
            listindex.append(line.strip(">UniRef\n"))
        elif line.startswith(">") == True:
            listindex.append(line.strip(">\n"))
        else:
            listsequence.append(line.strip())
    zipdict=zip(listindex,listsequence)
    dic=dict(zipdict)
    
    return dic
    
    fil.close()
'''
uniref_aa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def merge_with_average(lab_A, lab_B, output_filename):
    # lab_A and lab_B are the names of the files, you need to open and parse them.
    f = open(output_filename, 'w')

    f.close()

def save_unique(lab_A, lab_B, output_filename):
    # lab_A and lab_B are the names of the files, you need to open and parse them.
    f = open(output_filename, 'w')

    f.close()
'''

if __name__ == '__main__':
    print(parse_fasta("test.txt"))