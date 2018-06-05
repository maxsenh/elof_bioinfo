'''
#1.     ACDEFGHIKLMNPQRSTVWY
def is_protein(seq):
    aminoacids=["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"]
    return set(seq).issubset(aminoacids)
    # It should return either True or False, nothing else.
    
#2.
def longest_line(file_name):
    fil=open(file_name,"r").readlines()
    

#first way    
    listnumb=[]
    for i in range(len(fil)):
        listnumb.append(len(fil[i]))
        
    return max(listnumb)

#second way      
    return len(max(fil,key=len))
    
#third way   
    s=0
    for i in fil:
        if len(i)>s:
            s=len(i)
        return len(i)

'''
#3. or fasta function

def parse_fasta(file_name):
    fastafile=open(file_name)
    complete=fastafile.readlines()
    fastafile.close()
    newfasta=[]
    for i in complete:
        if i[0]!=">":
            newfasta.append(i.strip())
    return newfasta    
            
#complement function
def complementer(seq):
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
#-----------------------------------------------

def write_complement(input_file_name, output_file_name):
    a=parse_fasta(input_file_name)     #alle strings von dna_sequences.txt sind in einer liste
    out=open(output_file_name,"w")
    complementlist=[]
    for i in a:
        n=complementer(i)
        complementlist.append(n)
    for line in complementlist:
        out.write("complement\n")
        out.write(line)
        out.write("\n")
    out.close()
    return out
'''
    inpu=open(input_file_name)
    outpu=open(output_file_name,"w")

    lis=input_file_name
    out=open("output.txt","w")
    for f in lis:    
        new=""
        for n in f:
            if n=="A":
                new+="T"
            if n=="T":
                new+="A"
            if n=="G":
                new+="C"
            if n=="C":
                new+="G"
        out.write(new)

#4.     

def write_complement(input_file_name, output_file_name):
    inp=open(input_file_name)
    complete=inp.readlines()            #alle zeilen als strings in liste
    out=open(output_file_name,"w")
    oldfastalist=[]
    for i in complete:
        if i[0]!=">":
            oldfastalist.append(i.strip())  #jetzt sind alle fastas als strings in der liste
    complementlist=[]                       
    for s in oldfastalist:
        new=""
        for n in s:
            if n=="A":
                new+="T"
            if n=="T":
                new+="A"
            if n=="G":
                new+="C"
            if n=="C":
                new+="G"  
        complementlist.append(new)          #jetzt sind alle complementfastas in der liste
    for line in complementlist:
        out.write("complement\n")
        out.write(line)
        out.write("\n")
    
    
    return complementlist, oldfastalist, out'''

if __name__ == '__main__':
#    print(is_protein("AHCINENGPAMV"))
#    print(longest_line("longestline.txt"))
#    print(parse_fasta("dna_sequences.txt"))
    print(write_complement("dna_sequences.txt","output.txt"))
    
# Write all your tests here.
