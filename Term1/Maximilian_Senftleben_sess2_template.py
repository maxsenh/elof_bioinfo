def compute_gc(sequence):
    g=sequence.count("G")
    c=sequence.count("C")
    total=len(sequence)
    gccontent=(g+c)/total
    return gccontent
    '''Compute the GC-content of a nucleotide string as a 
    number between 0 and 1'''
    
def dist(seqA, seqB):
    '''Compute the Hamming distance between A and B
    Example: dist('GGGAT', 'GGCCT') = 2
    '''
    if len(seqA) == len(seqB):
        sum=0
        for s in range(len(seqA)):
            if seqA[s]!=seqB[s]:
                sum+=1

    else:
        return "sequences not the same lenght"
    return sum
	
def score(a, b):
    if a==b:
        return 1
    elif a!=b:
        return 0
    else:
        return "NO"
    
    '''Write a function that takes two characters and returns 
    1 if they are identical and 0 otherwise'''
	
def matchStrings(stringA, stringB):
    '''Write a function that takes two strings and return the number 
    of matches, "GGGAT" and "GGCCT" should return 3.
    Hint! Use the score function.'''
    sum2=0
    smallest=min(len(stringA),len(stringB))
    for i in range(0,smallest):
        if stringA[i]==stringB[i]:
            sum2+=1
    return sum2

        
    
    

if __name__=="__main__":
    print(compute_gc("GCGTTAGCTATGCTA"))
    print(dist("GCJD","GCKC"))
    print(score("b","l"))
    print(matchStrings("GGGATA","GGCCTADD"))
