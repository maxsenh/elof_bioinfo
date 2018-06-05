import numpy as np

#slow
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
#fast    
def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


#fast but different
def fibi2(n):
    a=0
    b=1
    for i in range(n):
        t=a
        a=b
        b=t+b    
    return a



#1 Intro
def fact(n):
    if n ==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fact(n-1)
        
#3 Intro
def subsequence(sequence):
    table=np.zeros(len(sequence))
    for i in range(len(sequence)):
        if sequence[i-1] < sequence[i]:
            table[i]=table[i-1]+1
        else:
            table[i]=1  
    return sequence[int(np.argmax(table)-table[np.argmax(table)]+1):np.argmax(table)+1] 
    
#1
def longest_substring(string1,string2):
    mat=np.zeros(shape=(len(string1),len(string2)))
    for x in range(len(string1)):
        for y in range(len(string2)):
            if x==0 or y==0:
                if string1[x]==string2[y]:
                    mat[x,y]=1
            else:
                if string1[x]==string2[y]:
                    mat[x,y]=mat[x-1,y-1]+1
    agmx=np.argmax(mat)
    iofagmx=np.unravel_index(agmx,mat.shape)
    numbofstr=int(np.max(mat))
    endstring=string1[iofagmx[0]-numbofstr+1:iofagmx[0]+1]
    return endstring
    
    
    

       
if __name__ == '__main__':
#    print(substring("dabanamvm","sanakds"))
#    print(fib(30))
#    print(fibi(35))    
#    print(fact(9))    
#    print(subsequence([3,4,5,1,2,6,8,10,9]))    

    assert longest_substring("jsanad","anasc") == "ana"
    assert longest_substring("ilovebioinformatics","icantwaitformax") == "forma"
    assert longest_substring("ironmansaregreat","triathlonforever") == "on"
    assert longest_substring("ihatewalking","nobikenolife") == "i"
    assert longest_substring("gofaster","govegan") == "go"    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
