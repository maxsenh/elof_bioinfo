#1.
def parse_fasta(filename):
    fil=open(filename)
    listindex=[]
    listsequence=[]
    for line in fil:
        if line.startswith(">") == True:
            listindex.append(line.strip(">\n"))
        else:
            listsequence.append(line.strip())
    zipdict=zip(listindex,listsequence)
    dic=dict(zipdict)
    fil.close()
    return dic

#2.
def merge_with_average(lab_A, lab_B, output_filename):
    # lab_A and lab_B are the names of the files, you need to open and parse them.
    labA=open(lab_A)
    labB=open(lab_B)
    f=open(output_filename,"w")
    dictA={}
    dictB={}
    for line in open(lab_A):
        if not line.strip():
            continue
        else:
            a,b=line.split()
            dictA.update({a:float(b)})    
    for line2 in open(lab_B):
        if not line2.strip():
            continue
        else:
            c,d=line2.split(",")
            dictB.update({c:float(d)})
    labA.close()
    labB.close()
    for key in dictB:
        if key in dictA:
            dictA.update({key:(dictB[key]+dictA[key])/2})
        else:
            dictA.update({key:dictB[key]})
    for writing in dictA:
        f.write("%s %f\n"%(writing,dictA[writing]))    
    f.close()  

#3.
def save_unique(lab_A, lab_B, output_filename):
    # lab_A and lab_B are the names of the files, you need to open and parse them.
    labA=open(lab_A)
    labB=open(lab_B)    
    f=open(output_filename,"w")
    dictA={}
    dictB={}
    for line in labA:
        if not line.strip():
            continue
        else:
            a,b=line.split()
            dictA.update({a:float(b)})
    for line2 in labB:
        if not line2.strip():
            continue
        else:
            c,d=line2.split(",")
            dictB.update({c:float(d)})
    labA.close()
    labB.close()
    for key in dictB:
        if key in dictA:
            dictA.pop(key)
        else:
            dictA.update({key:dictB[key]})
    for writing in dictA:
        f.write("%s %f\n"%(writing,dictA[writing]))    
    f.close()
import timeit

#4.
filetoclose=open("example.fasta")
uniref_aaset=set([])
for line1 in filetoclose:
    line=line1.strip("\n")
    if line[0]!=">":
        for s in line:
            uniref_aaset.add(s)
filetoclose.close()    
uniref_aa=list(uniref_aaset)
print(uniref_aa)    

uniref_aa=['Y', 'Q', 'O', 'A', 'L', 'U', 'V', 'K', 'R', 'W', 'D', 'Z', 'B', 'I', 'F', 'S', 'X', 'M', 'C', 'E', 'N', 'G', 'H', 'T', 'P']

    
if __name__ == '__main__':
    print(parse_fasta("example.fasta"))
    print(merge_with_average("resultslabA.txt","resultslabB.txt","withaverage.txt"))
    print(save_unique("resultslabA.txt","resultslabB.txt","onlyuniqe.txt"))

