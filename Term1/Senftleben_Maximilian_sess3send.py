
#1.     ACDEFGHIKLMNPQRSTVWY
def is_protein(seq):
    aminoacids=["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"]
    return set(seq).issubset(aminoacids)

#2.
def longest_line(file_name):
    filetoclose=open(file_name,"r")
    fil=filetoclose.readlines()
    listnumb=[]
    for i in fil:
        listnumb.append(len(i.strip()))
    filetoclose.close()
    return max(listnumb)


#3.
def parse_fasta(file_name):
    fastafile=open(file_name)
    complete=fastafile.readlines()
    newfasta=[]
    for i in complete:
        if i[0]!=">":
            newfasta.append(i.strip())
    fastafile.close()
    return newfasta    
   
#4.     
def write_complement(input_file_name, output_file_name):
    inp=open(input_file_name)
    complete=inp.readlines()            
    out=open(output_file_name,"w")


    for line in complete:
        if line[0]==">":
            out.write(line.strip()+" complement\n")
        else:
            for s in line:                
                new=""
                if s=="A":
                    new+="T"
                if s=="T":
                    new+="A"
                if s=="G":
                    new+="C"
                if s=="C":
                    new+="G" 
                out.write(new)
            out.write("\n")
    inp.close() 
    out.close()
  
if __name__ == '__main__':
    print(is_protein("AHCINENGPAOMV"))
    print(longest_line("longestline.txt"))
    print(parse_fasta("testfasta.txt"))
    print(write_complement("dna_sequences.txt","output.txt"))
    
