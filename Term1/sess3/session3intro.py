"""
Introductory questions session 3
1. Make a function that translates DNA into RNA. All the occurences of T change to U.
2. Write a function that gets the complement of a DNA sequence.
3. Given a string of characters, write a function that returns True if it is a valid DNA sequence, and False if it isn’t. DNA contains uniquely GATC.
4. Make a program that reads in a file and writes back into a new file only the odd lines (every other line).
5. In the previous exercise, what happens if the input and output files have the same name?
6. Write a parser for a Multiple Sequence Alignment in Jones/ALN format. In this format, each line contains one protein sequence.

    PEPTIDE
    PEPT-KE

    Save them in a list, one line per element: ['PEPTIDE', 'PEPT-KE']
7. What happens if you forget to close a file in read mode? And in write mode?
"""

#1.
def sequence(seq):
    return seq.replace("T","U")

#2.
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

#3.
def stri(seq):
    DNA=["A","T","C","G"]
    return set(seq).issubset(DNA)

#4.
def writeinfile(fil):
    old=open(fil,"r")
    oldinstring=old.readlines()
    new=open("oldtext2.txt","w")
    for i in range(1,len(oldinstring),2):
        h=new.write(oldinstring[i])
    old.close()
    new.close()
    

#5.it removes all the even lines! gets shorter

#6.

#7. could be opened 

#check
if __name__=="__main__":
    print(sequence("ATTUG"))
    print(sequence2("ATTGCU"))
    print(stri("AAAGGgCCTT"))
    print(writeinfile("oddeven.txt"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
