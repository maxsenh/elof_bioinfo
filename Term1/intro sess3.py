'''Intro'''

def sequence(seq):
    new=seq.replace("T","U")
    return new
    
def sequence2(seq):
    new=""
    for n in seq:
        if n=="A":
            new+="T"
        if n=="T":
            new+="A"    
        if n=="G":
            new+="C"  
        if n=="C":
            new+="G"          
    return new
    
def stri(seq):
    DNA=["A", "T", "C", "G"]
    return set(seq).issubset(DNA)
    


print(sequence("ATTGCCGTAGT"))
print(sequence2("ATGTGCGTAGCGTAA"))
print(stri("AAAV"))
